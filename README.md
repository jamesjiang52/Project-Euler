# Project Euler

Solving math problems using Python 3.6, using a plethora of external libraries. Problems are available [here](https://projecteuler.net/archives).

Since writing scripts to solve those problems didn't feel quite enough, I also created a manager script, `_project_euler.py`, that imported and ran the scripts in sequence and also displayed progress information (this required instantiating a `Progress()` class for every problem). I also created a miniature banner animation, `banner.py`, in the beginning for visual appeal. A demonstration of this manager script can be found [here](placeholder).

Some of the problems require input data to be read from a text file, and all of them read from the file `answers.txt` at least once. I've specified my own relevant file locations in the scripts, 

```
with open('C:\\Users\\James Jiang\\Documents\\Project Euler\\data\\problem_8_data.txt') as f:
```

for example. Of course, these locations need to be changed accordingly if you choose to run them on your own computer.

As of now, only the first fifty problems in the archive have been solved and incorporated into the manager.
