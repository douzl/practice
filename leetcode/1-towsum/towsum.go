package main

import "fmt"

func twoSum(nums []int, target int) []int {
     sumNum := make([]int, 2)
     for i, num := range nums {
       for j, num2 := range nums {
           fmt.Println("num1:", num, i)
           fmt.Println("num2:", num2, i)
           if i != j {
             if num + num2 == target {
               sumNum[0] = i
               sumNum[1] = j
               return sumNum
             }
           }
       }
     }
     return nil
}

func main() {
  nums := []int{5, 7, 11, 2}
  target := 9
  fmt.Println(twoSum(nums, target))
}
