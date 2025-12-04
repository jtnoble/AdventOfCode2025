# Advent Of Code - Jtnoble
This is my documentation of my "Advent of Code" solutions for the year 2025.
Each day is a different problem, and solving that problem leads to a solution to a code.
This year, I am trying to focus on Test-Driven Development principles.

### Subdirectories
Each subdirectory will have a solution. Included is also a {DAY_TITLE}.md that has some of my thoughts, along with a link to the problem for the day. Most every directory should run similarly, though, there might be a mixed batch of code (Python, C#, maybe something else?). To note as well, I will have provided a truncated version of my sample input to show you what the input *might* look like, but not exactly to avoid any spoiling.

### Running Python
- Ensure Python3.12 is installed
- Change into the respective day's subdirectory
- Create a virtual environment: `python3 -m venv .venv`
  - Activate the environment Linux: `source .venv/bin/activate` | Windows: `.\.venv\Scripts\activate `
- Install dependencies: 
  - If there is any other dependencies than `pytest`, then there will be a `requirements.txt` file. Run: `pip install -r requirements.txt`
  - If there is no `requirements.txt` file, then you can assume `pytest` is the only dependency. Run: `pip install pytest==9.0.1`
- Run tests in command line with `pytest`
- Run the solution by running the main file `python3 src/<main_filename>.py`

### Running C#
- Ensure .NET 8.0.x is installed: `dotnet --version`
- Restore dependencies: `dotnet restore`
- Run tests: `dotnet test`
- Run main code: `dotnet run`
  - *Note: Tests can be run from the project root, running main needs to be done in the `Day3_Lobby` directory


### More Information
https://adventofcode.com/2025