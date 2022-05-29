package main

import (
    "fmt"
    "io/ioutil"
	"bytes"
)

func ok(data interface{}) {
	fmt.Printf(data.(string))
}

func TransHtmlJson(data []byte) []byte {
	data = bytes.Replace(data, []byte("\\u0026"), []byte("&"), -1)
	data = bytes.Replace(data, []byte("\\u003c"), []byte("<"), -1)
	data = bytes.Replace(data, []byte("\\u003e"), []byte(">"), -1)
	return data
}

func main() {
    // 使用 io/ioutil.ReadFile 方法一次性将文件读取到内存中
    filePath := "C:/Users/76585/Desktop/test/test.json"
    content, err := ioutil.ReadFile(filePath)
    if err != nil {
        // log.Fatal(err)
        fmt.Printf("读取文件出错：%v", err)
    }
    fmt.Printf("%v\n", content)

	res := TransHtmlJson(content)

	fmt.Printf("%v\n", string(res))
    // fmt.Printf("%v\n", string(content))
	// ok(string(content))
}