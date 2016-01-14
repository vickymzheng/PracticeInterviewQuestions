/*
The diabolical Professor Boolean has captured you and a group of your hapless rabbit kin as test subjects for his terrible 
experiments! You're not sure what his real plans are, but currently it seems he's trying to make everyone faster and 
smarter? He's exposing rabbit test subjects to novel chemicals, genetic manipulations, and pathogens; then measuring 
their completion time for various puzzles and exercises. Then again, there's a rumor he's developing a kind of 
zombie rabbit. You don't want to become a zombit!

Unfortunately, due to insubordination and laziness, Professor Boolean just "eliminated" the lab assistant tracking 
all data from this research. Now, he's forcing you to sort through the notes and find something useful from the chaos. 
You have no choice but to abide by your captors evil rules. For now.

Of the subjects that have survived, each has a distinct file, with anywhere from 1 to 100 measurements of completion time 
for the tests. The measurements from the before and after cases are listed separately, but the ordering has been mixed up. 
You have to figure out the degree of improvement (0% to 99%, rounded to the nearest whole number) based on the two lists of 
results.

For example, if the first list of times is [22.2, 46, 100.8] and the second list is [23, 11.1, 50.4] you would return 50, 
because the times got 50% shorter: the 22.2 entry improved to 11.1, the 46 improved to 23, and the 100.8 improved to 50.4. 
Even though the data points are in different order, each improves by the same amount.

Write a function answer(x, y) which takes two lists of floating point performance scores and returns the improvement 
percentage, rounded to the nearest integer.
*/

package com.google.challenges; 

public class Answer {   
    public static int answer(double[] x, double[] y) { 
        /*Since these are all times, I am assuming that none of them can be negative
        (You cannot do anything in negative time)
        We can learn the proper order of the lists by sorting them
        Then we can calculate the improvement of each list
        Later thought: Optimal sorting time is O(nlogn), we can solve this problem in O(n) by just finding the min.
        This works because the second set of times is a multiple of the first set
        Assuming x and y are the same length
        */

        double minX = x[0];
        double minY = y[0];
        int length = x.length

        for (int i = 0; i < length; i++) {
        	if (x[i] < minX) {
        		minX = x[i];
        	}
        	if (y[i] < minY) {
        		minY = y[i];
        	}
        }

        double percentImprovement = (1.0 - minY/minX) * 100; 
        return (int) Math.round(percentImprovement);

    } 
}