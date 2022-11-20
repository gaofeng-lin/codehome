package main

import (
	"fmt"
	// "os"
	// "bufio"
	// "io/ioutil"

	obs "github.com/huaweicloud/huaweicloud-sdk-go-obs/obs"
)


func main() {

	var ak = "HORREKV8QTZTQAE00I1Q"
	var sk = "vOOLHCzeugIgfDCrdDtaoNI2ehw19hU9ex1HDFhO"
	var endpoint = "obs.cn-southwest-2.myhuaweicloud.com"
	// 创建ObsClient结构体
	var obsClient, err = obs.New(ak, sk, endpoint)

	if err == nil {
		input := &obs.PutFileInput{}
		input.Bucket = "phengcloud"
		input.Key = "test03/local (2).zip"
		input.SourceFile = "C:/Users/76585/Desktop/local (2).zip"
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
		// 关闭obsClient
		obsClient.Close()
	}


}
