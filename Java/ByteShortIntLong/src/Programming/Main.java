package Programming;

public class Main {

    public static void main(String[] args) {
	    int myValue = 10000; // This is an int data type with range

        int myMinIntValue = Integer.MIN_VALUE; // Integer is a wrapper class
        int myMaxIntValue = Integer.MAX_VALUE;

        System.out.println("Integer minimum value = "+myMinIntValue);
        System.out.println("Integer maximum value = "+myMaxIntValue);
        System.out.println("Busted MAX Value = "+(myMaxIntValue+1)); // Adding to a max value of the data type is called Overflow
        System.out.println("Busted MIN Value = "+(myMinIntValue-1)); // Reducing from minimum value of data type is called underflow

        byte myMinByteValue = Byte.MIN_VALUE;
        byte myMaxByteValue = Byte.MAX_VALUE;

        System.out.println("Byte minimum value ="+myMinByteValue);
        System.out.println("Byte maximum value ="+myMaxByteValue);

        short myMinShortValue = Short.MIN_VALUE;
        short myMaxShortValue = Short.MAX_VALUE;

        System.out.println("Short minimum value ="+myMinShortValue);
        System.out.println("Short maximum value ="+myMaxShortValue);

        // long values must be specified with L at the end
        // eg- lon myLongValue = 100L;
        long myMinLongValue = Long.MIN_VALUE;
        long myMaxLongValue = Long.MAX_VALUE;

        System.out.println("Long minimum value ="+myMinLongValue);
        System.out.println("Long maximum value ="+myMaxLongValue);

        // Byte occupies 8 bits
        // Short occupies 16 bits
        // Integer occupies 32 bits
        // Long occupies 64 bits
    }
}
