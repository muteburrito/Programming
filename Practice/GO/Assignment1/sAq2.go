package main

import "fmt"

func main() {
	var a int

	fmt.Println("Enter a number")
	fmt.Scan(&a)
	if a%2 == 0 {
		fmt.Println("Number is even")
	} else {
		fmt.Println("Number is odd")
	}

}
