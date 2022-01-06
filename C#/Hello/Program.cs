using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hello
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string name;

            Console.Write("Enter Your name: ");
            name = Console.ReadLine();

            Console.WriteLine("Hello, World!!");
            Console.WriteLine("Hello " + name);

            Console.ReadLine();
        }
    }
}
