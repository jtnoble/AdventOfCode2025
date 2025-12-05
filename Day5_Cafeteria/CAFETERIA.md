# Day 5: Cafeteria

## Personal Log About My Solution
Part 1 of this has was the easiest solution so far this year. It took me maybe 5 minutes? I didn't originally like how it looked, so I did separate it into functions and classes, but originally it was just all combined into a few lines of code.

Part 2 is where things got a little more difficult. Everything was the same, except now we needed to count the valid ingredients within the ranges, forgetting about the separated ingredients from part 1.

Conceptually, this was easy. Check the ranges, if they run into each other, then broaden the ranges, otherwise make them separate ranges. Do this for every range, and then the ends minus the starts of each range summed together (+1 for each to make it inclusive) would be the answer.

My first attempt was to just go through every one in order. It was brute force, and nested, where range one would check if range two falls within its range, and if it does, then shift the ranges around, then move on. Not only was this really rough looking, it also took *forever* to run. I believe I had a working solution, but after about 10 minutes of my RAM being maxed out, I don't know if I would really call it *a solution*.

My final answer started with sorting the ranges first by their starting point, and adding the first range of the sorted ranges to a merged list. Then, we go through every range in our sorted range list and compare the start of the current range to the end of the last range in the merged list. If the start is less than the end, we make the last range's end the larger of itself and the current range's end. Otherwise, we just add our current range ot the merged list.

Quite a nifty solution that doesn't take 23 days on a super computer to run.

## Problem Statement:

https://adventofcode.com/2025/day/5