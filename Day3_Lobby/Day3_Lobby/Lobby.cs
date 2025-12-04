namespace Day3_Lobby;
using System.IO;
using System.Numerics;
using static System.Runtime.InteropServices.JavaScript.JSType;

public class Lobby
{
    public static void Main(string[] args)
    {
        //Console.WriteLine("PART ONE:");
        //LobbyPart1.Run();
        Console.WriteLine("PART TWO:");
        LobbyPart2.Run();
    }
}

public class LobbyPart2()
{
    public static void Run()
    {
        int batteryAmount = 12; // Defined by problem
        string filepath = "input.txt"; // Be sure this file has "Copy to Output Directory" set to "Copy Always"
        string[] textfile = ReadInputFile(filepath);

        long sum = 0;
        int count = 0;

        foreach (string line in textfile)
        {
            long nums = GetHighestNumberGroup(line, batteryAmount);
            sum += nums;
            count++;
            Console.WriteLine($"{count}: {nums}");
        }
        Console.WriteLine($"The password is: {sum}");
    }

    public static long GetHighestNumberGroup(string line, int batteryAmount)
    {
        char[] lineArr = line.ToCharArray();
        char[] arr = new string('0', batteryAmount).ToCharArray();


        for (int i = 0; i < lineArr.Length; i++)
        {
            bool replaced = false;
            int j = 0;
            if (lineArr.Length - i < arr.Length)
            {
                j = arr.Length - (lineArr.Length - i);
            }
            while (j < arr.Length)
            {
                if (replaced)
                    arr[j] = '0';

                else if (arr[j] < lineArr[i])
                {
                    arr[j] = lineArr[i];
                    replaced = true;
                }
                    j++;
            }
        }

        string numberAsStr = new string(arr);
        return long.Parse(numberAsStr);
    }

    public static string[]? ReadInputFile(string filepath)
    {
        try
        {
            string[] lines = File.ReadAllLines(filepath);
            return lines;
        }
        catch (IOException e)
        {
            Console.WriteLine(e.ToString());
            return null;
        }
    }
}

public class LobbyPart1()
{
    public static void Run()
    {
        string filepath = "input.txt"; // Be sure this file has "Copy to Output Directory" set to "Copy Always"
        string[] textfile = ReadInputFile(filepath);

        int sum = 0;
        int count = 0;

        foreach (string line in textfile)
        {
            int numPair = GetHighestNumberPair(line);
            sum += numPair;
            count++;
            Console.WriteLine($"{count}: {numPair}");
        }
        Console.WriteLine($"The password is: {sum}");
    }

    public static int GetHighestNumberPair(string line)
    {
        int maxLeft = -1;
        int maxPair = -1;

        foreach (char c in line)
        {
            int digit = c - '0';

            if (maxLeft != -1)
            {
                int newValue = maxLeft * 10 + digit;
                if (newValue > maxPair)
                    maxPair = newValue;
            }

            if (digit > maxLeft)
                maxLeft = digit;
        }
        return maxPair;
    }

    public static string[]? ReadInputFile(string filepath)
    {
        try
        {
            string[] lines = File.ReadAllLines(filepath);
            return lines;
        }
        catch (IOException e)
        {
            Console.WriteLine(e.ToString());
            return null;
        }
    }
}