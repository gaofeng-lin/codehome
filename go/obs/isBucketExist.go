package main

// 引入依赖包
import (
	"fmt"

	obs "github.com/huaweicloud/huaweicloud-sdk-go-obs/obs"
)
func main() {
	var ak = "HORREKV8QTZTQAE00I1Q"
	var sk = "vOOLHCzeugIgfDCrdDtaoNI2ehw19hU9ex1HDFhO"
	var endpoint = "obs.cn-southwest-2.myhuaweicloud.com"
	// 创建ObsClient结构体
	var obsClient, err = obs.New(ak, sk, endpoint)
	if err == nil {
		// 使用访问OBS
		_, err := obsClient.HeadBucket("phengcloud123")
       if err == nil {
              fmt.Println("Bucket exists")
       } else {
              if obsError, ok := err.(obs.ObsError); ok {
                     if obsError.StatusCode == 404 {
                           fmt.Println("Bucket does not exists")
                     } else {
                           fmt.Printf("StatusCode:%d\n", obsError.StatusCode)
                     }
              } else {
                     fmt.Println(err)
              }
       }

		// 关闭obsClient
		obsClient.Close()
	}
}
