namespace Day3_Lobby;

public class Lobby
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Hello, world!");
    }

    public static int GetHighestNumberPair(string line)
    {
        char left = '0';
        char right = '0';

        char[] lineArr = line.ToCharArray();
        int len = lineArr.Length;
        int i = 0;

        foreach (char c in lineArr)
        {
            if (c > left && i != len - 1)
            {
                left = c;
            }
            else if (c > right)
            {
                right = c;
            }

            ++i;
        }
        
        
        int l = (int)Char.GetNumericValue(left);
        int r = (int)Char.GetNumericValue(right);
        int result = l * 10 + r;

        return result;
    }
}