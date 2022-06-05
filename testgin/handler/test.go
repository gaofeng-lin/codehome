package handler
import (
"github.com/gin-gonic/gin"
"io/ioutil"
"net/http"
"fmt"
// "encoding/json"
)
func Test(context *gin.Context) {

//获取请求body
msg, _ := ioutil.ReadAll(context.Request.Body)
str := string(msg)

fmt.Println(str)



context.Header("Access-Control-Allow-Origin", "*")
context.Header("Access-Control-Allow-Headers", "*")
context.Header("Access-Control-Allow-Methods", "POST, GET, PUT, PATCH, OPTIONS")
context.Header("Access-Control-Allow-Credentials", "true")
context.Header("Access-Control-Expose-Headers", "*")
context.JSON(http.StatusOK, gin.H{
	"message": str,
})

}