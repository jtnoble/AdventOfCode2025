namespace Test_Day6_TrashCompactor;
using Day6_TrashCompactor;

public class Test_Day6_TrashCompactor
{
    // PART 2
    [Theory]
    [InlineData(new long[] { 1, 2, 3 }, "+", 6)]   // 1 + 2 + 3 = 6
    [InlineData(new long[] { 2, 3, 4 }, "*", 24)]  // 2 * 3 * 4 = 24
    [InlineData(new long[] { 5 }, "+", 5)]         // Single number addition
    [InlineData(new long[] { 5 }, "*", 5)]         // Single number multiplication
    [InlineData(new long[] { }, "+", 0)]           // Empty list safety
    public void CalculateBlock_ShouldComputeCorrectly(long[] input, string op, long expected)
    {
        List<long> numbers = input.ToList();

        long result = Day6_TrashCompactor.CalculateBlock(numbers, op);

        Assert.Equal(expected, result);
    }

    [Fact]
    public void SolvePart2_ShouldMatchExampleResult()
    {
        List<string> rawInput = new List<string>
            {
                "123 328  51 64 ",
                " 45 64  387 23 ",
                "  6 98  215 314",
                "*   +   *   +  "
            };

        int maxLength = rawInput.Max(s => s.Length);
        List<string> normalized = rawInput.Select(s => s.PadRight(maxLength)).ToList();

        long result = Day6_TrashCompactor.SolvePart2(normalized, maxLength);

        Assert.Equal(3263827, result);
    }


    // PART 1
    [Fact]
    public void SeparateOperands_ShouldRemoveLastLine_AndReturnIt()
    {
        List<string[]> data = new List<string[]>
            {
                new string[] { "1", "2" },
                new string[] { "3", "4" },
                new string[] { "+", "*" }
            };

        string[] operands = Day6_TrashCompactor.SeparateOperands(data);

        Assert.Equal(2, data.Count);
        Assert.Equal(new string[] { "+", "*" }, operands);
        Assert.Equal("1", data[0][0]);
    }

    [Fact]
    public void PerformOperations_Part1_ShouldCalculateColumns()
    {
        List<string[]> numbers = new List<string[]>
            {
                new string[] { "10", "2" },
                new string[] { "5", "4" }
            };
        string[] operands = new string[] { "+", "*" };

        long[] results = Day6_TrashCompactor.PerformOperations(numbers, operands);

        Assert.Equal(15, results[0]);
        Assert.Equal(8, results[1]);
    }

    [Fact]
    public void SplitLines_ShouldRemoveEmptyEntries()
    {
        string[] input = new string[] { "10   20  30" };

        List<string[]> result = Day6_TrashCompactor.SplitLines(input);

        Assert.Single(result);
        Assert.Equal(3, result[0].Length);
        Assert.Equal("20", result[0][1]);
    }
}