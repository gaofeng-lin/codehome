package main

import (
    "fmt"
    "io/ioutil"
)

func main() {
    // 使用 io/ioutil.ReadFile 方法一次性将文件读取到内存中
    filePath := "C:/Users/76585/Desktop/test/test.json"
    content, err := ioutil.ReadFile(filePath)
    if err != nil {
        // log.Fatal(err)
        fmt.Printf("读取文件出错：%v", err)
    }
    // fmt.Printf("%v\n", content)
    fmt.Printf("%v\n", string(content))
}