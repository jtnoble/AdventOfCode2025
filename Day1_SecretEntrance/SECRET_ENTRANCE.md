# Day 1: Secret Entrance

## Personal Log About My Solution
This log is coming a little later than my solution, so it isn't as fresh for me.

I decided I wanted to use OOP a little deeper and make this scalable. The problem asks for a dial from 0-99, but I like the idea of theoretically being able to handle a dial of 0-149, or even 0-999.

For part 1, the rotation functions ended up being pretty simple. Just rotate the dial by an amount, and use modulo to handle if you pass the upper or lower bounds, in this case 99 and 0.

As for turning the dial based on an amount, this was just splitting the string into a left value that is just the first character of the string, and the rest of the string converted to an int for movement.

Part 2 gets a little more rough. Turn dial is the exact same, but now we need to accont for every pass of 0 or 99.

The tldr without getting too into the nitty-gritty: We use modulo division to check the amount we are above or below the bounds so we can grab excess passes, then sort of do a similar thing to part 1.

Overall pretty satisfied with this solution.


## Problem Statement:

https://adventofcode.com/2025/day/1