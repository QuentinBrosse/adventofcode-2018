#!/usr/bin/env python3

import os
import re
from datetime import datetime
from collections import defaultdict, Counter
cwd = dir_path = os.path.dirname(os.path.realpath(__file__))
inputPath = os.path.join(cwd, "input.txt")

def prepare():
    logs = []
    log_rgx = re.compile("\[([0-9-: ]+)\] (.*)")
    guard_rgx = re.compile("Guard #(\d+) begins shift")
    guards = {}
    with open(inputPath, "r") as f:
        for line in f:
            timestamp, log = log_rgx.findall(line)[0]
            guard = guard_rgx.findall(log)
            guard = int(guard[0]) if len(guard) > 0 else None
            dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
            logs.append({
                "timestamp": dt,
                "guard": guard,
                "msg": log,
            })
            if guard is not None and guard not in guards:
                guards[guard] = Counter()
    logs.sort(key=lambda l:l["timestamp"])

    i = 0
    current_guard = None
    while i < len(logs):
        if logs[i]["guard"]:
            current_guard = logs[i]["guard"]
            i += 1
        if i < len(logs) and logs[i]["msg"] == "falls asleep":
            inner = logs[i]["timestamp"].minute
            i += 1
            outer = logs[i]["timestamp"].minute
            i += 1
            for m in range(inner, outer):
                guards[current_guard][m] += 1

    return guards

def puzzle1(guards):
    best_sleeper = (0, 0) # guard_id, total_minutes
    for guard_id, minutes in guards.items():
        total = sum(minutes.values())
        if total > best_sleeper[1]:
            best_sleeper = (guard_id, total)

    best_sleeper_id = best_sleeper[0]
    return best_sleeper_id * guards[best_sleeper_id].most_common(1)[0][0]

def puzzle2(guards):
    higher = (0, 0, 0) # guard_id, minute, minute_counter
    for guard_id, minutes in guards.items():
        total = sum(minutes.values())
        hm = minutes.most_common(1)
        if len(hm) > 0 and hm[0][1] > higher[2]:
            higher = (guard_id, hm[0][0], hm[0][1])

    return higher[0] * higher[1]

if __name__ == "__main__":
    guards = prepare()

    print("Rep 1: {}".format(puzzle1(guards)))
    print("Rep 2: {}".format(puzzle2(guards)))
