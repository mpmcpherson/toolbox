package main

import (
	"fmt"
	"example.com/greetings"
)

func main() {
	fmt.Println(Hello("Michael"))
	message := greetings.Hello("Michael")
}
