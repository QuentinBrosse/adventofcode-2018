package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func orPanic(err error) {
	if err != nil {
		panic(err)
	}
}

func puzzle1(inputs []string) int {
	sum := 0

	for _, input := range inputs {
		if input == "" {
			continue
		}
		i, err := strconv.Atoi(input)
		orPanic(err)
		sum += i
	}

	return sum
}

func puzzle2(inputs []string) int {
	sum := 0
	sumMap := make(map[int]int)

	for {
		for _, input := range inputs {
			if input == "" {
				continue
			}
			i, err := strconv.Atoi(input)
			orPanic(err)
			sum += i
			sumMap[sum]++
			if sumMap[sum] == 2 {
				return sum
			}
		}
	}
}

func main() {
	body, errRead := ioutil.ReadFile("./input.txt")
	orPanic(errRead)
	inputs := strings.Split(string(body), "\n")

	fmt.Printf("Res 1: %v\n", puzzle1(inputs))
	fmt.Printf("Res 2: %v\n", puzzle2(inputs))
}
