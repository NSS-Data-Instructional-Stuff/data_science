## Machine Learning Exercise 3 - K-Means Clustering

For this exercise, you'll be working with a cleaned up version of the full WeGo data, meaning that you have all rows for each trip.

Your goal in this exercise is to find groupings of simlar time points (as identified by TIME_POINT_ABBR).

1. Read in the csv into a DataFrame named  `wego`. First, we need some features to compare time points. One strategy for this is to try and create some features that measure characteristics about the distribution of, for example, adherence values. Use the following code to find the 0.5, 0.25,0.5, 0.75, and 0.95 quantiles of ADHERENCE values for each stop.

```
time_point_quantiles = (
    wego
    .groupby('TIME_POINT_ABBR')
    ['ADHERENCE']
    .quantile([0.05, 0.25, 0.5, 0.75, 0.95])
    .reset_index()
    .rename(columns = {'level_1': 'quantile'})
    .pivot_table(index = 'TIME_POINT_ABBR', 
                 columns = 'quantile', 
                 values = 'ADHERENCE')
)
```

What is each step doing in this code?

2. When performing k-means clustering, we usually want to standardize our features so that we can compare across multiple dimensions. This means that we are going to convert our original values into z-scores. Create a Pipeline object whose first step employs a StandardScaler to standarize the features and whose second step performs KMeans clustering with 2 clusters.

3. How many points end up in each cluster? How do the points in each cluster compare?

4. Try a range of different values for the number of clusters and choose one which you think is appropriate. Inspect the results and compare the resulting clusters.

**Bonus:** Perform clustering on operators (identified by the OPERATOR variable). You'll need to create some featues on which to compare operators. Think about what types of aggregate values you could calculate which might be useful for this task.
