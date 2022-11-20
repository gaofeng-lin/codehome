package main

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
	input := &obs.PutFileInput{}
	input.Bucket = "fenglei-dev"
	input.Key = "test_obs/aether/PHengLEIv3d0/grid/m6_str.cgns"
	input.SourceFile = "C:/Users/76585/Desktop/grid/m6_str.cgns"
	output, err := obsClient.PutFile(input)

	if err == nil {
		   fmt.Printf("RequestId:%s\n", output.RequestId)
		   fmt.Printf("ETag:%s, StorageClass:%s\n", output.ETag, output.StorageClass)
	} else {
		   if obsError, ok := err.(obs.ObsError); ok {
				  fmt.Println(obsError.Code)
				  fmt.Println(obsError.Message)
		   } else {
				  fmt.Println(err)
		   }
	}
}
