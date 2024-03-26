## Machine Learning Exercise 4 - Regularized Regression

For this exercise, you'll be attempting to predict the next-to-last ADHERENCE value per trip. 

Download the prepared dataset from [here](https://drive.google.com/file/d/1Rki8-zZTet8jaWDYwIOnW5EE4-8lYL_q/view?usp=sharing).
 
You've been provided variables containg the HOUR, and DAY_OF_WEEK, STARTING_ADHERENCE, and STARTING_DWELL time.

1. Fit a regular, unregularized linear regression model using ROUTE_ABBR, ROUTE_DIRECTION_NAME, OPERATOR, DAY_OF_WEEK, HOUR, STARTING_ADHERENCE, and STARTING_DWELL. How well does this model do? Inspect the coefficients for this model. What do you notice? 

2. Now, use ridge regression. How well does this model do compared to the regular linear regression model? How do the coefficients compare?

3. Finally, try a lasso regression model. Try adjusting the regularization strength (the alpha parameter) to see how it affects the model. Inspect both the performance and the non-zero coefficients.
