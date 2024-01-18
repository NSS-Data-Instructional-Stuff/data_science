library(shiny)
library(tidyverse)

un_data <- read_rds("data/un_data.Rds")

year_choices <- un_data |> 
  pull(Year) |> 
  unique() |> 
  sort()
