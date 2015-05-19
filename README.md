# base_addition
Python script to add non-negative integers in an aribtrary base from 2 to 36 inclusive

See usage statement, it's pretty straightforward: you specify a base between 2 and 36, inclusive, (default: 10) and any number of non-negative integers in that base to add together, and you will get the answer in that base.

The simple way to do addition in an arbitrary base is to convert the inputs to base-10, do the addition, and convert the answer back into the desired base.<br/>
This script does not do that.<br/>
Instead, it goes back to first principles and uses the basic adding algorithm that you learned in grade school ("carry the one", etc.) directly in the desired base (except insofar as your computer's arithmetic unit uses base 10).

As a result, this is not necessarily efficient for what it does.<br/>
But it was an exercise, and I am happy with the result.

You can use the script directly on the commandline, or you can import it as a module into another script (such as the base_multiply script that I've got in a sibling repo to this one).
