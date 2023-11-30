## Tidyverse Solo Exercise

In this project, you'll practice working with data using the tidyverse libraries. 
You'll be working with data on each of 145 school districts and the State of Tennessee. This data contains, for the 2014-2015 school year:
* Proficiency rates on state tests
* Student demographics
* Chronic absenteeism
* Discipline (suspension, expulsion) rates
* High school graduation, dropout rates
* Average ACT composite scores
* A region in Tennessee  

Create an RMarkdown file to answer the following questions.

1. Read in `districts.csv` into a tibble named `districts`.

2. Notice that the first row corresponds to the whole State of Tennessee. Remove this row and save the result back to `districts`.

3. How many districts have a proficiency rate of at least 80% for both alg_1 and eng_1?

4. How many districts have a proviciency rate less than 50% for either alg_1 or eng_1?

5. Which district has the lowest graduation rate?

6. Within the Mid Cumberland region, which district has the highest ACT composite?

7. Create a scatter plot to compare alg_1 proficiency rates to alg_2 rates. What do you notice? Facet this plot by region. Does anything stand out when you facet the plots?

8. When creating this bar chart you may have noticed that some districts have missing enrollment values. For how many districts is this the case?

9. A lot of rows are missing additional values. Which district has the largest number of missing values (across all variables)? Hint: you might want to look at rowwise and c_across to answer this question.

10. What is the mean graduation rate across all districts? What might be wrong with using just the regular mean to assess average graduation rates?

11. Redo the previous question but use a weighted average (`weighted.mean`) graduation across all districts, weighing by enrollment. How much does this change your answer? Can you explain using the data the reason for the big change from using the mean?

12. Find the unweighted and weighted average graduation rate by district.

**Continued Exploration and Practice**

13. Read in the school-level testing data for 2014, available [here](https://www.tn.gov/content/dam/tn/education/data/data_2014_school_base.xlsx). You might find the readxl library useful for this task. If you use this library, be sure to look at the `na` argument for the `read_excel` function.

To answer the following questions, use "All Students" for the subgroup. 

14. How many schools have at least 20 percent of students below bsc for Algebra I? Which districts do these schools belong to?

15. How many schools have at least 20 percent of students below bsc for _both_ Algebra I and English I?

16. Which grade has the highest pct_adv for Algebra I? Plot the average pct_adv per grade level as a bar chart. Make sure that the bars are ordered by grade level.

17. Find the correlation between pct_adv for Algebra I and pct_adv for Algebra II by school. Create a scatterplot showing Algebra II scores vs. Algebra I scores by school.

18. Find all schools in Rutherford County that have "High School" in their name. For these schools, create a chart (your choice) showing the differences in pct_below_bsc, pct_bsc, pct_prof, and pct_adv for Algebra I when looking across all subgroups and grades.

19. Create a function which allows you to select a system_name and which creates a plot to show the differences in pct_below_bsc, pct_bsc, pct_prof, and pct_adv for Algebra I when looking across all subgroups and grades for all schools with "High School" in their names within that system.