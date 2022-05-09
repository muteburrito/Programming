package main

import "fmt"

func main() {

	var str1 string
	var str2 string

	fmt.Println("Enter 1st string: ")
	fmt.Scan(&str1)

	fmt.Println("Enter 2nd string: ")
	fmt.Scan(&str2)

	if str1 == str2 {
		fmt.Println("Strings are equal !")
	} else {
		fmt.Println("Strings are not equal !")
	}
}
