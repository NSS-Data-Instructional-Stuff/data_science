### Datasets
Two datasets are provided with this assessment:
- emissions tracker data (`climate.csv`)
- a table of country names and ISO country codes (`country_codes.csv`)

The data from climate.csv comes from the [Climate Action Tracker](https://climateactiontracker.org/), an organization that keeps track of countries' progress in tackling climate change. 

### Instructions
1. Create a new R file (either an R script or an R notebook, your choice). Name your file as <firstname_R_assessment>. For example, my notebook would be named `michael_R_assessment.Rmd`
2. Read in the data from climate.csv. How many rows and columns does this dataset have?
3. Read in the country_codes.csv data. This contains country names and 2 and 3-letter ISO country codes. Merge this with the original dataset (keeping only those rows that have matches on the 2-letter country code in both tables). At this point, feel free to rename columns and/or drop any columns that you think will not be useful.
4. After the merge, how many countries are left in the dataset?
5. Create a new dataframe, called "renewable" which contains all rows with indicator "Share of renewable electricity generation" from the **year 2014**. 
- Create a visualization (your choice) showing the distribution of the share of renewable electricity generation across the countries in the dataset. 
- What can you say about this distribution? 
- Create a new column in renewable, called "majority_renewable" and in this column indicate whether a country is majority renewable (>50% renewable electricity generation) or not. 
- What percentage of countries in this data frame were majority renewable in 2014?
- How does the "Electricity emissions intensity" in 2014 compare for countries which were majority renewable in 2014 vs those which were not? Create a visualization (your choice) to support your assessment.
6. Which country was the top oil and gas producer in 2014? (Hint: this value can be found by using the indicator "Oil and Gas activity: production")
7. Look at the trend in oil and gas production (again, using the "Oil and Gas activity: production" indicator) in the US from 1990 through 2014. What do you notice? Create a visualization (your choice) to support your assessment.
8. Find the total (across all countries in the dataset) number of new EV sales per year **from 2009 through 2014**. (Sales per country can be found using indicator "New EV sales".) What do you notice? Create a visualization (your choice) to support your answer.
9. Create a scatter plot showing Emissions per capita vs GDP per capita for the year 2014. Hint: You can find these values by using indicators "Emissions per capita" and "GDP per capita". Hint #2: You will probably want to subset and then pivot the data in order to create this plot.
10. Find the correlation between emissions per capita and GDP per capita for the year 2014 (dropping NAs). How strong of a (linear) relationship is there between these two measures?

Once you are finished, email your file to michael.holloway@nashvillesoftwareschool.com.