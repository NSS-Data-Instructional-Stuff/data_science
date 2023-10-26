## Introduction to the Tidyverse: An Exploration of UN Data 
In this project, you'll be redoing the UN Data project using the tidyverse libraries. You have been provided three csv files, gdp_per_capita.csv, life_expectancy.csv, and continents.csv.

Create a new R Notebook to complete this exercise.

1.	Using the `read_csv()` function, read the GDP dataset into your notebook as a tibble called `gdp_df`. After reading it in, inspect the first 10 rows and then inspect the last 10 rows. 

2. Drop the 'Value Footnotes' column, and rename the remaining columns to 'Country', 'Year', and 'GDP_Per_Capita'.

3. Which years are represented in this dataset? How many observations are there per year? Make a plot to view the number of observations per year.

4. How many countries are represented in this dataset? Which countries have the fewest observations?

5. Create a new dataframe by subsetting `gdp_df` to just the year 2014. Call this new dataframe `gdp_2014`.

6. Use `.describe()` to find the summary statistics for GDP per capita in 2014. 

7. Create a histogram of GDP Per Capita numbers for 2014 (you may wish to adjust the number of bins for your histogram).

8. Find the top 5 counties and bottom 5 countries by GDP per capita in 2014.

9. Now, return to the full dataset, `gdp_df`. Pivot the data for 1990 and 2018 (using the pandas `.pivot_wider()` method or another method) so that each row corresponds to a country, each column corresponds to a year, and the values in the table give the GDP_Per_Capita amount. Drop any rows that are missing values for either 1990 or 2018. Save the result to a dataframe named `gdp_pivoted`.

10. Create a new column in `gdp_pivoted` named `Percent_Change`. This column should contain the percent change in GDP_Per_Capita from 1990 to 2018. Hint: Percent change is calculated as 100*(New Value - Old Value) / Old Value.

11. How many countries experienced a negative percent change in GDP per capita from 1990 to 2018?

12. Which country had the highest % change in GDP per capita? Create a line plot showing these country's GDP per capita for all years for which you have data. Put both line charts on the same plot.

13. Read in continents.csv contained in the `data` folder into a new dataframe called `continents`. We will be using this dataframe to add a new column to our dataset.

14. Merge gdp_df and continents. Keep only the countries that appear in both data frames. Save the result back to gdp_df.

15. Determine the number of countries per continent. Create a bar chart showing this.

16. Create a seaborn boxplot showing GDP per capita in 2018 split out by continent. What do you notice?

17. Read life_expectancy.csv into a tibble named life_expectancy. Do not modify the csv file in order to read this data in. 
 
18. Drop the Country Code, Indicator Name, and Indicator Code columns. Then use `pivot_longer` to convert your data from wide to long. That is, instead of having one row per country and multiple colums per year, we want to have multiple rows per country and a single column for year. After melting, rename the columns to `Country`, `Year`, and `Life_Expectancy`.

19. What was the first country with a life expectancy to exceed 80?

20. Merge `gdp_df` and `life_expectancy`, keeping all countries and years that appear in both DataFrames. Save the result to a new DataFrame named `gdp_le`. If you get any errors in doing this, read them carefully and correct them. Look at the first five rows of your new data frame to confirm it merged correctly. Also, check the last five rows to make sure the data is clean and as expected.

21. Create a new DataFrame, named `gdp_le_2019` by extracting data for the year 2019 from `gdp_le`. How many countries have a life expectancy of at least 80 in 2019?

22. Find the countries that had the top 3 largest GDP per capita figures for 2019. Create a [seaborn FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html) showing the change in life expectancy over time for these three countries. Each individual figure in the facet grid will represent a single country.

23. Create a scatter plot of Life Expectancy vs GDP per Capita for the year 2019. What do you notice?

24. Find the correlation between Life Expectancy and GDP per Capita for the year 2019. What is the meaning of this number?

25. Add a column to `gdp_le_2019` and calculate the logarithm of GDP per capita. Find the correlation between the log of GDP per capita and life expectancy. How does this compare to the calculation in the previous part? Look at a scatter plot to see if the result of this calculation makes sense.
