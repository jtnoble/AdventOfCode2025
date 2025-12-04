# Day 3: Lobby

## Personal Log About My Solution
Much like yesterday, Part 1 was a little bit of a doozy, but part 2 was much more difficult. Rubberducking helped like crazy here, though, I kinda skimped on the TDD. I also chose to use C# this time around, and think that it may have made things easier honestly, being forced to think about char arrays more than Python's wonderful dynamic typing and not-so-limited length lists.

So for part 1:

I went through each character in a string and calculated the left value * 10 to place it in the 10s place plus the character. After, I would check the new value against the current max pair, and replace it if the value we just created was greater. Lastly, I would change the highest left digit (in the 10s place) if it were lower than the current digit

E.g., 
- Current pair is 21, the number is 9. We would calculate `value = 2 * 10 + 9` -> `value = 29`
- 29 is greater than our max pair of 21, so we would replace our max pair with 29.
- Now, we check if 9 is greater than our previous left max, 2.
- 9 is greater than 2, so replace it with 9.
- We're left with `maxPair = 29` and `maxLeft = 9`.

Now, if this were to continue onward, then we would of course see `9 * 10 + x` -> `9x`, which is definitely larger than our current pair, so we'd make changes. But if this were the end, then this 29 would be our returned value.

Now Part 2:

The first thing I did was hardcode the heck out of this. I'm talking `char[] arr = { '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0' }`, calculating using the magical number 12, etc. We'll talk about optmizations in a moment.

I broke things down into a list, and caught exceptions later on. This sort of aligns with TDD, though, really just the "refactor" portion.

- Create an empty arr of 0s 
- Loop through each character (number) of the line
- Loop through each value in the arr.
- Find the first value that the character > the number in the arr
- After doing so, replace all subsequent values with 0s.

I went through this 1 by 1. And while it *can* work, there is a glaring problem. This doesn't catch if the amount of content left in our line is larger than our arrays length of 12. We might be at element 20 of a 25 number string, but we're still replacing value 0.

This required me calculating 12 minus the string's length minus the string's current index. This gives me the starting point for my arr.

E.g.,

In a normal instance:
```
// splitting line into char array...
line = 81111111111191111111
arr = { '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0' };
```
At `line[0]` and `arr[0]`, we see 0 is greater than 8, so we replace is with 8. Likewise, at 1,1 we see 1 is less than 8, so we move to the next arr value, and see that 1 is greater than 0, so we replace the second index of arr with 1. But what about that 9?

Without the check in place, that 9 would change the first element of the arr, leading to an out of bounds error because there isn't enough numbers after the 9 to fill out the whole array.

```
arr = { '9', '1', '1', '1', '1', '1', '1', '1', INDEX ERROR: PAST LINE LENGTH, ...};
```

If we instead take the arr length minus line length minus the current index of the line, we get a starting point for our array to not overflow.

```
12 - (line_length(20) - index(12)) -> 12 - 8 -> 4
arr = { '8', '1', '1', '1', START_HERE:'1', '1', '1', '1', '1', '1', '1', '1' };
```

This way, `{'8', '1', '1', '1'` is untouched, while the rest is replaced.

As for minor optimizations/scalability, I went ahead and utilized a BatteryAmount variable. While it has no error checking for line length, theoretically if we were asked to instead use only 9 values, it should work.



## Problem Statement:

https://adventofcode.com/2025/day/3