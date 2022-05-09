package main

import "fmt"

func main() {
	var a int
	var b int

	fmt.Println("Enter two numbers fo a swap: ")
	fmt.Scan(&a, &b)

	a = a * b
	b = a / b
	a = a / b

	fmt.Print("Swapped numbers are ", a, " and ", b)
}
