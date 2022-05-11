package main

import "fmt"

func main() {
	var lgsmsize, i int

	fmt.Print("Enter the Array Size to find Smallest & Largest = ")
	fmt.Scan(&lgsmsize)

	lgsmArr := make([]int, lgsmsize)

	fmt.Print("Enter the Array Items  = ")
	for i = 0; i < lgsmsize; i++ {
		fmt.Scan(&lgsmArr[i])
	}
	largest := lgsmArr[0]
	smallest := lgsmArr[0]

	for i = 0; i < lgsmsize; i++ {
		if largest < lgsmArr[i] {
			largest = lgsmArr[i]
		}
		if smallest > lgsmArr[i] {
			smallest = lgsmArr[i]
		}
	}

	fmt.Println("\nThe Largest Number in this lgsmArr    = ", largest)
	fmt.Println("\nThe Smallest Number in this lgsmArr    = ", smallest)
}
