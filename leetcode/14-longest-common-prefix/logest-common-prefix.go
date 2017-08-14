package main

import (
  "fmt"
  "strings"
)

func longestCommonPrefix(strs []string) string {
    if len(strs) == 0 {
      return ""
    }

    var prefix string
    for i, str := range strs {
      fmt.Println(prefix)
      if i == 0 {
        prefix = strs[i]
        continue
      }

      if len(prefix) == 0 || len(str) == 0 {
        return ""
      }

      for strings.Index(str, prefix) != 0 {
        prefix = prefix[0:len(prefix) - 1]
      }
    }
    return prefix
}

func main() {
  strs := []string{"flower", "flow", "flight"}
  fmt.Println(longestCommonPrefix(strs))
}
