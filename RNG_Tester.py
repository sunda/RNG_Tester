# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:41:19 2013

@author: sunda
"""
import random



def RNGTester(generatedNumbers, interval):
    """Testing Random Number Generator

    Usage: randomTester(generatedNumbers, interval)
    generatedNumbers(int) = How many numbers generate?
    interval(int) = Interval of Naumers
    Example: randomTester(437,10)"""
    
    dictCases={}

    for j in range(interval):
        dictCases[j]=0

    #Generated Random Numbers


    for i in range(generatedNumbers):
        myRandom = random.randint(0,interval-1)    
        dictCases[myRandom] += 1

    #print values
    print "\nValues of RNG teszt:"
    print "\nGenerated "+str(generatedNumbers)+" number."
    print "Interval: 0 - " + str(interval-1) + "\n"
    print "Values:"
    for k in range(interval):
        percentOfResults =float(dictCases[k])/float(generatedNumbers)*100
        print str(k) + " : " +str("%0.0f" % (dictCases[k],))+"x -> "+str(percentOfResults) + "%"

"""
Example:
RNGTester(100,10)
"""