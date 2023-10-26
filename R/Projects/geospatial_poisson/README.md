# Analyzing Aggravated Burglaries in Davidson County

### Part 1 - Data Preparation

You've been provided three datasets for this project:
* burglaries_2023.csv: Contains data on the aggravated burglary incidents in Davidson County. This was obtained from https://data.nashville.gov/Police/Metro-Nashville-Police-Department-Incidents/2u6v-ujjs.
* census.csv: Census tract level data on population and median income. This was obtained from the US Census American Community Survey.
* DC: A shapefile containing Davidson County census tracts

Perform a spatial join to determine the census tract in which each burglary occurred. Hint: You may want to make use of the [st_as_sf function](https://r-spatial.github.io/sf/reference/st_as_sf.html) in order to convert the burglaries data into an sf object.


After performing the spatial join, merge in the census data. **Note:** Make sure that the final dataset contains all census tracts.

### Part 2 - Exploratory Analysis

Perform some exploraty analysis on your prepared dataset.

Aggregate the data by census tract. **Warning:** each incident can appear multiple times if there are multiple victims, so be sure that you aren't double-counting any incidents. 

Which census tract had the highest number of burglaries? Which census tract had the highest number of burglaries per 1000 residents? 

We're interested in the relationship between median income and number of aggravated burglaries, so examine those variables on their own and together to see what you can find. You may want to perform additional calculations, create plots, etc.

### Part 3 - Statistical Modeling

Fit a Poisson regression model with target variable the rate of burglaries per census tract and with predictor the median income. Offset using the log of the population so that we are looking at the rate of burglaries per population instead of the number of burglaries. How can you interpret the meaning of the output? How do the estimates from the model compare to the observed data?

Additional Resources for Generalized Linear Models:
* [Generalized Linear Models in R](https://app.datacamp.com/learn/courses/generalized-linear-models-in-r), a DataCamp course
* [Beyond Multiple Linear Regression, Chapter 4](https://bookdown.org/roback/bookdown-BeyondMLR/ch-poissonreg.html)

### Bonus: APIs in R

The data that you used for this project can be obtained through [the Nashville Open Data Portal](https://data.nashville.gov/Police/Metro-Nashville-Police-Department-Incidents/2u6v-ujjs) and through the [US Census 2020 American Community Survey API](https://www.census.gov/data/developers/data-sets/acs-5year.html). Utilize these APIs to retrieve the data used on this project (and any other data that you want to incorporate into your analysis). Hints: First, make sure to check out the [API Docs](https://dev.socrata.com/foundry/data.nashville.gov/2u6v-ujjs) for the Nashville Open Data API. When using the Census API, population, B01001_001E, is contained in the detailed tables and median income, S1901_C01_012E, is contained in the subject tables. Tennessee's FIPS code is 47 and Davidson County's FIPS code is 37. 

