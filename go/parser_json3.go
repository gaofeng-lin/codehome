package main

// 读取后端cfd_para_self.hypara。此时是新变量，要将它转换为老变量

import (
	// "bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	// "reflect"
	"strconv"
)

func con_old_name (key string, old_ver int) string {
	var res string
	bytes,_:=ioutil.ReadFile("C:/Users/76585/Desktop/para_compare_ver2.json")

	m :=make(map[string]interface{})
	err := json.Unmarshal([]byte(bytes),&m)

	if err != nil {
		fmt.Println("err=",err)
		return ""
	}
	for _, value :=range m{

		if(len(value.([]interface{}))==2){

			if key==value.([]interface{})[0].(map[string]interface{})["name"]{
				res=key
				return res
			} 
			if key==value.([]interface{})[1].(map[string]interface{})["name"]{

				ver1 :=value.([]interface{})[0].(map[string]interface{})["version"]
				val1,_ :=strconv.Atoi(ver1.(string))

				ver2 :=value.([]interface{})[1].(map[string]interface{})["version"]
				val2,_ :=strconv.Atoi(ver2.(string))

				if(old_ver>=val1)&&(old_ver<val2){
					res = (value.([]interface{})[0].(map[string]interface{})["name"]).(string)
					return res			
				}else{
					return (value.([]interface{})[1].(map[string]interface{})["name"]).(string)
				}
			}
		}

		if(len(value.([]interface{}))==3){

			if key==value.([]interface{})[0].(map[string]interface{})["name"]{
				res=key
				return res
			} 
			if key==value.([]interface{})[1].(map[string]interface{})["name"]{

				ver1 :=value.([]interface{})[0].(map[string]interface{})["version"]
				val1,_ :=strconv.Atoi(ver1.(string))

				ver2 :=value.([]interface{})[1].(map[string]interface{})["version"]
				val2,_ :=strconv.Atoi(ver2.(string))

				if(old_ver>=val1)&&(old_ver<val2){
					res = (value.([]interface{})[0].(map[string]interface{})["name"]).(string)
					return res			
				}else{
					return (value.([]interface{})[1].(map[string]interface{})["name"]).(string)
				}
			}
			if key==value.([]interface{})[2].(map[string]interface{})["name"]{

				ver1 :=value.([]interface{})[0].(map[string]interface{})["version"]
				val1,_ :=strconv.Atoi(ver1.(string))

				ver2 :=value.([]interface{})[1].(map[string]interface{})["version"]
				val2,_ :=strconv.Atoi(ver2.(string))

				ver3 :=value.([]interface{})[2].(map[string]interface{})["version"]
				val3,_ :=strconv.Atoi(ver3.(string))

				if(old_ver>=val1)&&(old_ver<val2){
					res = (value.([]interface{})[0].(map[string]interface{})["name"]).(string)
					return res			
				}else if ((old_ver>=val2)&&(old_ver<val3)){
					return (value.([]interface{})[1].(map[string]interface{})["name"]).(string)
				}else{
					return (value.([]interface{})[2].(map[string]interface{})["name"]).(string)
				}
			}
		}
		
	}	
	return key
}

func main() {
	
	var res string
	var key ="TorqueRefX"
	res=con_old_name(key,5720)
	fmt.Println(res)
}