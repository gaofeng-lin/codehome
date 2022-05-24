package router
import (
"github.com/gin-gonic/gin"
"testgin/handler"
)
func InitRouter() *gin.Engine {

router := gin.Default()
router.POST("/api/test", handler.Test)
return router

}