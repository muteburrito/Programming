<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Variables</title>
</head>
<body>
    Hello here we wil denote Variables:
    <?php
    //A variable is defined by $ sign

    $a = 5;
    $b = 6;

    echo $a;
    echo $b;
    /* Here we dont need to specify the data type it automatically identifies */

    $num1 = 56;
    $str1 = "Hello";

    echo $num1 + $b + $a;

    //Operators in PHP:
    //Arithmetic Operators
    echo "<h1>Arithmetic Operator</h1>";
    echo "<br>";
    echo "The value of a + b is", $a + $b;
    echo "<br>";//to add new line or space we can use html tags
    echo "The value of a - b is", $a - $b;
    echo "<br>";//to add new line or space we can use html tags
    echo "The value of a * b is", $a * $b;
    echo "<br>";//to add new line or space we can use html tags
    echo "The value of a / b is", $a / $b;
    echo "<br>";//to add new line or space we can use html tags

    //Comparison Operator
    //This retuen a boolean value ie. 1 or blank depending on the condition
    echo "<h1>Comparison Operator</h1>";
    echo "<br>";
    echo "The value of a == b is: ", $a == $b;
    echo var_dump($a == $b);
    echo "<br>";
    echo "The value of a <= b is: ", $a <= $b;
    echo var_dump($a <= $b); //This will dump the value of the boolean
    echo "<br>";
    echo "The value of a >= b is: ", $a >= $b;
    echo var_dump($a >= $b);
    echo "<br>";
    echo "The value of a != b is: ", $a != $b;
    echo var_dump($a != $b);
    echo "<br>";
    echo "The value of a < b is: ", $a < $b;
    echo var_dump($a < $b);
    echo "<br>";
    echo "The value of a > b is: ", $a > $b;
    echo var_dump($a > $b);
    echo "<br>";
    

    //Assignment Operator (As the name states. it is used to assign the values )
    echo "<h1>Assignment Operator</h1>";
    echo "<br>";
    $var1 = $a;
    echo $var1;
    echo "<br>";
    $var1 += 1; // This will add 1 and print 
    echo $var1;
    echo "<br>";
    $var1 -= 1; // This will subtract 1 and print
    echo $var1;
    echo "<br>";
    $var1 *= 10; //This will multiply 10 and print
    echo $var1;
    echo "<br>";
    $var1 /= 10; //This wull divide 10
    echo $var1;
    echo "<br>";


    //Logical Operator
    echo "<h1>Logical Operator</h1>";
    // there is AND (&&), OR (||), XOR, NOT(!)
    $log = (true and true); // when both are true then only it will give true ow it will be false
    echo var_dump($log);
    echo "<br>";
    $log = (false or true); //Even if one condtion is true it will be true
    echo var_dump($log);
    echo "<br>";
    $log = (false xor true); //This condition requies true as well as flase to return true. if not then it will give false
    echo var_dump($log);
    echo "<br>";
    $log = (!false); //This will invert the original value 
    echo var_dump($log);
    echo "<br>";


    //Increment Operator
    $Ivar = 0;
    echo "<h1>Increment Operator</h1>";
    echo "<br>";
    echo $Ivar++; //This will first print the value and then add 1 to it and store it
    echo $Ivar;
    echo "<br>";
    echo $Ivar--; // This fir print the value of va1 and then sub 1 and store it 
    echo $Ivar;
    echo "<br>";
    echo ++$Ivar; // This will first add 1 to the value and then print it 
    echo $Ivar;
    echo "<br>";
    echo --$Ivar; //Similarly this will sub 1 from the value and then print it
    echo $Ivar;
    echo "<br>"
    ?>
</body>
</html>