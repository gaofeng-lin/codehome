package main
import (
    "fmt"
    "reflect"
)
type Tags struct {
    ID   int `json:"id"`
    Name string `json:"name"`
}
func main() {
    var tag Tags
    tag.ID = 1
    tag.Name = "魏花花"
	tag1 :=&tag
    var typeInfo = reflect.TypeOf(*tag1)
    var valInfo = reflect.ValueOf(*tag1)
    num := typeInfo.NumField()
    for i := 0; i < num; i++ {
        key := typeInfo.Field(i).Name
        val := valInfo.Field(i).Interface()
        fmt.Println(i)
        // fmt.Printf("%T --- %v\n", key, key)
        // fmt.Printf("%T --- %v\n", val, val)
		fmt.Printf("%v --- %v\n", key, val)
    }
}