make sure to:
- [ ] upload original data sets
- [ ] upload analyzed excel files to show work to derive data insights
- [ ] check [github template](https://github.com/jhu-business-analytics/midterm-project-template)

# How Voter Turnout (for Older Adults) in the 2020 Election Could Be Impacted by the COVID-19 Pandemic in Maryland
It is vital that we understand the implications of the pandemic on the election to best know what measures can and should be taken to adapt voting systems to protect the most vulnerable and allow as many eligible voters to participate under the circumstances.
// TODO when done at end 
* 2-3 sentences that explain your “business question” and some high-level findings and suggestions. Tell the reader a little bit about your business question, why this is important, a high-level finding, and the future implicateions of your findings. Make this short and captivating so that the user wants to continue reading about this topic and what you’ve done. 

**Original Question: //TODO**

## Background
As the 2020 National Election approaches and the novel coronavirus continues to spread across the country, COVID-19 presents many challenges to voting efforts beyond the already existing factors. Measures to prevent the further spread of COVID-19 have led to cancelled events of all kinds- from sports seasons to campaign rallies, concerts to canvassing. To date, 16 states have already restructured or rescheduled their presidential primaries [(1)](https://www.nytimes.com/article/2020-campaign-primary-calendar-coronavirus.html).

Unlike the primary elections, however, the date of the general election is set by federal law which means that postponing it would not only be a tremendous political ordeal, but would also potentially result in social upheaval. However threatening this pandemic, we cannot let it interrupt out democratic process and disenfranchise voters. While it is still unclear how the United States will find itself in just a matter of months, we must start preparing now for what is sure to be an unprecedented and logistically challenging general election. 

In 2016, only 60% of eligible voters participated in the US presidential election [(2)](http://www.electproject.org/2016g). While total voter turnout for Maryland in the 2016 general election was 72%, voter turnout in Baltimore City was only slightly better than the national average at 62% [(3)](https://elections.maryland.gov/elections/2016/turnout/general/Official%20by%20Party%20and%20County.pdf).

Older adults and those with underlying conditions are at higher risk for severe illness as a result of COVID-19 [(4)](https://www.cdc.gov/coronavirus/2019-ncov/need-extra-precautions/people-at-higher-risk.html). This is particularly concerning when considering voter turnout because older Americans are historically much more likely to vote. In 2016, citizens 65 years and older voted at higher rates (70.9%) than 45-64 year olds (66.6%), 30-44 year olds (48.7%), and 18-29 year olds (46.1%) [(5)](https://www.census.gov/newsroom/blogs/random-samplings/2017/05/voting_in_america.html).
Maryland citizens over 65 years old are even more likely to vote  with 2016 turnout reaching 76.7% [(6)](https://elections.maryland.gov/press_room/2012_stats_general/2012_general_voter_turnout_by_age.pdf). 

In Maryland, citizens who are registered to vote can vote for the general election in one of three ways:
* Early Voting, in-person between October 22nd and 29th between 8am-8pm.
* Absentee ballot, mailed ballot by election day. 
* Election Day, in-person at assigned polling place. 
With a state-wide shelter-in-place and social distancing guidelines of keeping people 6ft apart, in-person voting will most likely decrease which places more importance on mail-in absentee ballots. We've already seen this happen in several primaries [(7)](https://www.npr.org/2020/03/16/815504537/voting-amid-coronavirus-what-you-need-to-know).


## Solution

### 2016 Presidential Election Analysis

To analyze what voting methods citizens across Maryland were more likely to use in the 2016 General Election, we will be using [Maryland's Official Turnout Statistics for the 2016 General Election in Maryland by Party and Precinct](https://github.com/CamilaCamacho/baltimore_voter_turnout/blob/master/Official%20by%20Party%20and%20Precinct.csv).
Excel file with analyzed data found [here](https://github.com/CamilaCamacho/baltimore_voter_turnout/blob/master/MD%20Vote%20Method%20Frequency%20Analysis.xlsx). 

Maryland has a total of 1,989 precincts and the number of eligible voters and turnout percentage for each precinct varies widely. The following histograms show the popularity of different methods of voting across all Maryland precincts. 

#### Frequency of Voting on Election Day
Across all precincts in Maryland, there is a wide distribution of number of votes on Election Day. For 2016, about 17% of precincts received between 800 to 1,000 votes, 48% receivied less than 800 votes, and 35% received more than 1,000 votes.
![Polls Histogram](https://github.com/CamilaCamacho/baltimore_voter_turnout/blob/master/histograms/Polls%20Histogram.png)

#### Frequency of Early Voting 
For Early Voting period of October 22nd-29th 2016, there was an average number of 440 votes collected per precinct. This right-skewed histogram shows that about 74% of precincts received less than 600 votes during Early Voting with about 28% of precincts receiving between 0 to 200 votes. This shows that Early Voting is not all that popular across Maryland. 
![Early Voting Histogram](https://github.com/CamilaCamacho/baltimore_voter_turnout/blob/master/histograms/Early%20Voting%20Histogram.png)

#### Frequency of Absentee Voting
Throughout Maryland, absentee voting was very uncommon in the 2016 election. About 90% of precincts reveived between 0 and 200 votes, only 1 precinct received more than 600 absentee ballots, and there were no precincts that reveived more than 800 absentee ballots. When we break this down further, we see a right-skewed histogram showing that 68% of precincts received less than 100 absentee ballots. 
![Absentee Histogram](https://github.com/CamilaCamacho/baltimore_voter_turnout/blob/master/histograms/Absentee%20Histogram.png)
![Detailed Absentee Histogram](https://github.com/CamilaCamacho/baltimore_voter_turnout/blob/master/histograms/Absentee%20Histogram%20(Detailed).png)

#### Geo-Map of Voter Turnout
Out of curiosity, we also wanted to look at voter turnout to provide context on our analysis. The data presented here is by county for the 2016 General Election. As can be seen, St. Mary's County and Howard County has amongst the highest rate of voter turnout. Baltimore County and Talbot County had some of the lowest.
![Voter Turnout Map](https://github.com/CamilaCamacho/baltimore_voter_turnout/blob/master/Figures/VoterTurnout.png)

### Impact of COVID-19 in Maryland
Given recent trends, it is also extremely important to place our analysis within the context of the COVID-19 pandemic. As this is a highly unprecedented time, it is likely that much of the factors involved in voter turnout will be even more impacted. Specifically, this is difficult for the older population, age groups above 65 years old. 

#### Geo-Map of Percent Infected by Corona Virus
At a first glance, Maryland is certainly better than many other states in terms of limiting the community-wide spread of corona virus amongst its counties. From the map, it can be noted that Queen Anne's and Talbot Counties have amongst the highest percent of cases as 04/20/2020 with the highest being about 0.4% of the total population of the county, irrespective of age, gender, or race. 
![Percent Infected Map](https://github.com/CamilaCamacho/baltimore_voter_turnout/blob/master/Figures/PercentInfected.png)

#### Geo-Map of County Risk Number
From basic logical reasoning, it can be ascertained that COVID-19 certainly impacts the older age group of people above 65 years old. To assess how COVID-19 would impact the upcoming election, we wanted to see for each county what the impact would be given its population of citizens above 65 and percent of infected population. Amongs all of Maryland, we normalized both of these value and took the product to obtain a risk metric. Here, a higher value of the risk metric illustrates a county which has higher relative number of cases and higher relative population of citizens above 65 years old. The county with the highest risk number here was Talbot County, followed by Queen Anne's County and Baltimore County. 
![Risk Map](https://github.com/CamilaCamacho/baltimore_voter_turnout/blob/master/Figures/RiskNumber.png)

## Future Suggestions
* Now that you told us what needs to happen for your problem as a result of your analysis, how does this come into play in the next 6 months? Year? Ten years? 
* What would you recommend happens in this industry/situation from an organizational, policy, leadership, or some other type of shift or pivot? This is similar to a conclusion, but also gives a clear call-to-action to the designated group/people who can do something about your original business question. This section should be about one paragraph.
