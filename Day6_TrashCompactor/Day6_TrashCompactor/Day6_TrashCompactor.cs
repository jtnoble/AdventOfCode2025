namespace Day6_TrashCompactor;

public class Day6_TrashCompactor
{
    public static void Main(string[] args)
    {
        RunPart1();
        RunPart2();
    }

    // Part 2
    public static void RunPart2()
    {
        string[] input = ReadFile.ReadInputFile("input.txt");

        int maxLength = input.Max(s => s.Length);
        List<string> normalizedLines = input.Select(s => s.PadRight(maxLength)).ToList();

        long result = SolvePart2(normalizedLines, maxLength);

        Console.WriteLine($"The final amount for part 2 is {result}");
    }

    public static long SolvePart2(List<string> lines, int width)
    {
        long grandTotal = 0;

        List<long> currentNumbers = new List<long>();
        string currentOperator = "";

        int rows = lines.Count;

        for (int x = 0; x < width; x++)
        {
            string colNumberStr = "";
            bool isColumnEmpty = true;

            for (int y = 0; y < rows; y++)
            {
                char c = lines[y][x];

                if (c != ' ')
                {
                    isColumnEmpty = false;
                    if (c == '+' || c == '*')
                    {
                        currentOperator = c.ToString();
                    }
                    else
                    {
                        colNumberStr += c;
                    }
                }
            }

            if (isColumnEmpty)
            {
                if (currentNumbers.Count > 0)
                {
                    grandTotal += CalculateBlock(currentNumbers, currentOperator);
                    currentNumbers.Clear();
                    currentOperator = "";
                }
            }
            else
            {
                if (!string.IsNullOrEmpty(colNumberStr))
                {
                    currentNumbers.Add(long.Parse(colNumberStr));
                }
            }
        }

        if (currentNumbers.Count > 0)
        {
            grandTotal += CalculateBlock(currentNumbers, currentOperator);
        }

        return grandTotal;
    }

    public static long CalculateBlock(List<long> numbers, string op)
    {
        if (numbers.Count == 0)
            return 0;

        long result = (op == "*") ? 1 : 0;

        foreach (long num in numbers)
        {
            if (op == "*")
                result *= num;
            else
                result += num; 
        }
        return result;
    }

    // PART 1
    public static void RunPart1()
    {
        string[] input = ReadFile.ReadInputFile("input.txt");
        List<string[]> splitLines = SplitLines(input);
        string[] operands = SeparateOperands(splitLines);

        long[] operations = PerformOperations(splitLines, operands);
        long result = SumAllValues(operations);

        Console.WriteLine($"The final amount for part 1 is {result}");

    }

    public static List<string[]> SplitLines(string[] lines)
    {
        List<string[]> result = [];
        foreach (string line in lines)
        {
            string[] valuesInLine = line.Split(" ", StringSplitOptions.RemoveEmptyEntries);
            result.Add(valuesInLine);
        }

        return result;
    }

    public static string[] SeparateOperands(List<string[]> splitLines)
    {
        string[] result = splitLines.Last();
        splitLines.Remove(result);

        return result;
    }

    public static long[] PerformOperations(List<string[]> numbersList, string[] operands)
    {
        long[] result = new long[operands.Length];

        for (int i = 0; i < result.Length; i++)
        {
            long operation = operands[i] == "+" ? 0 : 1; // if addition, 0, if multiplication, 1
                foreach (string[] numbers in numbersList)
                {
                    switch (operands[i])
                    {
                        case "+":
                            operation += long.Parse(numbers[i]);
                            break;
                        case "*":
                            operation *= long.Parse(numbers[i]);
                            break;
                    }
                }
            result[i] = operation;
        }

        return result;
    }

    public static long SumAllValues(long[] values) => values.Sum();
    public static long SumAllValues(List<long> values) => values.Sum();

}

public static class ReadFile
{
    public static string[] ReadInputFile(string filepath)
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