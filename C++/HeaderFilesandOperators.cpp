#include <iostream>
/* There are two types of Header files:

1. System Header Files (Shipped by the user)
which is like #iclude<iostream>

2. User defined header file (Created by the user)
eg. #include"usr.h" --> This wil gie error if usr.h is not present in 
current directory
visit --> https://en.cppreference.com/w/cpp/header for more information */
using namespace std;

int main()
{
    int a = 5, b = 2;
    cout << "Operators in C++: " << endl;

    //Arithmetic Operator
    cout << "The value of a + b = " << a + b << endl;
    cout << "The value of a - b = " << a - b << endl;
    cout << "The value of a * b = " << a * b << endl;
    cout << "The value of a / b = " << a / b << endl; //the division of integers will always be integer
    cout << "The value of a % b = " << a % b << endl; //remainder is printed
    cout << "The value of a ++ = " << a++ << endl;    //here a is printed first then 1 is added to its value, that is a=5 is printed and a+1 is stored
    cout << "The value of a -- = " << a-- << endl;    //similarly above value which a+1 is printed and a+1-1 is stored
    cout << "The value of ++ a = " << ++a << endl;    //here 1 will be added to a+1-1 and then printed
    cout << "The value of --a = " << --a << endl;     //here 1 minus from above and then printed

    //Assignment Opperators (They are used to assign values to variables)
    //int = 3 here equal to is operator
    cout << endl;
    //Comparison Operator
    cout << "The value of a == b is " << (a == b) << endl;
    cout << "The value of a != b is " << (a != b) << endl;
    cout << "The value of a <= b is " << (a <= b) << endl;
    cout << "The value of a >= b is " << (a >= b) << endl;
    cout << "The value of a > b is " << (a > b) << endl;
    cout << "The value of a < b is " << (a < b) << endl;
    cout << endl;

    //Logical Operator
    cout << "The value of AND(&&) operator for ((a==b) && (a>b)) is: " << ((a == b) && (a > b)) << endl; //for AND means both must be true for the value of whole expression to be true
    cout << "The value of OR(||) operator for ((a==b) || (a>b)) is: " << ((a == b) || (a > b)) << endl;  //If either one of the values is true the expression is true
    cout << "The value of NOT(!) operator for !(a==b) is: " << !(a == b) << endl;                        //This will print the inverted or opposite value of the result of the expression

    return 0;
}