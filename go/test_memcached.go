package main

import (
   "fmt"
//    "time"
   "github.com/bradfitz/gomemcache/memcache"
)

var (
	server = "121.37.93.92:11211"
)

func main() {
	key := "xbmuscl"
	var res string
	mc := memcache.New(server)
    if mc == nil {
        fmt.Println("memcache New failed")
    }
    it, _ := mc.Get(key)
	if it == nil{
		res = key
	} else {
		res = string(it.Value)
	}
    // if string(it.Key) == key {
    //     // fmt.Println("value is ", string(it.Value))
	// 	res = string(it.Value)
    // } else {
    //     fmt.Println("Get failed")
	// 	res = key
    // }

	fmt.Println("res is :", res)
}