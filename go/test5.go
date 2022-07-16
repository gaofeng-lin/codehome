package main

import (

	"encoding/json"
	"fmt"
)


type Product struct {
	Name string
	ProductId int64
	Number int
	Price float64
	IsOnSale bool
}


func main()  {
	var p Product
	// p := Product{}
	p.Name="apple"
	p.ProductId=1
	p.Number=100
	p.Price=3.45
	p.IsOnSale=false
	data, _ := json.Marshal(&p)
	fmt.Println(string(data))

}
