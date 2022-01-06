using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Variables
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string characterName = "Jhon";
            int characterAge = 35;

            Console.WriteLine("Hello my name is " +characterName+ " I am " +characterAge+ " years old!");

            characterName = "William"; //We can change variable value in between of code as well 

            Console.WriteLine("Hello my name is " + characterName + " I am " + characterAge + " years old!");

            Console.ReadLine();
        }
    }
}
