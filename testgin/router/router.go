package router
import (
"github.com/gin-gonic/gin"
"testgin/handler"

)

// func CorsHandler() gin.HandlerFunc {
// 	return func(c *gin.Context) {
// 		c.Header("Access-Control-Allow-Origin", "*")
// 		c.Header("Access-Control-Allow-Headers", "*")
// 		c.Header("Access-Control-Allow-Methods", "POST, GET, PUT, PATCH, OPTIONS")
// 		c.Header("Access-Control-Allow-Credentials", "true")
// 		c.Header("Access-Control-Expose-Headers", "*")
// 		if c.Request.Method == "OPTIONS" {
// 			c.JSON(http.StatusOK, "")
// 			c.Abort()
// 			return
// 		}
// 		c.Next()
// 	}

// }


func InitRouter() *gin.Engine {

router := gin.Default()
router.POST("/api/test", handler.Test)
return router

}