## Data Question 4: Nashville COVID-19 Violations

In this project, you will explore COVID-19 violations reported to hubNashville, Metro Nashville government's comprehensive customer service system. 

### Part 1:
Gather the dataset of hubNashville requests from https://data.nashville.gov/Public-Services/hubNashville-311-Service-Requests/7qhx-rexh. For this project, you should look at requests with Request Type of "COVID-19" and Subrequest Type of "COVID-19 Violations". Explore this dataset, looking at when and where these violations occurred.

### Part 2:
The file davidson_cases.csv contains the number of COVID cases in Davidson county per day from March 8 through October 29. Use this dataset to compare the trend for the number of cases over time to the number of reported violations. Feel free to add any additional data that you think might be useful.

### Part 3:
The Metro Public Health Department tracks COVID-19 clusters. The files `clusters.csv` and `clusters_by_type.csv` contain the tables of clusters as reported by [WSMV](https://www.wsmv.com/news/metro-health-releases-latest-covid-19-clusters/article_ef554e08-1558-11eb-b290-873345e174d7.html) along with the coordinates of the clusters. Can you find any connection between the reported COVID violations and subsequent COVID clusters?

### Part 4:
The dataset from data.nashville.gov includes geospatial information, which allows you to see where violations occurred geographically, but it does not provide information in regard to the specific businesses that were reported. In this part, you should explore the  businesses and types of businesses that have been reported. To attempt to answer this, you have been provided data from the [Google Places API](https://developers.google.com/places/web-service/overview). Each file is formatted as a json. The values are as follows:
* `mapped_location`: The mapped location from the hubNashville dataset
* `address`: The address from the hubNashville dataset
* `results`: The first five results from a Google Maps API nearbysearch, ranked by proximity to the Mapped Location. See https://developers.google.com/places/web-service/search#PlaceSearchResponses for more details on the fields in the results.

Take these results and use them to match as many violations as possible to a business. **Warning:** it will not be possible to match all violations to a business, and there will be ambiguities when trying to do this match, so do not spend all of your time on this task.
What do you find when you look into the types of businesses that have been reported for COVID violations?

Prepare a 10-15 presentation to showcase your findings.