package main


// 从路径字符串提取需要的一部分
import (
	// "crypto/ecdsa"
	"fmt"
	// "bytes"
	// "encoding/json"
	"strings"

)

func main() {
	
	str := "/home/yskj/phopt/job/1/136/Ma0.73H0α2.79"
	dirSlice := strings.Split(str, "/")
	// res := strings.Split(str, "/")
	// fmt.Println(res[:len(res)-1])
	// fmt.Println(strings.Join(res[:len(res)-1],"/")) 

	res := strings.Join(dirSlice[:len(dirSlice)-1],"/")
	fmt.Println(res)
}