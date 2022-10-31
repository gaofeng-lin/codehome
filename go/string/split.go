package main

import (
	"fmt"
	"strings"
)

func main() {
	str1 := "test03/local (2).zip/23"
	str2 := strings.Split(str1, "/")
	filename := str2[len(str2)-1]

	fmt.Println(filename)
}