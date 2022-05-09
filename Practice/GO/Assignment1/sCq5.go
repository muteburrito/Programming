package main

import (
	"fmt"
	"strings"
)

func main() {
	var a string
	var b string

	fmt.Println("Enter string 1 and string 2:")
	fmt.Scan(&a, &b)

	if strings.Contains(a, b) {
		fmt.Println(a + " is substring of " + b)
	} else if strings.Contains(b, a) {
		fmt.Println(b + " is substring of " + a)
	} else {
		fmt.Println("No substring present")
	}
}
