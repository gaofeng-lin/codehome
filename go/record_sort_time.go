package main

import (
   "fmt"
   "time"
)

func main() {
   var a []int
   for i := 0; i < 1e4; i++ {
      a = append(a, 1e4-i)
   }
   start := time.Now()
   fmt.Println(start)
   InsertSort(a)
   cost := time.Since(start)
   for _, el := range a {
      fmt.Println(el)
   }
   fmt.Println("cost:", cost)
}

func InsertSort(a []int) {
    for i := 1; i < len(a); i++ {
        tmp, j := a[i], i
        for ; j > 0 && a[j-1] >= tmp; j-- {
            a[j] = a[j-1]
        }
        a[j] = tmp
    }
}