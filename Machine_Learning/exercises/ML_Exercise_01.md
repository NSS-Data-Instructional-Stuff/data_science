## Machine Learning Exercise 1 - Introduction to Regression for Predictive Analytics

For this exercise, you've been provided a dataset derived from the full WeGo headway dataset. Your goal is to see how well a model can predict the ADHERENCE value.

Note that this dataset is a condensed version of the dataset that you've worked with before. Each trip has been condensed to a single row, identified by the ID column, a combination of the original CALENDAR_ID and TRIP_ID columns and where the ADHERENCE value is ADHERENCE value for the next-to-last stop.

For example, the original data, the first trip 

|    |               ID |   CALENDAR_ID |   TRIP_ID |   ADHERENCE |   TRIP_EDGE |
|---:|-----------------:|--------------:|----------:|------------:|------------:|
|  0 | 120230801_345104 |     120230801 |    345104 |   -2.13333  |           1 |
|  1 | 120230801_345104 |     120230801 |    345104 |   -2.45     |           0 |
|  2 | 120230801_345104 |     120230801 |    345104 |   -0.933333 |           0 |
|  3 | 120230801_345104 |     120230801 |    345104 |    6.28333  |           2 |

Has been reduced to just the value for the next-to-last stop:

|    |               ID |   CALENDAR_ID |   TRIP_ID |   ADHERENCE |   TRIP_EDGE |
|---:|-----------------:|--------------:|----------:|------------:|------------:|
|  2 | 120230801_345104 |     120230801 |    345104 |   -0.933333 |           0 |


**Note:** Make sure that you perform a train/test split before fitting any models so that you can properly measure the performance of the model.

1. Fit a linear regression model predicting the ADHERENCE using the ROUTE_ABBR and ROUTE_DIRECTION_NAME columns. Measure the performance of the model using the R^2 and mean absolute error metrics. Interpret the meaning of each metric.

2. Now, try using the ROUTE_ABBR, ROUTE_DIRECTION_NAME, and OPERATOR. Does this improve the model? Warning: Your model may perform very poorly once you add the OPERATOR. If so, this is likely caused because some operators have very few observations. One option to correct this is to assign an "Other" (or -999999) value to operators with few observations. 

3. Finally, the data you have been provided has an STARTING_ADHERENCE column, which contains the ADHERENCE at the beginning of the route. If you add this metric, does it improve the model? Is this of any practical use?

**Bonus Questions:** 
* How well does a constant-only model perform compared to the models above?
* For this exercise, you were provided data that was already prepared by condensing each trip into one row. Go back to the original dataset and perform the preparation, creating an ID column and keeping only the next-to-last ADHERENCE value.