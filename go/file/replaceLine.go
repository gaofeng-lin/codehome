

package main

import (
        "io/ioutil"
        "log"
        "strings"
)

func main() {
        input, err := ioutil.ReadFile("C:/Users/76585/Desktop/key.hypara")
        if err != nil {
                log.Fatalln(err)
        }

        lines := strings.Split(string(input), "\n")

        for i, line := range lines {
                if strings.Contains(line, "nsimutask") {
                    lines[i] = "int    nsimutask          =   0;"
                }
				if strings.Contains(line, "string parafilename") {
					lines[i] = "string parafilename       =   \"../bin/grid_para.hypara\";"
					break
				}
        }
        output := strings.Join(lines, "\n")
        err = ioutil.WriteFile("C:/Users/76585/Desktop/key.hypara", []byte(output), 0644)
        if err != nil {
                log.Fatalln(err)
        }
}