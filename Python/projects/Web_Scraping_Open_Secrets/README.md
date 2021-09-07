# An Analysis of Political Contributions During the 2020 House of Representatives Election

### Part 1: Preparing Election Results
Start with the U.S. House election results from the MIT Election Data and Science Lab (https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IG0UN2).
1. Filter the results down to just the 2020 election.
2. Combine the results together for fusion ticket candidates so they only have one row. (For example, Lee M. Zeldin in New York's 1st district appears three times across three different parties).
3. Create a column giving the rank of each candidate within their district in terms of number of votes received.
4. Create another column giving the margin of victory within each district (the difference between the percentage of votes received by the first and second place candidates).
5. Export the resulting DataFrame as a csv.

### Part 2: Scraping Campaign Contributions Data
In this part, you will obtain as much data as you can on the campaign contributions received by each candidate. This data is avaiable through the website https://www.opensecrets.org/.
1. Start by scraping the data for Tennessee's 2nd District, which is available at https://www.opensecrets.org/races/candidates?cycle=2020&id=TN02&spec=N.
    * Make a DataFrame showing, for each candidate, the candidate's name, state, district, whether they were an incumbent, total amount spent, and contributions by source.
    * Create a calculated column giving to total contributions received per candidate.
2. Once you have working code for Tennessee's 2nd District, expand on it to capture all of Tennessee's districts.
3. Once you have working code for all of Tennessee's districts, expand on it to capture all states and districts.
4. Export the results to a csv.

### Part 3: Merging and Analyzing
1. In a new notebook, import the csv files you created in the previous two parts.
2. Merge the two datasets together.
3. Bonus: You may notice that you are unable to match some candidates based on the way their name is given in the MIT dataset vs on OpenSecrets. For example, John Sarbanes appears as "JOHN P. SARBANES" in the MIT data and "JOHN SARBANES" on OpenSecrets. Use the _fuzzywuzzy_ library to resolve as many of these as you can.
4. Explore the relationship between contributions received and whether a candidate won their election. Here are some example questions to get you started:
    * How frequently does the candidate who received more contributions win?
    * Is there a relationship between total contributions and how close a race is in terms of margin of victory?
    * Is there a relationship between how much _more_ a candidate raised (in either absolute or relative terms) and their margin of victory or whether they won?

Prepare a short presentation to showcase your findings.