
# Define server logic required to draw a histogram
function(input, output, session) {

    output$scatterPlot <- renderPlot({
      
      #cat(file=stderr(), "drawing scatterplot for", input$year, "\n")
      
      un_data |> 
        filter(Year == input$year) |> 
        drop_na() |> 
        ggplot(aes(x = gdp_per_capita, y = life_expectancy)) + 
        geom_point()
    })
    
    #observeEvent(input$debug, browser())

}
