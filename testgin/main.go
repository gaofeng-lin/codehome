package main
import "testgin/router"
import "testgin/cors"

func main(){

//初始化go-gin，启动webserver
r := router.InitRouter()
r.Use(cors.Cors())
_ = r.Run(":8100")
}