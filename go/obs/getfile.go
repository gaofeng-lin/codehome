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
	if err == nil {
		// 使用访问OBS
		input := &obs.ListObjectsInput{}
		input.Bucket = "fenglei-dev"
		// input.Key = "test_obs/userID2/PHengLEIv3d0/bin/"
		output, err := obsClient.ListObjects(input)
		if err == nil {
			   fmt.Printf("RequestId:%s\n", output.RequestId)
			   for index, val := range output.Contents {
					  fmt.Printf("Content[%d]-OwnerId:%s, ETag:%s, Key:%s, LastModified:%s, Size:%d\n",
							index, val.Owner.ID, val.ETag, val.Key, val.LastModified, val.Size)
			   }
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
