package main

import (
	"fmt"
	"math"
)

func main() {
	x := -12345678
	fmt.Println(reverse(x))
}

func reverse(x int) int {
	const max = 2147483647
	var res int

	for x != 0 {
		if math.Abs(float64(res)) > max/10 {
			return 0
		}
		res = res*10 + x%10
		x = x / 10
	}

	return res
}
