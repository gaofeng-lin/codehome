package main

//利用gorequest传输文件过去

import (

	// "encoding/json"
	"fmt"
	"io/ioutil"
	"github.com/parnurzeal/gorequest"

)


// type Product struct {
// 	Name string
// 	ProductId int64
// 	Number int
// 	Price float64
// 	IsOnSale bool
// }


func main()  {
	// var p Product
	// // p := Product{}
	// p.Name="apple"
	// p.ProductId=1
	// p.Number=100
	// p.Price=3.45
	// p.IsOnSale=false
	// data, _ := json.Marshal(&p)
	// fmt.Println(string(data))

	wsFileSendUrl := "http://121.37.93.92/api/ws/sendfile"
	content, err := ioutil.ReadFile("C:/Users/76585/Desktop/testfile.docx")
	if err != nil {
		// log.Fatal(err)
		fmt.Printf("读取文件出错：%v", err)
		return
	}
	request := gorequest.New()
	_, _, errs := request.Post(wsFileSendUrl).Type("multipart").SendFile(content).End()

	if errs != nil {
		fmt.Printf("发送出错：%v", err)
		return 
	}
	fmt.Println("成功")


}
