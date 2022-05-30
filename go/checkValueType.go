package main

import (
 "fmt"
)

type Tqest struct {
	Tone string
	Ttwo int
	Tthree float64
}


func main() {

	var test Tqest
	test.Tone = "hello"
	test.Ttwo = 100
	test.Tthree = 10.20

	fmt.Printf("%T\n", test)

        // v1 := "123456"
        // v2 := 12

        // fmt.Printf("v1 type:%T\n", v1)
        // fmt.Printf("v2 type:%T\n", v2)



}