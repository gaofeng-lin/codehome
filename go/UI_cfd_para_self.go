package main

import (
	"fmt"
	// "io/ioutil"
)

func special_handle() map[string]string{
	special_had :=make(map[string]string)

	special_had["a"]="a2"
	special_had["b"]="b1"

	return special_had

}

func main() {
	var special_had map[string]string
	// special_had=make(map[string]string)
	special_had =special_handle()

	fmt.Printf(special_had["b"])
}