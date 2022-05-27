# Election_Analysis_Challenge
---
## Overview of Project
The election commision has requested an audit. We need to help Seth and Tom complete the audit results by adding some data including:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

### Purpose
The purpose of this analysis is to extract certain candidate and state information into a text file for the election commision that has requested an audit.

## Analysis

The python script used for the analysis is:

[PyPoll_Challenge.py](https://github.com/ClaudAMC/Election_Analysis_Challenge/blob/main/PyPoll_Challenge.py)

The text file the analysis is printed to is:

[election_analysis.txt](https://github.com/ClaudAMC/Election_Analysis_Challenge/blob/main/analysis/election_analysis.txt)

### Election-Audit Results

During this analysis we hoped to awnser a 5 questions:

1. How many votes were cast in this congressional election?

In the image below we can see the code used to calculate this variable.

![Q1 Code](https://user-images.githubusercontent.com/103139895/170616470-3e243250-3076-4df5-b0c8-9b099e86544d.PNG)

This is then printed into the text file as seen in the image below.

![Q1 txt file](https://user-images.githubusercontent.com/103139895/170616475-b78eeb11-06bc-45bd-944c-f52fceae1ff2.PNG)

We can see from this that the total votes cast in the election was 369,711.

2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

In the 2 images below we can again see the code used to find both the number of votes per county and the percentage of votes per county.

![Q2 Code](https://user-images.githubusercontent.com/103139895/170617019-90b838e6-2861-4057-9aeb-6959816bdf75.PNG)

![Q2 Code prt 2](https://user-images.githubusercontent.com/103139895/170617334-1a6bb68e-f17c-443f-b71e-63cf3cbc260c.PNG)

This is then printed onto the text file as seen below:

![Q2 txt file](https://user-images.githubusercontent.com/103139895/170617024-85a468fe-b238-457b-9890-acb28b9f492a.PNG)

From here we can see the number of votes and percentage of votes in a three counties (Jefferson, Denver, and Arapahoe).

3. Which county had the largest number of votes?

The code below shows how I extract which county had the largest number of votes.

![Q3 Code](https://user-images.githubusercontent.com/103139895/170617757-4eb8a80c-a6a8-44bf-8642-bc5a7a127c83.PNG)

This was the printed onto the text file as seen below.

![Q3 txt file](https://user-images.githubusercontent.com/103139895/170617764-ea43ee57-cf24-4e89-a5eb-f59d7419e628.PNG)

We can see here that the county with the largest number of votes was Denver.

4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

The code below demonstrates how the candidate votes and the candidates percentage of total votes was calculated and extract form the data.

![Q4 Code](https://user-images.githubusercontent.com/103139895/170618163-4ef674e6-75a4-46c2-aedd-115682663185.PNG)

![Q4 Code prt 2](https://user-images.githubusercontent.com/103139895/170618172-42c6bc67-d330-409c-8b1d-df309c0ab28d.PNG)

Here we can see the output ontot the text file showing our analysis results.

![Q4 txt file](https://user-images.githubusercontent.com/103139895/170618233-ecaeaff8-a73c-46d6-b820-0ce82346b2b3.PNG)

From this we see the breakdown of how the votes were distributed between each of the candidates (Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane).

5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

In the code below we can see how the winning candidate was found.

![Q5 Code](https://user-images.githubusercontent.com/103139895/170618765-4d944742-3251-4cdb-95fe-eb660bda887d.PNG)

In the image below we can see the results printed onto to the text file.

![Q5 txt file](https://user-images.githubusercontent.com/103139895/170618769-c1db862e-13ae-4ff1-8112-fbab4dc23338.PNG)

Here we see that the winning candidate was Diana DeGette with 272,892 votes meaning they had 73.8% of the vote.

### Election-Audit Summary

This code can be applied to any csv file with the same format as the one used for this analysis. This mean we can add more counties and more candidates if desired.

One way to modify this code would be to apply it to states; in this case we could a column with the states to the csv and we can analyze the data by looking at each state individually and its counties or by forgoing the counties all together and only looking at the state wide data and its candidates. here we would use a similar code but tailor it to look at the state as opposed to county or candidate.

Another way to modify the code would be to look more closely at the regions within the county, the voting areas. With this again we would simlarly adapt the code to each voing area and then extract the number of votes for each one; this can give us an idea of which regions within the counties people are voting from. This might be particularly important for the counties that dont have a big turnout. The committe could take a look at what is different about this high turnout areas compared to the low turnout areas and in doing so find ways to improve voter turnout for the next election.

