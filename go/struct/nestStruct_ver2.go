package main


import (
        "fmt"
        "reflect"
		// "errors"
)

// type Orange struct {
//         Size int
// }

type Response struct {
	Type       string              	  `json:"type"`
	Properties map[string]interface{} `json:"properties"`
}

func (in *Response) SetSpecialStruct(value map[string]interface{}) {
	tmp := reflect.ValueOf(in)
	tmp.Elem().FieldByName("Properties").Set(reflect.ValueOf(value))
}

func main() {

    a := Response{}
    v := reflect.ValueOf(&a)
    // fmt.Println("v:", v)
    // fmt.Println("v Type:", v.Type())
    // fmt.Println("v CanSet:", v.CanSet())
    // v = reflect.ValueOf(&a)
    // fmt.Println("v:", v)
    // fmt.Println("v Type:", v.Type())
    // fmt.Println("v CanSet:", v.CanSet())
    //element
    v = v.Elem()
    size := v.FieldByName("Type")
    // fmt.Println("size CanSet:", size.CanSet())
    size.SetString("object")
    // fmt.Println("after set:", v)
	// fmt.Println(a)
	// --------------------------------------------
	// --------------------------------------------


	tmp := make(map[string]interface{})
	tmp["type"] = "string"

	tmp2 := make(map[string]interface{})
	tmp2["湍流模型"] = tmp

	tmp3 := make(map[string]interface{})
	tmp3["type"] = "int"

	tmp4 := make(map[string]interface{})
	tmp4["最大迭代步数"] = tmp3

	tmp4["湍流模型"] = tmp


	// tmp1 := make(map[string]Instance)
	

	// setprpo := v.FieldByName("Properties")
	// setprpo.SetSpecialStruct(p)
	// a.SetSpecialStruct(tmp2)
	// fmt.Println(a)
	a.SetSpecialStruct(tmp4)

	fmt.Println(a)



}
