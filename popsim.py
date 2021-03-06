#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:32:45 2019

@author: stephencranney
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 17:43:49 2016

@author: Stephen
"""
# popsim python
#Create matrix (of integers, not tuples)

import numpy as np

simulation_duration_years= 55
simulation_duration_months= simulation_duration_years * 12 

offspring=0
month=1
monthly_conception_probability= .2
pregnancy_miscarriage_probability= .25 #Double check these numbers with the book
average_miscarriage_duration= 3 # 3 months?
pregnancy_length= 9
postpartum_infertility=12 
finalchildbearingage= 40*12
deathage= 89*12
infertile_age= 40*12


number_of_women=4 #Have to do this one by hand because have to assign specific values. 
womanage_0=7
womanage_1=5
womanage_2=3
womanage_3=0

repeat_number=100

offspring_simulation= np.zeros(repeat_number,) 

matrix= np.zeros((number_of_women, simulation_duration_months)) 
#for i in range(0, (number_of_women-1)): #  At some point figure this out so I don't have to do it by hand. 
    #matrix[i,0]="womanage_"+i


#x[1][2] # 2nd row, 3rd column 


matrix[0,0]=womanage_0*12
matrix[1,0]=womanage_1*12
matrix[2,0]=womanage_2*12
matrix[3,0]=womanage_3*12

young_infertile= 23*12


#Populate matrix ages first, then things can be taken out, etc on the way.

#Put simulate code in here and at end once I figure out how to name 
#http://stackoverflow.com/questions/10133294/execute-python-script-multiple-times
#Figure out how to do if value error, jump out of this loop and go to next higher order loop. 
runs=range(repeat_number)
for y in runs: 
#Then after I have it, make an instagram

#REMEMBER TO TAKE OUT SONS IF THIS IS A SELF-SUPPORTED POPULATION, IF JUST CALCULATING TOTAL DESCENDANTS THEN LEAVE THEM IN. 

    for i in range(number_of_women):
        for k in range(1, (simulation_duration_months)):
            matrix[i,k]= matrix[i,(k-1)]+1 #Add one to age
        
    #np.random.seed(1) # Set the seed to 1 for now for debugging
        
    for i in range (0, 1000): #Put in number of possible people, high estimate. Later on try to figure out while stopping condition for as long as there's a non-dead value or non-infertile value keep running. Either way, it should terminate in an error once it doesn't fit the array that is based on the time amount. 
        for k in range(1,simulation_duration_months): #Start the one after 0 so that it doesn't change the first one. 
            if matrix[i,k]< infertile_age and matrix[i,k]>young_infertile:  # Don't have to make -500 explicit, it's already "young infertile"
                except IndexError: 
                   offspring_simulation[y]= offspring 
                else: 
                    conception = np.random.binomial(1, monthly_conception_probability, size=None)
                    if conception==1:
                        miscarriage = np.random.binomial(1, pregnancy_miscarriage_probability, size=None)
                        if miscarriage==1:
                            for s in range(average_miscarriage_duration):
                                if (k+s)< simulation_duration_months: #Adding this part prevents it from terminating early when it refers to a cell that's off the map
                                    matrix[i,k+s]= -300
                        if miscarriage==0:
                            offspring= offspring+1
                            newrow=np.zeros(simulation_duration_months)
                            for q in range(k, simulation_duration_months-1):
                                newrow[q+1]=newrow[q]+1
                            matrix = np.vstack((matrix,newrow))
                            for z in range(pregnancy_length+postpartum_infertility):
                                if (k+z)<simulation_duration_months:
                                    matrix[i,k+z]= -500
                            
# It will naturally end by aborting once it tries to reach for that child # that doesn't exist. But wait, naturally ending this way makes it so that I can't do the simulation multiple times! Maybe later figure out the if, error command, go out of that loop. 
                          
import pandas as pd 
matrix_df = pd.DataFrame(matrix)
matrix_df.to_csv("C:\Users\Stephen\Desktop", sep='\t')
matrix_df.to_csv("C:\Users\Stephen\Desktop.csv")
                    
matrix[1,]

matrix_year= matrix/12
matrix_year[:,-1] # Get the last column (who is alive at the end of the period, total size)