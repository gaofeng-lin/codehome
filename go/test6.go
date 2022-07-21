// map to json

package main



import (
    // "encoding/json"
    "fmt"


)


func main() {

    versionRelationMap := map[string]string{"mgCFLScale":"cflMGTimes", "CFLEnd":"cfl_end", "CFLVaryStep":"cfl_nstep"}

    for key, val := range versionRelationMap{
        if key == "mgCFLScale" {
            fmt.Println(val)
        }
    }

}