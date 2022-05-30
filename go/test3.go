package main

import (
	"fmt"
	// "strings"
	"io/ioutil"
	// "encoding/json"
)

func main() {
	var bytes, _ = ioutil.ReadFile("C:/Users/76585/Desktop/test/test.json")
	// var v interface{}
	// json.Unmarshal(bytes, &v)
	// data := v.(map[string]interface{})

	// fmt.Println(data)
	fmt.Println(bytes)

}