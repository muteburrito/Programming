package main

import "fmt"

func main() {
	var a int

	fmt.Println("Enter the number you want table of : ")
	fmt.Scan(&a)

	for b := 1; b <= 10; b++ {
		fmt.Println(a * b)
	}
}
