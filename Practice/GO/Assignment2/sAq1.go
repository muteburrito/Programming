package main

import "fmt"

func sum(num1, num2 int) int {
	return num1 + num2
}

func main() {

	var a int
	var b int

	fmt.Println("Enter 2 numbers: ")
	fmt.Scan(&a, &b)

	fmt.Println("Sum is ", sum(a, b))
}
