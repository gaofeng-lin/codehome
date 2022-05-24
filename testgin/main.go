package main
import "testgin/router"
func main(){

//初始化go-gin，启动webserver
r := router.InitRouter()
_ = r.Run(":8000")
}