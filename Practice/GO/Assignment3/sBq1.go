package main

import "fmt"

func main() {

	s1 := [][]int{
		{1, 2},
		{3, 4},
		{5, 6},
		{7, 8},
	}

	fmt.Println("Slice 1 : ", s1)

	s2 := [][]string{
		[]string{"str1", "str2"},
		[]string{"str3", "str4"},
		[]string{"str5", "str6"},
	}

	fmt.Println("Slice 2 : ", s2)

	fmt.Println("MultiDimensional Slice s2:")
	for i := 0; i < len(s2); i++ {
		fmt.Println(s2[i])
	}

	fmt.Println("Slice s2 Like Matrix:")

	n := len(s2)

	m := len(s2[0])
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Print(s2[i][j] + " ")
		}
		fmt.Print("\n")
	}
}
