package main

import (
	// "crypto/ecdsa"
	"fmt"
	"bytes"
	"encoding/json"

)
/* 在slice中去除重复的元素，其中a必须是已经排序的序列。
 * params:
 *   a: slice对象，如[]string, []int, []float64, ...
 * return:
 *   []interface{}: 已经去除重复元素的新的slice对象
 */
 type reqCancel struct {
	JobID *int64 `json:"job_id" binding:"required,gte=1" example:"15"`
}

func main() {
	
	x := int64(100)

	req := reqCancel{
		JobID: &x,
	}
	requestBody := new(bytes.Buffer)
	json.NewEncoder(requestBody).Encode(req)

	fmt.Println(requestBody)


		
	// x1 := "int"
	// x2 := "param1.1"
	// x3 := "="
	// x4 := 55.66
	// x5 := ";"

	// str := fmt.Sprintf("%s %s %s %v%s \n", x1, x2, x3, x4, x5)

	// fmt.Println(str)


	

	
}