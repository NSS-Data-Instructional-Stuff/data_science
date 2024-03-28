## Machine Learning Exercise 5 - Decision Tree Models

For this exercise, use the same dataset from the last exercise (which can be downloaded [here](https://drive.google.com/file/d/1Rki8-zZTet8jaWDYwIOnW5EE4-8lYL_q/view?usp=sharing)).

1. Create a new (target) variable, ON-TIME. We'll consider a trip to be on-time is it is no more than 6 minutes late (ADHERENCE >= -6) and is  no more than 1 minute early (ADHERENCE <= 1).

2. Fit a decition tree model predicting ON-TIME using the ROUTE_ABBR, ROUTE_DIRECTION_NAME, OPERATOR, DAY_OF_WEEK, HOUR, STARTING_ADHERENCE, and STARTING_DWELL columns. How accurate is this model? How does it do in terms of precition and recall? What about ROC-AUC and calibration?

3. Try a shallow decistion tree. How does it compare to an unrestricted decision tree model?

4. How does a random forest or gradient boosting model compare? What features do this models place high importance on?
