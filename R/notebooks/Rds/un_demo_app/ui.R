
# Define UI for application that draws a histogram
fluidPage(
  
  tags$style(
    ".irs-bar {",
    "  display: none;",
    "}"
  ),
  
  # Application title
  titlePanel("UNData"),
  
  # Sidebar with a slider input for number of bins
  sidebarLayout(
    sidebarPanel(
      sliderInput(
        "year",
        "Select a year:",
        min = min(year_choices),
        max = max(year_choices),
        value = min(year_choices),
        sep = ""
      )
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("scatterPlot")
    )
  )
)
