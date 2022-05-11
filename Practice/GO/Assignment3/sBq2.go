package main

import "fmt"

func main() {
	var arr [5]int
	var min int = 0
	var temp int = 0

	fmt.Printf("Enter numbers in array: \n")
	for i := 0; i <= 4; i++ {
		fmt.Printf("Numbers: arr[%d]: ", i)
		fmt.Scanf("%d", &arr[i])
	}

	for i := 0; i <= 4; i++ {
		min = i
		for j := i + 1; j <= 4; j++ {
			if arr[j] < arr[min] {
				min = j
			}
		}
		temp = arr[i]
		arr[i] = arr[min]
		arr[min] = temp
	}

	fmt.Printf("Array after sorting: \n")
	for i := 0; i <= 4; i++ {
		fmt.Printf("%d ", arr[i])
	}
}
