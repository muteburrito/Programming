package com.example.javarefresher;

public class fuctions {
    public static double average(int a, int b, int c){
        return (a + b + c)/3;
    }
    public static void main(String[] args) {
        int a = 34;
        int b = 45;
        int c = 56;
        System.out.println(average(a, b, c));
        ClassEx nclass = new ClassEx();
        nclass.method1();
        ClassInherit nclass2 = new ClassInherit();
        nclass2.method1();
        nclass2.method2();
    }
}
