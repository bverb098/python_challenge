import os
import csv

election_csv=os.path.join("Resources","election_data.csv")
with open(election_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

    csv_header=next(csv_file)

    #create a dictionary with the main keys as voter IDs and a nested dictionary for each voter ID storing voter's County and Candidate
    #use csv data to create the dictionary
    election_data={}
    for row in csv_reader:
        election_data[str(row[0])]={}
        election_data[str(row[0])]["County"]=row[1]
        election_data[str(row[0])]["Candidate"]=row[2]
           
    #total votes cast = 1 per voter ID. Therefore count number of keys in the election_data dictionary
    #store the answer as a variable
    total_votes=int(len(election_data.keys()))

    #if a candidate recieved a vote their name will be in the nested dictionary
    candidate_list=[]
    for i in election_data.values(): #loop thru each Voter ID key
       candidate_list.append(i["Candidate"])
    
    #remove duplicates from the candidate list by converting it into a set
    candidate_set = set(candidate_list)
    #conver set back into a list to have a list of candidates who received votes
    short_candidate_list=list(candidate_set)

    #make a dictionary to store vote count and percent of vote received for each candidate
    winners={}
    #compare each candidate from the short list to how many times their name came up in the full list
    for x in short_candidate_list:
        v_tally=int(candidate_list.count(x)) #store in variable number of votes for the candidate in the loop
        v_percent=float(v_tally/total_votes) #store in variable the number of votes as a percent of total votes
        winners[x]={} #create a nested dictionary for each candidate
        winners[x]["Vote Count"]=v_tally #store in nested dic for candidate their total votes
        winners[x]["Vote Percent"]=v_percent #store in nested dic for dandidate their percent vote

    #re order the dictionary so that the candidates are in order of the number of votes
    sorted_winners=dict(sorted(winners.items(), key=lambda x:x[1]['Vote Count'], reverse=True))

    #print the analysis
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")
    for x in sorted_winners.keys():
        cname=x
        cvotes=winners[x]["Vote Count"]
        cpercent=winners[x]["Vote Percent"]
        print(f"{cname}: {cpercent:.2%} ({cvotes})")
    print("--------------------------")
    wname = next(iter(sorted_winners))
    print(f"Winner: {wname}")