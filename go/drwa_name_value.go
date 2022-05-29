package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"strings"

	// "strings"

	// "ioutil"
	"os"
	// "strings"
	"io"
	"regexp"
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
		value := strings.Split(reg.FindAllString(str,-1)[0], ";")
		res_map[reg.FindAllString(str,-1)[1]] = value[0]
	
		}
	return res_map

}

func main() {
	map_newvalue_type :=DrawValueNameFromPareSelfFile("C:\\Users\\76585\\Desktop\\cfd_para_self.txt")

	for key,val := range map_newvalue_type{
		fmt.Println(key,val)
	}

	marshal, _ := json.MarshalIndent(map_newvalue_type, "", " ")

	fmt.Println(string(marshal))

}