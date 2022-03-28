
var greeting: String ?= "Hello"
var name="Chinmay"
fun main(){
// Here if we dont set the property/data type of the variable greeting we cannot change it to null
    greeting = null
    if (greeting != null){
        println(greeting)
    }
    println(name)


    // here using when control block is same as switch case in Java/C
    when(greeting){
        null -> println("Hi")
        else -> println(greeting)
    }

    val greetingToPrint = if(greeting != null) greeting else "Hi"
    println(greetingToPrint)
}