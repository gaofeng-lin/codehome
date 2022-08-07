package main

import (
    "fmt"
    "io/ioutil"
)

func main() {

    // 存储文件字符流的切片
    fileByte := make([][]byte, 0)

    // 从文件夹读取文件名并存入切片
    files, err2 := ioutil.ReadDir("C:/Users/76585/Desktop/test/")
    if err2 != nil {
        panic(err2)
    }

    fileName := make([]string, 0)


    for _, file := range files {
        fullStringName := ""  + file.Name()
        fileName = append(fileName, fullStringName)
        fullPath := "C:/Users/76585/Desktop/test/" + file.Name()

        // 读文件
        content, err := ioutil.ReadFile(fullPath)
        if err != nil {
            // log.Fatal(err)
            fmt.Printf("读取文件出错：%v", err)
        }

        // 写文件
        writePath := "C:/Users/76585/Desktop/test2/" + file.Name()
        err1 := ioutil.WriteFile(writePath,content,0766)

        if err1 != nil {
            fmt.Println("write fail")
        }

        // 文件字符流存入切片
        fileByte = append(fileByte,content)

    }
    fmt.Println(fileName)
    fmt.Println(fileByte[0])

    // 使用 io/ioutil.ReadFile 方法一次性将文件读取到内存中
    // filePath := "C:/Users/76585/Desktop/test/test.json"
    // content, err := ioutil.ReadFile(filePath)
    // if err != nil {
    //     // log.Fatal(err)
    //     fmt.Printf("读取文件出错：%v", err)
    // }
    // fmt.Printf("%v\n", content)
    // // fmt.Printf("%v\n", string(content))

    // err1 := ioutil.WriteFile("C:/Users/76585/Desktop/test/test123.json",content,0766)

    // if err1 != nil {
    //     fmt.Println("write fail")
    // }

    // fmt.Println("write success")

}