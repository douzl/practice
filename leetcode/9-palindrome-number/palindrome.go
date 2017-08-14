package main

import "fmt"

func main() {
	x := 12321
	fmt.Println(isPalindrome(x))
}

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	len := 1
	for x/len >= 10 {
		len *= 10
	}

	for x > 0 {
		left := x / len
		right := x % 10

		if left != right {
			return false
		}

		x = (x % len) / 10
		len /= 100
	}
	return true
}
