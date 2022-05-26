import os
import csv
from time import strftime
from tokenize import Ignore

from attr import field, fields

employee_csv=os.path.join("employee_data.csv")
with open(employee_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

    csv_header=next(csv_file)
    employee_data = {}
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',}

    # I did not do a step where I convert the date value from a string to an actual date object
    for row in csv_reader:
        employee_data[row[0]]={}
        employee_data[row[0]]["First Name"]=str(row[1].split()[0])
        employee_data[row[0]]["Last Name"]=str(row[1].split()[1])
        employee_data[row[0]]["DOB"]=str(row[2].split("-")[1])+"/"+str(row[2].split("-")[2])+"/"+str(row[2].split("-")[0])
        employee_data[row[0]]["SSN"]="***-**-"+str(row[3].split("-")[2])
        employee_data[row[0]]["State"]=us_state_abbrev[row[4]]

    
    fields=("Emp ID", "First Name", "Last Name", "DOB","SSN","State")
    with open("NewData/new_employee_data.csv","w") as csvfile:
        
        writer=csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for k in employee_data:
            writer.writerow({field: employee_data[k].get(field) or k for field in fields})