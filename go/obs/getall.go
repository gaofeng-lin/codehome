package main

import (
	"fmt"
	"os"
	"bufio"
	// "io/ioutil"
	"strings"

	obs "github.com/huaweicloud/huaweicloud-sdk-go-obs/obs"
)

func main() {
	solverName := "PHengLEIv3d0.exe"
	// paramFile := [...]string{"cfd_para.hypara","cfd_para.hypara","cfd_para.hypara","cfd_para.hypara",
							// "cfd_para.hypara","cfd_para.hypara","cfd_para.hypara","cfd_para.hypara","cfd_para.hypara","cfd_para.hypara"}

	var ak = "PSP8YKUVXYTEWZ2A9IRP"
	var sk = "9WKsKkUuMj5l7VscttebvZ3AOdnuKK1aQsjxWS4B"
	var endpoint = "obs.cn-southwest-2.myhuaweicloud.com"
	// 创建ObsClient结构体
	var obsClient, err = obs.New(ak, sk, endpoint)
	if err == nil {
		// 使用访问OBS

		// 获取对象
		getObject := &obs.ListObjectsInput{}
		getObject.Bucket = "fenglei-dev"
		output, err := obsClient.ListObjects(getObject)
		if err == nil {
			//    fmt.Printf("RequestId:%s\n", output.RequestId)
			   for _, val := range output.Contents {

					// fmt.Printf("Content[%d]-OwnerId:%s, ETag:%s, Key:%s, LastModified:%s, Size:%d\n",
					// 		index, val.Owner.ID, val.ETag, val.Key, val.LastModified, val.Size)
					// 下载文件
					if strings.Contains(val.Key, "test_obs/default/PHengLEIv3d0.exe") {
						fmt.Println("包含子串test_obs/default/")
						fmt.Printf("%s\n", val.Key)
						downloadObject := &obs.GetObjectInput{}
						downloadObject.Bucket = "fenglei-dev"
						downloadObject.Key = val.Key
						downloadOutput, err := obsClient.GetObject(downloadObject)
						if err == nil {
							defer downloadOutput.Body.Close()
							p := make([]byte, 1024)
							var readErr error
							var readCount int
							// 读取对象内容
							filePath := "C:/" + solverName
							file, err := os.Create(filePath)
							if err != nil {
								fmt.Println(err)
							}
							defer file.Close()
							file1, err := os.OpenFile(filePath,  os.O_RDWR |os.O_APPEND, 0666)
							if err != nil {
								fmt.Printf("打开文件出错：%v", err)
								return
							}
							defer file1.Close()
							writer := bufio.NewWriter(file1)
							for {
								   readCount, readErr = downloadOutput.Body.Read(p)
								   if readCount > 0 {
									  str := string(p[:readCount])
									  _, err := writer.WriteString(str)
									  if err != nil {
										  fmt.Printf("文件写入出错：%s", err)
									  }
			  
								   }
								   if readErr != nil {
										 break
								   }
			  
							}
						  _ = writer.Flush()
					 } else if obsError, ok := err.(obs.ObsError); ok {
							fmt.Printf("Code:%s\n", obsError.Code)
							fmt.Printf("Message:%s\n", obsError.Message)
					 }
					}
					// downloadObject := &obs.GetObjectInput{}
					// downloadObject.Bucket = "fenglei-dev"
					// downloadObject.Key = 
				}
		} else {
			   if obsError, ok := err.(obs.ObsError); ok {
					  fmt.Println(obsError.Code)
					  fmt.Println(obsError.Message)
			   } else {
					  fmt.Println(err)
			   }
		}

		obsClient.Close()
	}
}
