package handler
import (
"github.com/gin-gonic/gin"
"io/ioutil"
"net/http"
)
func Test(context *gin.Context) {

//获取请求body
msg, _ := ioutil.ReadAll(context.Request.Body)
str := string(msg)
context.JSON(http.StatusOK, gin.H{
	"message": str,
})

}