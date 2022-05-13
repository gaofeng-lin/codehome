package main

import (
	"fmt"
	// "io/ioutil"
	"strings"
	// "reflect"
)

func main() {
	s := "/home/yskj/phopt/work/2/47/Ma0.8395H0α3.06/bin/cfd_para_self.hypara"
	tmp :=strings.Split(s,"/")
	// tmp1 :=[]rune(tmp)
	fmt.Println(tmp)
	// fmt.Println(reflect.TypeOf(tmp))
	fmt.Println("/"+tmp[1]+"/"+tmp[2]+"/"+tmp[3]+"/"+tmp[4]+"/"+tmp[5]+"/"+tmp[6]+"/Default/bin/cfd_para_self.hypara")
	fmt.Println("/"+tmp[1]+"/"+tmp[2]+"/"+tmp[3]+"/"+tmp[4]+"/"+tmp[5]+"/"+tmp[6]+"/"+tmp[7]+"/"+tmp[8]+"/cfd_para.hypara")

	// i:=6
	// s1 :="/"
	// for i>0{
	// 	s2=
	// }
}