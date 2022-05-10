package main

import "fmt"

func checkPalindrome(num int) string {
	input_num := num
	var remainder int
	res := 0
	for num > 0 {
		remainder = num % 10
		res = (res * 10) + remainder
		num = num / 10
	}
	if input_num == res {
		return "Palindrome"
	} else {
		return "Not a Palindrome"
	}
}

func main() {
	var num int

	fmt.Println("Enter Number: ")
	fmt.Scan(&num)

	fmt.Print(checkPalindrome(num))
}
