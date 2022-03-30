fun sayHello(greeting:String, itemToGreet:String)=println("$greeting $itemToGreet")

fun main(){

    val interestingThings = arrayOf("Kotlin", "C#", "Java")
    println(interestingThings.size)
    println(interestingThings[0])
    println(interestingThings.get(0))

    // Conventional way of looping items
    for(Thing in interestingThings){
        println(Thing)
    }

    // Lambda syntax in kotlin
    interestingThings.forEach { items -> //By default, it is the keyword used for referencing the elements in an array
        println(items)
    }


    interestingThings.forEachIndexed { index, items ->
        println("$items is at index $index")
    }

    val items = listOf("Programming", "Gaming", "Chill")

    items.size
    println(items[1])
    // for list as well we can use a period and use different methods available
}