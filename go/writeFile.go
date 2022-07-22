package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    valueMap := map[string]interface{}{"参数1.1":"123","参数1.2":"nnd"}
    nameMap := map[string]interface{}{"参数1.1":[]string{"param1.1","int"},"参数1.2":[]string{"param1.2","string"}}
    filePath := "c:/a.txt" // 此文件事先不存在
    file, err := os.OpenFile(filePath, os.O_WRONLY | os.O_APPEND, 0766) // O_CREATE 能创建文件
    if err != nil {
        fmt.Printf("打开文件出错：%v", err)
        return
    }
    defer file.Close()
    writer := bufio.NewWriter(file)
    for key, val := range nameMap {
        varType := val.([]string)[1]
        varName := val.([]string)[0]
        varValue := valueMap[key].(string)
        fmt.Println(val.([]string)[1])
        fmt.Println(val.([]string)[0])
        fmt.Println(valueMap[key])
        var str string
        if varType == "string" {
            str = varType + "\t" + varName + "\t" + "= \t" + "\""+ varValue + "\""+"; \n"
        } else {
            str = varType + "\t" + varName + "\t" + "= \t" + varValue + "; \n"
        }
        
        
        _, err := writer.WriteString(str) // func (b *Writer) WriteString(s string) (int, error)
        if err != nil {
            fmt.Printf("文件写入出错：%s", err)
        }
    }

    // 因为 writer 是带缓存的，所以需要 Flush 方法将缓冲中的数据真正写入到文件中
    _ = writer.Flush()
}
