

val middle:String="Sunil" //These are called as Top-level variables

fun main(){
    // To define a read only variables we use val

    val name: String = "Chinmay"

    // To define a variable whose value can be changed we use var

    var surname:String="Kulkarni"

    println(surname)

    surname =  "Kapoor"

    println(surname)
    // Here these variables declared inside a function are called local variables

    println(name+ middle+ surname) // We can use variables which are defined outside the main function as well

    // In Kotlin we cannot have null type variables. If we want to have null we add a ?

    var greeting: String? = "Hello"

    println(greeting)

    greeting = null

    println(greeting)

    // Kotlin supports type inference, so we can omit the type declaration

    var addr = "44/124"

    println(addr)

    // Although NULL needs to be declared using a var data type

}

