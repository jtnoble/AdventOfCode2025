# Day 7: Laboratories

## Personal Log About My Solution
Part 1 I wasn't *fully* understanding at first, but once I understood, it wasn't too difficult.

My original thought was that I was supposed to count the amount of beams. Definitely not the right answer. Afterwards, I needed to count the amount of splits, but originally I just thought "well isn't it just the amount of '^' characters? Answer, no, but rather, the amount of '^' characters that have a '|' entering the top of it.

I wanted a small visualization for this, so I went ahead and made and output.txt as well, that turns into a nice sort of Christmas tree shape.

As for Part 2, I must admit, I ever so slightly cheated... I was browsing Reddit and found a post visualizing part 1 and 2, and spoiled that there was a more "mathy" solution. [Credits to the post here](https://www.reddit.com/r/adventofcode/comments/1pgnmou/2025_day_7_lets_visualize/).

Essentially, I just made a list that's the same length as the lines since they're all the same length anyways. That list is just a bunch of ints, starting at 0. If the character is S, then just add one to that index. If the character is '^', then add one to the left and right int, then reset the current int to 0. Then just sum up all the values. Way better than my thoughts to try doing some sort of "Convert to a binary tree then count everything that way" solution.

## Problem Statement:

https://adventofcode.com/2025/day/7