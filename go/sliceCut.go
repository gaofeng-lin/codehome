package main

import (
	"fmt"
	// "io/ioutil"
	// "strings"
	// "reflect"
)

func main() {

	str := []int{0,1,2,3,4,5,6} 

	halfFront := len(str) / 2
	strhalf := str[:halfFront]
	strhalf2 := str[halfFront:]
	fmt.Println(strhalf)
	fmt.Println(strhalf2)
	// i := 0
	
	// for i < 2 {
	// 	strhalf := str[:halfFront]
	// 	i += i
	// 	fmt.Println(strhalf)
	// }
}