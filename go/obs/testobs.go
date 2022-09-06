package main

// 引入依赖包
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
	if err == nil {
		// 使用访问OBS
		input := &obs.CreateBucketInput{}
		input.Bucket = "test20220901"
		input.Location = "cn-southwest-2"
		input.ACL = obs.AclPrivate
		input.StorageClass = obs.StorageClassWarm
		input.AvailableZone = "3az"
		output, err := obsClient.CreateBucket(input)
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

		// 关闭obsClient
		obsClient.Close()
	}
}
