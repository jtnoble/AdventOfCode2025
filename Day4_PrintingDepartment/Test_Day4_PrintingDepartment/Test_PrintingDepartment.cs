namespace Test_Day4_PrintingDepartment;
using Day4_PrintingDepartment;

public class Test_PrintingDepartment
{
    // PART 1
    [Theory]
    [InlineData("....@@..@@@.@..", 6)]
    [InlineData("@..........@..@", 3)]
    [InlineData("@.............@", 2)]
    [InlineData("@........@@@...", 4)]
    public void TestCountPaper(string line, int expected)
    {
        int actual = PrintingDepartment.CountPaper(line);
        Assert.Equal(expected, actual);
    }

    [Fact]
    public void TestCountPaperAllPaper()
    {
        int actual = PrintingDepartment.CountPaper("@@@@@@@@@@@@@@@@@@@@");
        Assert.Equal(20, actual);
    }
    [Fact]
    public void TestCountPaperAllNotPaper()
    {
        int actual = PrintingDepartment.CountPaper("....................");
        Assert.Equal(0, actual);
    }

    public static IEnumerable<object[]> SampleMatrix()
    {
        // Sample Matrix for testing GetNeighbors
        yield return new object[]
        {
            new List<List<char>>
            {
                new() { '.', '@', '.' },
                new() { '.', '.', '@' },
                new() { '.', '.', '@' }
            }
        };
    }


    [Theory]
    [MemberData(nameof(SampleMatrix))]
    public void TestGetNeighborsCenter(List<List<char>> matrix)
    {
        string expected = ".@..@..@"; // All but the center value
        string actual = PrintingDepartment.GetNeighbors(matrix, 1, 1);

        Assert.Equal(expected, actual);
    }

    [Theory]
    [MemberData(nameof(SampleMatrix))]
    public void TestGetNeighborsTopLeft(List<List<char>> matrix)
    {
        string expected = "@..";
        string actual = PrintingDepartment.GetNeighbors(matrix, 0, 0);

        Assert.Equal(expected, actual);
    }

    [Theory]
    [MemberData(nameof(SampleMatrix))]
    public void TestGetNeighborsTopMiddle(List<List<char>> matrix)
    {
        string expected = "....@";
        string actual = PrintingDepartment.GetNeighbors(matrix, 0, 1);

        Assert.Equal(expected, actual);
    }

    [Theory]
    [MemberData(nameof(SampleMatrix))]
    public void TestGetNeighborsTopRight(List<List<char>> matrix)
    {
        string expected = "@.@";
        string actual = PrintingDepartment.GetNeighbors(matrix, 0, 2);

        Assert.Equal(expected, actual);
    }

    [Theory]
    [MemberData(nameof(SampleMatrix))]
    public void TestGetNeighborsLeft(List<List<char>> matrix)
    {
        string expected = ".@...";
        string actual = PrintingDepartment.GetNeighbors(matrix, 1, 0);

        Assert.Equal(expected, actual);
    }

    [Theory]
    [MemberData(nameof(SampleMatrix))]
    public void TestGetNeighborsRight(List<List<char>> matrix)
    {
        string expected = "@...@";
        string actual = PrintingDepartment.GetNeighbors(matrix, 1, 2);

        Assert.Equal(expected, actual);
    }

    [Theory]
    [MemberData(nameof(SampleMatrix))]
    public void TestGetNeighborsBottomLeft(List<List<char>> matrix)
    {
        string expected = "...";
        string actual = PrintingDepartment.GetNeighbors(matrix, 2, 0);

        Assert.Equal(expected, actual);
    }

    [Theory]
    [MemberData(nameof(SampleMatrix))]
    public void TestGetNeighborsBottomMiddle(List<List<char>> matrix)
    {
        string expected = "..@.@";
        string actual = PrintingDepartment.GetNeighbors(matrix, 2, 1);

        Assert.Equal(expected, actual);
    }

    [Theory]
    [MemberData(nameof(SampleMatrix))]
    public void TestGetNeighborsBottomRight(List<List<char>> matrix)
    {
        string expected = ".@.";
        string actual = PrintingDepartment.GetNeighbors(matrix, 2, 2);

        Assert.Equal(expected, actual);
    }

    [Fact]
    public void TestGetMatrix()
    {
        string input = "..@\n@..\n.@.";

        List<List<char>> expected = [
            ['.', '.', '@'],
            ['@', '.', '.'],
            ['.', '@', '.']
        ];

        List<List<char>> actual = PrintingDepartment.GetMatrix(input);

        Assert.Equal(expected, actual);
    }

    [Fact]
    public void TestCanRemovePaperTrue()
    {
        int count = 3;

        bool expected = true;
        bool actual = PrintingDepartment.CanRemovePaper(count);

        Assert.Equal(expected, actual);
    }

    [Fact]
    public void TestCanRemovePaperFalse()
    {
        int count = 4;

        bool expected = false;
        bool actual = PrintingDepartment.CanRemovePaper(count);

        Assert.Equal(expected, actual);
    }
}