package main


import (
	"bytes"
	"encoding/json"
	// "fmt"
	// "io/ioutil"
	"net/http"
)

type User struct {
	Name string  	`json:"name"`
	Job string 	    `json:"job"`
}

func main() {
	user := User{
		Name: "Test User",
		Job: "Go lang Developer",
	}

	//Convert User to byte using Json.Marshal
	//Ignoring error. 
	body, _ := json.Marshal(user)

	//Pass new buffer for request with URL to post.
  //This will make a post request and will share the JSON data
	_, err := http.Post("http://127.0.0.1:8100/api/test", "application/json", bytes.NewBuffer(body) )

	// An error is returned if something goes wrong
	if err != nil {
		panic(err)
	}

}