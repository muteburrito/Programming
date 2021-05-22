//we can write comments by using '/**/' or '//', which are ignored while compiling the code

#include<iostream> //there is a file named iostrem as a header file. We are just including it, as it will help in the input output functions and applications

using namespace std; //another way to define the standard namespace

/*int is a integer */ int main(/*paranthesis is useful when we want to define something which is in the function, before the function begins*/) //this is our function named main which is already defined in the header file
{//every function is written between curly brackets
    /*cout is another function which is present in standard name space, so we write std ::*/std :: cout <</*less than sign is important before writing what to print*/ "Hello World";//every sentence or word must be present in between double quotes
    //we can write std before main function so to avoid it writing it evertime. 
    
    return 0;//this means successful termination of the program, which means if the above code runs return the value of main as 0, else give the error.
}
//Refer to the executable file for the result of this entire code