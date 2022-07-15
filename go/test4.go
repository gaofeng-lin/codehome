package main

import (
	// "crypto/ecdsa"
	"fmt"
	// "reflect"
	"strings"
	"strconv"
)

func main() {
	//第一种方法
	// s := make(map[interface{}]interface{})
	// s["a"] = "a"
	// s["b"] = "b"
	// s[1] = 1
	
	// b := make(map[interface{}]interface{})
	// b["a"] = "ba"
	// b["e"] = 45
	// b[1] = "str"
	// b[2] = 2
	// b["s"] = s
	// fmt.Println(b)
	// fmt.Println(b["s"].(map[interface{}]interface{})[1])
	// tmp_map := make(map[string]interface{})
	// tmp_slice := make([]interface{}, 0)
	// tmp_slice = append(tmp_slice,1,2,3)
	// tmp_map["enum"] = tmp_slice
	// tmp_map["type"] = "string"

	// res_map := make(map[string]interface{})
	// res_map["参数1"] = tmp_map
	// res_map["参数2"] ="number"
	// res_map["参数3"] = "number"
	// // fmt.Println(res_map)

	// for _, val := range res_map {
	// 	// fmt.Println(key)
	// 	if reflect.TypeOf(val).Kind() == reflect.Map {
	// 		// fmt.Printf("%v is a map\n",val)
	// 		for nk, nv := range val.(map[string] interface {}) {
	// 			fmt.Println(nk)
	// 			fmt.Println(nv)
	// 		}
	// 	}
	// 	// fmt.Println(reflect.TypeOf(val))
	// }

	tmp_slice := make([]interface{}, 0)
	// tmp_slice2 := make([]interface{}, 0)
	// str :=strings.Replace("12;34;56",";",",",-1)
	str := strings.Split("12;34;56",";")
	// finres,_ := strconv.Atoi(str) 
	// tmp_slice = append(tmp_slice,str)
	// // fmt.Println(tmp_slice)
	// for e := range tmp_slice {
	// 	res := tmp_slice[e].(string)
	// 	fmt.Println(res)
	// }

	for e := range str {
		a ,_:= strconv.Atoi(str[e])
		fmt.Println(a)
		tmp_slice = append(tmp_slice,a)
		tmp_slice = append(tmp_slice,",")
	}
	fmt.Println(tmp_slice[:len(tmp_slice)-1])
	
}