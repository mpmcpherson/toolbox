package greetings

import "fmt"
//import "rsc.io/quote"


func main() {
	fmt.Println(Hello("Michael"))
}

func Hello(name string) string {
	message := fmt.Sprintf("Hi, %v. Welcome!", name)
	return message
}