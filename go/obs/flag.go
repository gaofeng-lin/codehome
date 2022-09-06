package main

import (
	"flag"
	"fmt"
) 



func main() {
    dir := flag.String("b", "/home/default_dir", "backup path")
    mode := flag.Bool("d", false, "debug mode")
 
     flag.Parse()
 
     fmt.Println("dir: ", *dir)
     fmt.Println("mode: ", *mode)
 }