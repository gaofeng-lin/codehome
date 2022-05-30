package main

import (
	"fmt"
	// "strings"
	// "io/ioutil"
	// "encoding/json"
	"reflect"
)

func main() {
	// var bytes, _ = ioutil.ReadFile("C:/Users/76585/Desktop/test/test.json")
	// var v interface{}
	// json.Unmarshal(bytes, &v)
	// data := v.(map[string]interface{})

	// fmt.Println(data)
	// fmt.Println(bytes)

	tmp := make(map[string]interface{})

	tmp["type"] = "object123"

	for k,v := range tmp {
		// value, _ :=v.(string)
		fmt.Println(reflect.ValueOf(k),reflect.ValueOf(v))
		// in.instance.Field(i).SetMapIndex(reflect.ValueOf(k),reflect.ValueOf(v))
	}

}