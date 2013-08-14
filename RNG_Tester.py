# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:41:19 2013

@author: sunda
"""
import random



def randomTester(generatedNumbers, interval):
    """Veletlenszam generator vizsgalata

    Usage: randomTester(generatedNumbers, interval)
    generatedNumbers(int) = Hány számot generáljunk?
    interval(int) = Hány lehetőség legyen
    Example: randomTester(437,10)"""
    
    dictCases={}

    for j in range(interval):
        dictCases[j]=0

    #Véletlenszámok legenerálása


    for i in range(generatedNumbers):
        myRandom = random.randint(0,interval-1)    
        dictCases[myRandom] += 1

    #eredmények kiírása
    print "\nVéletlenszám-generátor vizsgálat eredményei:"
    print "\n"+str(generatedNumbers)+" db számgenerálás történt"
    print "Intervallum: 0 - " + str(interval-1) + "\n"
    print "Eredmények:"
    for k in range(interval):
        percentOfResults =float(dictCases[k])/float(generatedNumbers)*100
        print str(k) + " : " +str("%0.0f" % (dictCases[k],))+" db -> "+str(percentOfResults) + "%"

randomTester(100,10)