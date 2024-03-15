## Machine Learning Exercise 2 - Introduction to Logistic Regression for Predictive Analytics

For this exercise, you'll be using the same wego dataset from last exercise. Your goal will be to predict whether a trip is on-time.

1. Create a new (target) variable, ON-TIME. We'll consider a trip to be on-time is it is no more than 6 minutes late (ADHERENCE >= -6) and is  no more than 1 minute early (ADHERENCE <= 1).

**Note:** Make sure that you perform a train/test split before fitting any models so that you can properly measure the performance of the model.

2. Fit a logistic regression model predicting the ADHERENCE using the ROUTE_ABBR and ROUTE_DIRECTION_NAME columns. How accurate is this model? How does it do in terms of precition and recall? What about ROC-AUC and calibration?

3. Now, try using the ROUTE_ABBR, ROUTE_DIRECTION_NAME, and OPERATOR. Does this improve the model? Note: you may need to increase the max_iter parameter of your model in order for it to converge.

4. Finally, the data you have been provided has an STARTING_ADHERENCE column, which contains the ADHERENCE at the beginning of the route. If you add this metric, does it improve the model?
