# Day 4: Printing Department

## Personal Log About My Solution
Full disclosure, I recently had to do nearly this exact same thing a few weeks ago as part of a technical interview, though, it was framed as Minesweeper there. This is the same, but instead of mines, its paper, and instead of returning the count, it's just checking if there are 3 or more adjacent spaces with a mine/paper. This interview was in Python, so I knew I had to do this in C#.

Essentially, I just broke this down into converting the input into a matrix (2D array?), retrieved the neighbors from each point in the matrix, counted the amount of '@' symbols, and lastly if the symbols in the neighbors were 4 or more, added this to the total roll count.

Part 2 was super simple, as all I needed to do was replace checked paper rolls with a '.', and keep looping until no more paper rolls were found. This is easy with a boolean that just checks if the new count is the same as the count before the loop, and if it was the same, then we should be done and can't grab any further rolls.

## Problem Statement:

https://adventofcode.com/2025/day/4