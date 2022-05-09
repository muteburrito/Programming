package main

import "fmt"

func main() {

	var number int

	fmt.Println("Enter Number: ")
	fmt.Scan(&number)

	if number <= 9 && number >= 0 {
		fmt.Println("Number is single digit")
	} else if number < 0 && number >= -9 {
		fmt.Println("Number is single digit")
	} else {
		fmt.Println("Number is double digit")
	}
}
