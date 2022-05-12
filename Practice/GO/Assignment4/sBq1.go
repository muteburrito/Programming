package main

import "fmt"

type student struct {
	name      string
	branch    string
	particles int
}

func (a *student) show(abranch string) {
	(*a).branch = abranch
}

func main() {

	res := student{
		name:   "Sona",
		branch: "CSE",
	}

	fmt.Println("student's name: ", res.name)
	fmt.Println("Branch Name(Before): ", res.branch)

	p := &res

	p.show("ECE")
	fmt.Println("student's name: ", res.name)
	fmt.Println("Branch Name(After): ", res.branch)
}
