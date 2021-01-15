library(tidyverse)

penguins <- read_csv('data/penguins.csv')

## Part 1
penguins %>% 
  ggplot(aes(x = "species")) +
  geom_bar()

## Part 2
penguins %>% 
  ggplot(aes(x = species, y = body mass g)) +
  geom_boxplot()

## Part 3
penguins %>% 
  ggplot(aes(x = island)) +
  geom_bar()
