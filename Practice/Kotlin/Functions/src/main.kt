fun getGreeting():String{ // we define the return type
    return "Hello Kotlin"
}
//We can return null value as well in a function using ? as we used in variables

// To define a function in Kotlin we use fun keyword

fun sayHello():Unit{ // Here Unit in Kotlin means that function does not return anything
    println(getGreeting()) // We can either keep Unit or keep it empty to specify that function returns nothing
}

// Single expression function ->

fun getWeather():String="Summer" // This is a more simplified way of writing a function in Kotlin
// For single expression function we can use type inference for eg-
fun getDay()="Monday"

// Adding parameters in functions
fun sayHi(itemToGreet:String){
    val msg = "Hi $itemToGreet"
    println(msg)
}

fun greet(greeting:String, personToGreet:String)=println("$greeting $personToGreet")

fun main(){

    //println("Hello World!")
    //println(getGreeting())
    //sayHello()
    //println(getWeather())
    //println(getDay())
    sayHi("John")
    greet("Good Morning", "Michel")
}

