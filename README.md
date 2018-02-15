# Project Euler

Solving math problems using Python 3.6, using a plethora of external libraries. Problems are available [here](https://projecteuler.net/archives).

Since writing scripts to solve those problems didn't feel quite enough, I also created a manager script, `_project_euler.py`, that imported and ran the scripts in sequence and also displayed progress information (this required instantiating a `Progress()` class for every problem). I also created a miniature banner animation, `banner.py`, in the beginning for visual appeal, as well as a summary ending footer, `end_text.py`. A demonstration of this manager script can be found [here](placeholder).

Some of the problems require input data to be read from a text file, and all of them read from the file `answers.txt` at least once. I've specified my own relevant file locations in the scripts, 

```
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_8_data.txt') as f:
```

for example. Of course, these locations need to be changed accordingly if you choose to run them on your own computer.

Additionally, the manager script (as well as all the individual problem scripts) has the following lines:

```
import sys
sys.path.insert(0, 'C:\\Users\\James Jiang\\Documents\\Project Euler\\problems')
```

which are necessary in order to import the individual problem scripts, which are located in a different directory. Once again, this path needs to be changed accordingly. 

As well as running the manager, you can run the problem scripts individually as well. There will still be a progress bar displaying the completion percentage and elapsed time. I've accounted for this via the lines 

```
if __name__ == '__main__':
	input()
```

for example.

If only the _functions_ I've used in solving the problems interest you, I've put them in a separate file, `functions.py`, and used it as a star import in the scripts where they are used. Included, of course, are appropriate docstrings.

As of now, only the first seventy-five problems in the archive have been solved and incorporated into the manager. More will be added upon completion.
