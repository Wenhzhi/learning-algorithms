package main

import (
	"encoding/json"
	"fmt"
)

func maxIncreaseKeepingSkyline(grid [][]int) (ans int) {
	n := len(grid)
	rowMax := make([]int, n)
	colMax := make([]int, n)
	for i, row := range grid {
		for j, h := range row {
			rowMax[i] = max(rowMax[i], h)
			colMax[j] = max(colMax[j], h)
		}
	}
	for i, row := range grid {
		for j, h := range row {
			ans += min(rowMax[i], colMax[j]) - h
		}
	}
	return
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}


func main() {
	var gridInput string
	if _, err := fmt.Scanf("%s", &gridInput); err != nil {
		println("err:", err)
		return
	}

	grid := make([][]int, 0)
	if gridJsonErr := json.Unmarshal([]byte(gridInput), &grid); gridJsonErr != nil {
		println("gridJsonErr: ", gridJsonErr)
		return
	}

	println(maxIncreaseKeepingSkyline(grid))
}
