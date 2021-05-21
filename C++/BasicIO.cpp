#include<iostream>
using namespace std;

int main()
{
    int num1, num2;
    cout<<"Enter the value of num1:\n";//this << is called insertion operator whih prints
    cin>>num1;//this >> is called extractions operator which accepts data from user

    cout<<"Enter the value of num2:\n";//this << is called insertion operator whih prints
    cin>>num2;//this >> is called extractions operator which accepts data from user

    cout<<"The sum is  "<<num1+num2;
    
    return 0;
}