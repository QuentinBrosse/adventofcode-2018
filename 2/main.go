package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func orPanic(err error) {
	if err != nil {
		panic(err)
	}
}

func puzzle1(inputs []string) int {
	boxes2 := 0
	boxes3 := 0

	for _, id := range inputs {
		m := make(map[rune]int)
		for _, r := range id {
			m[r]++
		}

		for _, r := range m {
			if r == 2 {
				boxes2++
				break
			}
		}

		for _, r := range m {
			if r == 3 {
				boxes3++
				break
			}
		}
	}

	return boxes2 * boxes3
}

func diffOne(a, b string) (bool, int) {
	luck := 0
	diffIdx := 0

	for i := range a {
		if a[i] != b[i] {
			luck++
			if luck > 1 {
				return false, 0
			}
			diffIdx = i
		}
	}

	return luck == 1, diffIdx
}

func puzzle2(inputs []string) string {
	var boxes []string

	for _, id := range inputs {
		m := make(map[rune]int)
		for _, r := range id {
			m[r]++
		}

		for _, r := range m {
			if r == 2 || r == 3 {
				boxes = append(boxes, id)
			}
		}
	}

	for _, b1 := range boxes {
		for _, b2 := range boxes {
			ok, diffIdx := diffOne(b1, b2)
			if ok {
				return b1[:diffIdx] + b1[diffIdx+1:]
			}
		}
	}

	return "???"
}

func main() {
	body, errRead := ioutil.ReadFile("./input.txt")
	orPanic(errRead)
	inputs := strings.Split(string(body), "\n")

	fmt.Printf("Res 1: %v\n", puzzle1(inputs))
	fmt.Printf("Res 2: %v\n", puzzle2(inputs))
}
