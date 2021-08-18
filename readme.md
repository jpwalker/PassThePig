# Pass the Pig Game Simulation

Two versions of a program to compute the expectation score value for a strategy where you keep rolling until your score is higher than a particular value or you roll the losing value. This was inspired by the Numberphile video, [The Math of Being a Pig - Numberphile](https://www.youtube.com/watch?v=ULhRLGzoXQ0). The code reproduces the same graph shown in the video for larger range of possible scores.

## Requirements
* Numpy
* Matplotlib

## Files
* passThePig.py - Single threaded program.
* passThePig_multi.py - Mutli-threaded(process?) program. Note: This program may be further optimized by playing with the chunksize in the map function.

On my Intel i5-2435M CPU laptop the single and multi-threaded versions took 278.388219925 and 146.828163685 s, respectively.