package com.example.javarefresher;

import java.util.ArrayList;

public class Arrays {
    public static void main(String[] args) {
        int [] arr1 =  {1, 3, 4, 5 ,6 , 7};
        System.out.println(arr1[3]);
        ArrayList newlist = new ArrayList();
        newlist.add(24);
        newlist.add(45);
        newlist.add(26);
        System.out.println(newlist);
        System.out.println(newlist.contains(24));
        for (Object o: newlist ){
            System.out.println("Object is : "+o);
        }
    }
}
