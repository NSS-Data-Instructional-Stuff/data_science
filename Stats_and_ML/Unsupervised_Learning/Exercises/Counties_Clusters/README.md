# Unsupervised Learning Exercise

In this exercise, you will apply unsupervised learning techniques to a dataset of all US counties. This dataset comes from the [2018 County Health Rankings](https://www.countyhealthrankings.org/explore-health-rankings/rankings-data-documentation). 

1. How many missing values are there per variable? You might want to think about dropping some of the columns that have a large number of missing values.

2. PCA clustering do not work if you have observations with missing values. After choosing which variables to drop, you'll need to decide what to do with any counties that are still missing values. The easiest solution is to drop those observations. Drop any rows that contain missing values. **Bonus:** If time allows, come back to this part and try imputing missing values to see if it changes your final result.

3. Apply PCA to the remaining data. How much of the overall variance do the first two principal components capture? How many are needed to capture 80% of the variance? 90%?

4. Look at the scatterplot of the projection using the first two principal components. Do any observations stand out? Figure out which counties the observations belong to.

5. Apply k-means clustering to the dataset. Make sure that you scale the data before clustering. Look at a scree plot to determine a good number of clusters to use. 

6. Take a closer look at the clustering on the Tennessee counties. Do the results you get make sense?

7. Look at the average values of your variables per cluster. What do you notice?