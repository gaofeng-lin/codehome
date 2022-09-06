package main

// 这次要尝试的是把文件拉下来，为后续工作做准备
import (
	"fmt"

	obs "github.com/huaweicloud/huaweicloud-sdk-go-obs/obs"
)


func main() {
	var ak = "PSP8YKUVXYTEWZ2A9IRP"
	var sk = "9WKsKkUuMj5l7VscttebvZ3AOdnuKK1aQsjxWS4B"
	var endpoint = "obs.cn-southwest-2.myhuaweicloud.com"
	// 创建ObsClient结构体
	var obsClient, err = obs.New(ak, sk, endpoint)
	input := &obs.DeleteObjectInput{}
	input.Bucket = "fenglei-dev"
	input.Key = "test_obs/userID2/PHengLEIv3d0/grid/m6_str_0.bcmesh"
	output, err := obsClient.DeleteObject(input)
	if err == nil {
		   fmt.Printf("RequestId:%s\n", output.RequestId)
	} else {
		   if obsError, ok := err.(obs.ObsError); ok {
				  fmt.Println(obsError.Code)
				  fmt.Println(obsError.Message)
		   } else {
				  fmt.Println(err)
		   }
	}
}
