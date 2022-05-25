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

    #create a list of all the profits/lossses only by extracting each value from each key of our dic
    profitonly=[profit_loss[key] for key in profit_loss.keys()]

    #create a list using the list above. This time it is a list of the change in profit from each month
    #it has to start from index 1 as there is no change to calculate from index 0
    #use len function on list of profits to find the last entry number in the list to iterate to
    profchange=[profitonly[i]-profitonly[i-1] for i in range(1, len(profitonly))]
    avchange=sum(profchange)/len(profchange)
    formatavchange="{:.2f}".format(avchange)

    #each element (n) in the profchange list corresponds to element (n+1) of the profit_loss dictionary
    # return the index numbers of the max and min values in the profchange list and then return corresponding key name

    #create list of key names from profit_loss to access them by index
    keys_list=list(profit_loss)
    #max profit increase:
    maxincreaseamount = max(profchange)
    #index of max increase stored as variable
    k = profchange.index(max(profchange))
    #return the max increase month
    maxincreasemonth = keys_list[k+1]

    #max profit decrease
    maxdecreaseamount = min(profchange)  
    #index of max profit decrease stored as variable
    l = profchange.index(min(profchange))
    #return max decrease month
    maxdecreasemonth = keys_list[l+1]

    with open(os.path.join("Analysis","Analysis.txt"), "w") as a:
        print("Financial Analysis",file=a)
        print("-----------------------",file=a)
        print(f"Total Months: {months}",file=a)
        print(f"Total: ${netprof}",file=a)
        print(f"Average Change: ${formatavchange}",file=a)
        print(f"Greatest Increase in Profits: {maxincreasemonth} (${maxincreaseamount})",file=a)
        print(f"Greatest Decrease in Profits: {maxdecreasemonth} (${maxdecreaseamount})",file=a)

    print("Financial Analysis")
    print("-----------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${netprof}")
    print(f"Average Change: ${formatavchange}")
    print(f"Greatest Increase in Profits: {maxincreasemonth} (${maxincreaseamount})")
    print(f"Greatest Decrease in Profits: {maxdecreasemonth} (${maxdecreaseamount})")

