namespace Test_Day3_Lobby;
using Day3_Lobby;
using System.Numerics;

public class LobbyTest
{
    // Part 2
    [Theory]
    [InlineData("987654321111111", 987654321111)]
    [InlineData("811111111111119", 811111111119)]
    [InlineData("234234234234278", 434234234278)]
    [InlineData("818181911112111", 888911112111)]
    public void GetHighestNumberGroupReturnsHighestNumberGroups(string value, long expected)
    {
        // Based off of examples from part 2 page
        long result = LobbyPart2.GetHighestNumberGroup(value, 12);
        Assert.Equal(expected, result);

    }

    // Part 1
    [Fact]
    public void GetHighestNumberPairReturnsHighestNumberPair()
    {
        // Check that the number pair that makes for the largest number is returned
        int pair = LobbyPart1.GetHighestNumberPair("9822554262");
        Assert.Equal(98, pair);

        pair = LobbyPart1.GetHighestNumberPair("258912090");
        Assert.Equal(99, pair); 
    }

    [Fact]
    public void GetHighestNumberPairLargestNumberAtEnd()
    {
        int pair = LobbyPart1.GetHighestNumberPair("8685147529");
        Assert.Equal(89, pair);
    }

    [Fact]
    public void GetHighestNumberPairLargestNumberAtStart()
    {
        int pair = LobbyPart1.GetHighestNumberPair("74444444");
        Assert.Equal(74, pair);
    }

    [Fact]
    public void GetHighestNumberPairAllNumbersEqual()
    {
        int pair = LobbyPart1.GetHighestNumberPair("1111111111");
        Assert.Equal(11, pair);
    }

}