package tojson

import (
	"bufio"
	"fmt"
	"strings"

	// "strings"

	// "ioutil"
	"os"
	// "strings"
	"io"
	"regexp"
	"encoding/json"
	"log"
	// "bytes"
	// "StringEscapeUtils"



)

func DrawValueNameFromPareSelfFile(file_path string) map[string]string {
	
	res_map := make(map[string]string)
	fd,_ :=os.Open(file_path)
	defer fd.Close()
	buff :=bufio.NewReader(fd)
	
	for{
		data,_,eof := buff.ReadLine()
		if eof ==io.EOF {
			break
		}
		str :=string(data)
		// fmt.Println(strings.TrimSpace(str))
		reg := regexp.MustCompile(`[\S]+`)
		// reg1 := regexp.MustCompile(`[]+`)
		if (strings.Contains(str,"#")){
			continue
		}

		if(len(str)==0){
			break
		}
		value := strings.Split(reg.FindAllString(str,-1)[3], ";")
		res_map[reg.FindAllString(str,-1)[1]] = value[0]
	
		}
	return res_map

}

func writeLog(msg string) {

	fileName := "C:/Tools/codehome/go/tojson/test4.json"
	fileHandle, err := os.OpenFile(fileName, os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
	if err != nil {
		log.Println("open file error :", err)
		return
	}
	defer fileHandle.Close()
	// NewWriter 默认缓冲区大小是 4096
	// 需要使用自定义缓冲区的writer 使用 NewWriterSize()方法
	buf := bufio.NewWriterSize(fileHandle, len(msg))

	buf.WriteString(msg)

	err = buf.Flush()
	if err != nil {
		log.Println("flush error :", err)
	}
}

// 去除json中的转义字符
// func disableEscapeHtml(data interface{}) (string, error) {
// 	bf := bytes.NewBuffer([]byte{})
// 	jsonEncoder := json.NewEncoder(bf)
// 	jsonEncoder.SetEscapeHTML(false)
// 	if err := jsonEncoder.Encode(data); err != nil {
// 		return "", err
// 	}
// 	return bf.String(), nil
// }

func main() {
	map_newvalue_type :=DrawValueNameFromPareSelfFile("C:\\Users\\76585\\Desktop\\cfd_para_self.txt")

	// for key,val := range map_newvalue_type{
	// 	fmt.Println(key,val)
	// }

 
    //编码成json
    // result, err := json.Marshal(map_newvalue_type)
    //result =  {"address":"北京","languages":["Golang","PHP","Java","Python"],"price":666.666,"status":true}
	// raw :=json.RawMessage()
    result, err := json.MarshalIndent(map_newvalue_type, "", "    ")
    if err != nil {
        fmt.Println("err = ", err)
        return
    }

	// res, _:= disableEscapeHtml(result)
	// data :=json.RawMessage(string(result)) 
	// result.SetEscapeHTML(false)
	
	
	// 去除json中的转义字符

	// bf := bytes.NewBuffer([]byte{})
	// jsonEncoder := json.NewEncoder(bf)
	// jsonEncoder.SetEscapeHTML(false)
	// if err := jsonEncoder.Encode(string(result))
	// err != nil {
	// 	fmt.Println(err)
	// }
	// return bf.String(), nil



    fmt.Println("result = ", string(result))
	// fmt.Println(bf.String())
	writeLog(string(result))
}


