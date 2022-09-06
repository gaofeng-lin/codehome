package main

import (
	// pb "compute/protos"
)

type FileManager interface {
	
	Remove(uri string)  error                           // 移除目录或者文件
	Rename(srcUri, desUri string) error                 // 修改文件目录名或者给文件名改名
	MkDir(uri string) error                             // 新建文件夹
	GetPath(uri string) string                          // 获取绝对路径
	FindFileWithExt(dir, suffix string) (string, string, error) // 找到存在某个后缀的文件, 并返回全路径
	RemoveAllFileWithSuffix(dir, suffix string) error // 移除某个文件夹所有含suffix后缀的文件

}

// type SolverManager interface {
// 	NewFile(name string, uri string)
// 	Store(file *File,  uri string, req *pb.Chunk, id string)
	
// }