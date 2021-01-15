library(tidyverse)

bigfoot_sightings <- read_csv('data/sightings.csv')

wilderness <- read_csv('data/wilderness_by_state.csv')

sightings_by_state <- bigfoot_sightings %>% 
  ## Fill in your code here
