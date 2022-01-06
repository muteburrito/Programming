using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Strings
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This is a simple plain string \n This will be on a \"new line\""); // BackSlash is a escape character in c#

            string phrase = "Hello" + "World"; //We can concatinate the strings in thi sway

            Console.WriteLine(phrase.Length); //Legth is a inbuilt method of a string to calculate the length and print the characters !  
            Console.WriteLine(phrase.ToUpper());
            Console.WriteLine(phrase.ToLower());
            Console.WriteLine(phrase.Contains("World"));
            Console.WriteLine(phrase[0]); //This is indexing cs and will print the context of the string at that index 
            Console.WriteLine(phrase.IndexOf("World")); //This will return the index of the string 
            Console.WriteLine(phrase.IndexOf('o')); //Single quotes will take a character 
            Console.WriteLine(phrase.Substring(3)); //This will start the string from the index mentiond 
            Console.WriteLine(phrase.Substring(3, 2)); //This will only print 2 chars

            Console.ReadLine();
        }
    }
}
