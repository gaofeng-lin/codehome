package main

// json文件为空额外处理

import(
	"fmt"
	"io/ioutil"
	"encoding/json"
)

func test() string{
	bytes,_:=ioutil.ReadFile("/home/yskj/lgf/para_compare_ver2.json")
	m :=make(map[string]interface{})
	err := json.Unmarshal([]byte(bytes),&m)

	if err != nil {
		fmt.Println("err=",err)
		return ""
	}

	return "ok"
}


func main() {
	// bytes,_:=ioutil.ReadFile("/home/yskj/lgf/para_compare_ver2.json")
	// m :=make(map[string]interface{})
	// err := json.Unmarshal([]byte(bytes),&m)

	// if err != nil {
	// 	fmt.Println("err=",err)

	// }
	// fmt.Println(m)

	flag :=test()

	if flag == ""{
		fmt.Println("出错了")
	}else{
		fmt.Println("出错了")
	}
}