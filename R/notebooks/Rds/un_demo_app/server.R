
# Define server logic required to draw a histogram
function(input, output, session) {

    output$scatterPlot <- renderPlot({
      un_data |> 
        filter(Year == input$year) |> 
        drop_na() |> 
        ggplot(aes(x = gdp_per_capita, y = life_expectancy)) + 
        geom_point()
    })

}
