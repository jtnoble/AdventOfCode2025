# Day 2: Gift Shop

## Personal Log About My Solution
I feel like my solution was a little complicated; however, it was still solid. Not the best solution, but still pretty quick.

Part 2 though... This was extremely slow. On my computer it took nearly 20 seconds to run when getting the answer the first time (Ryzen 5600X).

My original implementation had a ton of repeats. For example, the number 755752303 breaks into the following:
['7557', '5230', '3'],
['755', '752', '303'],
['75', '57', '52', '30', '3'],
['75', '57', '52', '30', '3'],
['75', '57', '52', '30', '3'],
['7', '5', '5', '7', '5', '2', '3', '0', '3'],
['7', '5', '5', '7', '5', '2', '3', '0', '3'],
['7', '5', '5', '7', '5', '2', '3', '0', '3']

If you notice... There are a lot of repeats here. This was because the `split_number` rounds the value, causing repeat splits.

For example: `len("755752303") / 4 = 2.25`, `len("755752303") / 5 = 1.8`, `len("755752303") / 6 = 1.5`. All of these round to 2, meaning we're just going to repeat grabbing two numbers at a time 3 times in a row. My solution was to just check if `split_number` received an input that would split unevenly, causing a value to not match the same length as the rest, and just skip it if this were true.

Now we're down to about 9 seconds. Again, I feel like (without multiprocessing) this could be significantly faster, but maybe I'll revisit another day.

## Problem Statement:

https://adventofcode.com/2025/day/2