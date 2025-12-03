namespace Test_Day3_Lobby;
using Day3_Lobby;

public class LobbyTest
{
    [Fact]
    public void GetHighestNumberPairReturnsHighestNumberPair()
    {
        // Check that the number pair that makes for the largest number is returned
        int pair = Lobby.GetHighestNumberPair("9822554262");
        Assert.Equal(98, pair);

        pair = Lobby.GetHighestNumberPair("258912090");
        Assert.Equal(99, pair);

        pair = Lobby.GetHighestNumberPair("8685147529");
        Assert.Equal(89, pair);

        pair = Lobby.GetHighestNumberPair("74444444");
        Assert.Equal(74, pair);

        pair = Lobby.GetHighestNumberPair("1111111111");
        Assert.Equal(11, pair);
    }
}