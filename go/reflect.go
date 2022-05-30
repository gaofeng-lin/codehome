package main

import (
	"fmt"
	"reflect"
)


func main() {
	var f float64 = 3.1415
	v := reflect.ValueOf(f)   // f 隐式地被转成了interface{}
	y := v.Interface().(float64) // y的类型是float64

	fmt.Println(v)
	fmt.Println(y)
}