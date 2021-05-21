#include<iostream>

using namespace std;

void funct1()
{
    int a = 65; // Here even though we eclare a variable a = 65 still while considering in main function the variable value inside that function will be considered
    cout << "The value of a in func1 is:" <<a;
}
int main()
{
    int a = 6; //Here int means integer whose name is a which has value 6
    char b = 'd'; //Here char means character we can include any character which will be treated as a string but it must be in single quotes
    float c = 5.67; //Here float means decimal numbers
    bool is_check = true; // this will give boolean value that is if its true then 1 if false then 0
    double x = 5.67890; // This is another decimal form but with more decimal points

    cout << "The value of a, b, c, is_check & x is:\n" <<a <<"\n" <<b <<"\n" <<c <<"\n" <<is_check <<"\n" <<x <<"\n";

    funct1();
    return 0;

}

// Now as everytime our program starts the program and runs only the function main so this will not print the values and run the function func1 unless and untill it is called in the main function.