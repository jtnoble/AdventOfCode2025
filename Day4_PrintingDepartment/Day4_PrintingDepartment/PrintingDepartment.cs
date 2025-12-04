namespace Day4_PrintingDepartment;

public class PrintingDepartment()
{
    const char paperSymbol = '@';
    const char emptySymbol = '.';
    public static void Main(string[] args)
    {
        RunPart1();
        RunPart2();
    }

    public static void RunPart2()
    {
        // Main for Part 1
        string input = ReadFile.ReadInputFile("input.txt");
        List<List<char>> matrix = GetMatrix(input);

        int count = 0;
        bool paperThisRun = true;

        while (paperThisRun)
        {
            int preCount = count;
            for (int i = 0; i < matrix.Count; i++)
            {
                for (int j = 0; j < matrix[i].Count; j++)
                {
                    if (matrix[i][j] != paperSymbol)
                        continue;

                    string neighbors = GetNeighbors(matrix, i, j);
                    int countedPaper = CountPaper(neighbors);

                    if (CanRemovePaper(countedPaper))
                    {
                        matrix[i][j] = emptySymbol;
                        count++;
                    }
                }
            }
            paperThisRun = preCount != count;
        }

        Console.WriteLine($"PART 2: The amount of paper you can remove is {count} rolls!");

    }
    public static void RunPart1()
    {
        // Main for Part 1
        string input = ReadFile.ReadInputFile("input.txt");
        List<List<char>> matrix = GetMatrix(input);

        int count = 0;

        for (int i = 0; i < matrix.Count; i++)
        {
            for (int j = 0; j < matrix[i].Count; j++)
            {
                if (matrix[i][j] != paperSymbol)
                    continue;

                string neighbors = GetNeighbors(matrix, i, j);
                int countedPaper = CountPaper(neighbors);

                if (CanRemovePaper(countedPaper))
                {
                    count++;
                }
            }
        }

        Console.WriteLine($"PART 1: The amount of paper you can remove is {count} rolls!");

    }

    public static List<List<char>> GetMatrix(string input)
    {
        List<List<char>> matrix = [];

        string[] splitByNewLineInput = input.Split(new[] { "\r\n", "\n" }, StringSplitOptions.RemoveEmptyEntries);

        foreach (string line in splitByNewLineInput)
        {
            List<char> row = [];
            foreach (char c in line)
            {
                row.Add(c);
            }
            matrix.Add(row);
        }

        return matrix;
    }

    public static string GetNeighbors(List<List<char>> matrix, int row, int col)
    {
        List<char> neighbors = [];

        if (row > 0 && col > 0)
            neighbors.Add(matrix[row - 1][col - 1]); // Top Left

        if (row > 0)
            neighbors.Add(matrix[row - 1][col]); // Top Middle

        if (row > 0 && col < matrix[row - 1].Count - 1)
            neighbors.Add(matrix[row - 1][col + 1]); // Top Right

        if (col > 0)
            neighbors.Add(matrix[row][col - 1]); // Left

        if (col < matrix[row].Count - 1)
            neighbors.Add(matrix[row][col + 1]); // Right

        if (row < matrix.Count - 1 && col > 0)
            neighbors.Add(matrix[row + 1][col - 1]); // Bottom Left

        if (row < matrix.Count - 1)
            neighbors.Add(matrix[row + 1][col]); // Bottom Middle

        if (row < matrix.Count - 1 && col < matrix[row + 1].Count - 1)
            neighbors.Add(matrix[row + 1][col + 1]); // Bottom Right

        string result = new string(neighbors.ToArray());
        return result;
    }

    public static int CountPaper(string line)
    {
        int count = line.Count(c => c == paperSymbol);
        return count;
    }

    public static bool CanRemovePaper(int count)
    {
        return count < 4;
    }
}

public static class ReadFile
{
    public static string? ReadInputFile(string filepath)
    {
        try
        {
            string lines = File.ReadAllText(filepath);
            return lines;
        }
        catch (IOException e)
        {
            Console.WriteLine(e.ToString());
            return null;
        }
    }
}