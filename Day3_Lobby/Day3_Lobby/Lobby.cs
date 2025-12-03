namespace Day3_Lobby;
using System.IO;

public class Lobby
{
    public static void Main(string[] args)
    {
        string filepath = "input.txt"; // Be sure this file has "Copy to Output Directory" set to "Copy Always"
        string[] textfile = ReadInputFile(filepath);

        List<int> numPairs = [];

        int sum = 0;
        int count = 0;

        foreach (string line in textfile)
        {
            int numPair = GetHighestNumberPair(line);
            numPairs.Add(numPair);
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