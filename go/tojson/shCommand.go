package main

import (
	"fmt"
	"os/exec"
)

func main() {
	str :=`gojson -input="test4.json" -pkg=hyparser -name=CFDParaSelfHYPara -o="test4.go"`
	command := exec.Command("sh", "-c", str)
	bytes, _ := command.Output()
	fmt.Println(string(bytes))
}