package main

// 这次要尝试的是把文件拉下来，为后续工作做准备
import (
	"fmt"
	"os"
	"bufio"
	// "io/ioutil"

	obs "github.com/huaweicloud/huaweicloud-sdk-go-obs/obs"
)
func main() {

	// paramFile := [...]string{"cfd_para.hypara","cfd_para.hypara","cfd_para.hypara","cfd_para.hypara",
							// "cfd_para.hypara","cfd_para.hypara","cfd_para.hypara","cfd_para.hypara","cfd_para.hypara","cfd_para.hypara"}

	var ak = "PSP8YKUVXYTEWZ2A9IRP"
	var sk = "9WKsKkUuMj5l7VscttebvZ3AOdnuKK1aQsjxWS4B"
	var endpoint = "obs.cn-southwest-2.myhuaweicloud.com"
	// 创建ObsClient结构体
	var obsClient, err = obs.New(ak, sk, endpoint)
	if err == nil {
		// 使用访问OBS
		input := &obs.GetObjectInput{}
       input.Bucket = "fenglei-dev"
       input.Key = "test_obs/someone/PHengLEIv3d0/grid/m6_str.cgns"
       output, err := obsClient.GetObject(input)
       if err == nil {
              defer output.Body.Close()
              fmt.Printf("StorageClass:%s, ETag:%s, ContentType:%s, ContentLength:%d, LastModified:%s\n",
                     output.StorageClass, output.ETag, output.ContentType, output.ContentLength, output.LastModified)
              p := make([]byte, 1024)
              var readErr error
              var readCount int
              // 读取对象内容
			  filePath := "C:/m6_str.cgns"
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
                     readCount, readErr = output.Body.Read(p)
                     if readCount > 0 {
						str := string(p[:readCount])
						fmt.Println(str)
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
		// 关闭obsClient
		obsClient.Close()
	}
}
