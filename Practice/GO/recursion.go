package main

import "fmt"

func fact(i int) int {
	if i <= 1 {
		return 1
	}
	return i * fact(i-1)
}

func main() {
	num := 0
	fmt.Print("Enter a number you want factorial of: ")
	fmt.Scan(&num)
	fmt.Print(fact(num))
}
