package main

import (
	"os"
)


func main() {
	type LocalStorage struct{
		root string  // 项目管理的根环境
   }
   var _ FileManager = new(LocalStorage)
}

func NewLocalStorage(root string) *LocalStorage {
	if root == ""{
		// 默认当前目录
		root, _ = os.Getwd()
	}
	return &LocalStorage{
		root: root,
	}
}