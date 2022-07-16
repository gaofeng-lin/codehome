package main

import (
	// "crypto/ecdsa"
	"fmt"
	// "reflect"
	// "strings"
	// "strconv"
	"sort"
	"reflect"
)
/* 在slice中去除重复的元素，其中a必须是已经排序的序列。
 * params:
 *   a: slice对象，如[]string, []int, []float64, ...
 * return:
 *   []interface{}: 已经去除重复元素的新的slice对象
 */
 func SliceRemoveDuplicate(a interface{}) (ret []interface{}) {
	if reflect.TypeOf(a).Kind() != reflect.Slice {
		fmt.Printf("<SliceRemoveDuplicate> <a> is not slice but %T\n", a)
		return ret
	}
 
	va := reflect.ValueOf(a)
	for i := 0; i < va.Len(); i++ {
		if i > 0 && reflect.DeepEqual(va.Index(i-1).Interface(), va.Index(i).Interface()) {
			continue
		}
		ret = append(ret, va.Index(i).Interface())
	}
 
	return ret
}
func main() {
	

		slice_string := []string{"模块1","模块3","模块2","模块2","模块3"}

	 
		sort.Strings(slice_string)

	 
		fmt.Printf("slice_string = %v, %p\n", slice_string, slice_string)

	 
		ret_slice_string := SliceRemoveDuplicate(slice_string)
	
	 
		fmt.Printf("ret_slice_string = %v, %p\n", ret_slice_string, ret_slice_string)

	



	

	
}