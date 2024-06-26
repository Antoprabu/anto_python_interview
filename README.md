# Frequency Calibration
# Part 1 - Find the Frequency
We are going to be calibrating a tiny device. The device shows a sequence of changes in frequency (your program's input). A value of +6 means the current frequency increases by 6; a value of -3 means the current frequency decreases by 3.

For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

Current frequency 0, change of +1; resulting frequency 1.
Current frequency 1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency 2.
Current frequency 2, change of +1; resulting frequency 3.
In this example, the resulting frequency is 3.

Here are other example situations:

+1, +1, +1 results in 3
+1, +1, -2 results in 0
-1, -2, -3 results in -6

Starting with a frequency of zero, 
what is the resulting frequency 
after all of the changes in frequency have been applied?

# Part 2 - Calibrate the frequency
Now that we've determined how to calculate a frequency, 
we need to calibrate our device. 
To calibrate the device, 
you need to find the first frequency it reaches twice.

For example, using +1, -2, +3, +1 again, the device would loop as follows:

 Current frequency 0, change of +1; resulting frequency 1.
 Current frequency 1, change of -2; resulting frequency -1.

Current frequency -1, change of +3; resulting frequency 2.
Current frequency 2, change of +1; resulting frequency 3.
(At this point, the device continues from the start of the list.)
Current frequency 3, change of +1; resulting frequency 4.
Current frequency 4, change of -2; resulting frequency 2, 
which has already been seen.
In this example, the first frequency reached twice is 2.

Note that your device might need to repeat 
its list of frequency changes many times 
before a duplicate frequency is found, 
and that duplicates might be found 
while in the middle of processing the list.

Here are other examples:

+1, -1 first reaches 0 twice.
+3, +3, +4, -2, -4 first reaches 10 twice.
-6, +3, +8, +5, -6 first reaches 5 twice.
+7, +7, -2, -7, -4 first reaches 14 twice.

What is the first frequency your device reaches twice?

