package main

import (
	"fmt"
)

func main() {
	tmp_map := make(map[string]interface{})
	// x :=3
    // a := [x]int{1,2,3}
	// a :=[] int {1,2,3}
	a := make([]interface{},0)
	a = append(a,"wqe",2,3)
    tmp_map["ol"] = a
    fmt.Println(tmp_map)
}