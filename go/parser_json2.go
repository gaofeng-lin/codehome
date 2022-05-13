package main

import (
	// "bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	// "reflect"
	"strconv"
)

func con_var_name (key string, old_ver int) string {
	var res string
	bytes,_:=ioutil.ReadFile("C:/Users/76585/Desktop/para_compare_ver2.json")

	m :=make(map[string]interface{})
	err := json.Unmarshal([]byte(bytes),&m)

	if err != nil {
		fmt.Println("err=",err)
		return ""
	}
	for _, value :=range m{
		// fmt.Println(reflect.TypeOf(value.([]interface{})[1].(map[string]interface{})["name"]))	
		if key==value.([]interface{})[0].(map[string]interface{})["name"]{
			res=key
			return res
		} 

		if key==value.([]interface{})[1].(map[string]interface{})["name"]{
			tmp :=value.([]interface{})[0].(map[string]interface{})["name"]
			res=tmp.(string)
			return res
		}
		// res :=key
	}

	return res
}

func main() {
	// var res string
	bytes,_:=ioutil.ReadFile("C:/Users/76585/Desktop/para_compare_ver2.json")

	m :=make(map[string]interface{})
	err := json.Unmarshal([]byte(bytes),&m)

	if err != nil {
		fmt.Println("err=",err)
		// return ""
	}
	for _, value :=range m{
		// fmt.Println(reflect.TypeOf(value.([]interface{})[1].(map[string]interface{})["name"]))	
		// fmt.Println(key,value)
		// str :=value.([]interface{})[0].(map[string]interface{})["version"]
		// i,_ := strconv.Atoi(str)
		// fmt.Println(reflect.TypeOf(value.([]interface{})[0]))
		if(len(value.([]interface{}))==3){
			fmt.Println("3 is exist")
		}

		ver :=value.([]interface{})[1].(map[string]interface{})["version"]
		val,_ :=strconv.Atoi(ver.(string))
		if(val > 5000){
			fmt.Println(val)
		}
	
	}
	
}