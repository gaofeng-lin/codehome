package main
// 这个程序的目的是为了建立老变量名和值的关系


  
import (
	"fmt"
	"encoding/json"
)
  
type Books struct {
    Title string
    Author string
    Subject string
    Book_id int
}
  
// func changeBook(book Books) string {   //把book对象传进来，返回的值是string类型的，也就是将被修改的值返回出来。
//     book.title = "book1_change"
//     return book.title
// }
  
func main() {
    var book1 Books
	// book1 :=Books{}
    book1.Title = "book3"
	book1.Subject ="math"
    book1.Author = "zuozhe"
    book1.Book_id = 1


	book2 :=&book1
	book2.Author="gaofeng1"

	// book3 :=*book2

	// fmt.Println(book3)
	// data, _ := json.MarshalIndent(book3, "", "   ")
		
	data, _ := json.Marshal(&(*book2))
 
	fmt.Println(string(data))

	old_map :=make(map[string]interface{})
	err :=json.Unmarshal([]byte(data),&old_map)
	if err != nil {
		fmt.Println("err=",err)
		
	}

	for key, val := range old_map {
		if(key=="Author"){
			fmt.Println(val)
		}
		// fmt.Println("key=",key)
		// fmt.Println("val=",val)
	}


}
