# Advent Of Code - Jtnoble
This is my documentation of my "Advent of Code" solutions for the year 2025.
Each day is a different problem, and solving that problem leads to a solution to a code.
This year, I am trying to focus on Test-Driven Development principles.

### Subdirectories
Each subdirectory will have a solution. Included is also a {DAY_TITLE}.md that is simply the problem for the day. Most every directory should run similarly, though, there might be a mixed batch of code (Python, C#, maybe something else?)

### Running Python
- Ensure Python3.12 is installed
- Change into the respective day's subdirectory
- Create a virtual environment: `python3 -m venv .venv`
  - Activate the environment Linux: `source .venv/bin/activate` | Windows: `.\.venv\Scripts\activate `
- Install dependencies: `pip install -r requirements.txt`
- Run tests in command line with `pytest`
- Run the solution by running the main file `python3 src/<main_filename>.py`


### More Information
https://adventofcode.com/2025