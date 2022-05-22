import os
import csv
#Set a path for this file to find the csv data file and call the file we are working with bank_csv
bank_csv=os.path.join("Resources","budget_data.csv")

#open the file from the path set above and call it csv_file
with open(bank_csv) as csv_file:
    #Create a csv reader by passing in the csv file we just "made" when we opened bank_csv
    #We will call it csv_reader as we will work with the reader 
    #A csv reader creates a list from the data from a csv file so we can loop or work with the rows using python
    #The delimeter tells the csv how to seperate the data in the file. In this case data is seperated with commas
    csv_reader=csv.reader(csv_file,delimiter=",")

    #Name header row so that the loop will not include this data later
    #Each time "next" is used, a row is iterated through the csv file
    #Since we use it once we will now be on row 2 when we start looping later
    csv_header=next(csv_file)
    
    #create a dictionary that will store the months and profit/loss for each month
    profit_loss = {}
     #loop through the csv to add to the dictionary
    for row in csv_reader:
        profit_loss[row[0]] = int(row[1])
    
    #count number of entries (months)
    months=len(profit_loss)

    #sum net profit/loss by totalling dictionary value for each month (key)
    netprof=0
    for key in profit_loss.keys():
        prof=profit_loss[key]
        netprof += prof

    change=[]
    for key in profit_loss.keys():
        change.append(profit_loss[key+1] - profit_loss[key])
    totchange=0
    for x in change:
        totchange+= x
    avchange = totchange/len(change)





