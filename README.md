# Jonathan Hansen's Portfolio

# [Visualizing California Weather Patterns With RShiny](https://jonathanhansen808.shinyapps.io/californiaWeather/)
- This project analyzes precipitation, temperature, drought, and natural disaster data from 1920-2021 in California.
- The application includes four tabs, including one on yearly precipiation and temperature averages of 10 California areas, where users can select an area to view against the other nine areas. The second tab shows the same 10 areas on a map, where users can see precipitation and temperature averages for the year and month of their choice. The third tab shows the percentage of California under five specific drought severity levels (e.g., D0 is the least severe and D5 is the most severe) for a selected span of years. The last tab is a static plot of the count of natural disasters in California from 1980-2020 and their respective costs. 
- Findings include seeing temperatures, severe droughts, and natural disasters increasing over time and precipitation decreasing over time. 
- Data was used from https://www.weather.gov/wrh/climate, https://www.drought.gov/states/california, and https://www.ncei.noaa.gov.

![](/images/temp_plot.png)
![](/images/temp_map.png)
![](/images/drought.png)
![](/images/nat_disasters.png)

# [Beer Production in America Using RShiny](https://jonathanhansen808.shinyapps.io/beer/)
- This project visualizes beer production across the United States from 2009-2019. 
- Production consists of the number of barrels produced in beer bottles or cans for a given year.
- The Shiny application includes both a bar chart of the top 15 states in beer production for a year, as well as a map of the continental United States, where the states are shaded by their production for a year. 

![](/images/beer_app.png)

# [Modeling Crime in North Carolina Using RStan](https://github.com/jonathanhansen808/crime_modeling)
- This project looks at the influence of several deterrent and non-deterrent factors that affect a county's crime rate in North Carolina. 
- The Data is from the Ecdat R package Crime: Crime in North Carolina (https://rdrr.io/cran/Ecdat/man/Crime.html).
- The data spans from 1981 to 1987 and includes data from 88 counties in North Carolina (n=618). 
- The explanatory variables chosen for analysis were the probability of arrest, probability of a prison sentence, the county's population density, and the ratio of a county's police force to the average police force density. The response variable was the county's crime rate in a given year. 
- All variables included were transformed logarithmically and two bayesian log-log regression models were fit. The first model used a pooled intercept approach, giving all counties the same baseline crime rate. The second model was hierarchical, where each county had a different intercept for crime rate. 
- Using 1987 as a year to test both models' predictions, the pooled intercept model captured 80/88 counties in 95% prediction intervals, and the hierarchical model captured 83/88 counties in 95% prediction intervals. 
- Of the four explanatory variables, probability of arrest turned out to be the only crime deterrent, since as the probability of arrest increased, the crime rate decreased. Interestinly, as the population of police increased in a given county, relative to the average in North Carolina, crime increased. 

![](/images/MLR_OOS_hierarchical.png)
![](/images/county_baseline_probs.png)


# [America's Pastime Reviews Website](https://americaspastime-99f97.web.app) 
- This project was created by Peter Kennedy and I. America's Pastime Reviews is hosted by Google Firebase and was built using Bulma and JavaScript. 
- The site was created with the intent of consolidating stadium information, event tickets, and stadium rankings for all 30 teams in the MLB.
- Users must sign up or sign in order to leave a review or see other reviews. 
- Firebase was utilized to store user account credentials, stadium reviews and pictures through a NoSQL database. 
- Be sure to check out some of the cool stadiums featured like the Chicago Cubs or San Francisco Giants!  

![](/images/home.PNG)
![](/images/pit.PNG)

# [Hospital Readmission Machine Learning](https://github.com/Jonnyboyy808/Hospital_readmission)
- This project looks at the relationship between length of stay and readmission for hospital patients with diabetes. 
- Generated heat maps showing the commonalities of admission source to discharge disposition. 
- Regressed the number of days in the hospital on the number of prior visits. 
- Used one-hot encoding to make categorical variables numeric in order to regress the number of days spent in the hospital on additional factors including race, gender, and age.
- Performed logistic regression to predict whether a patient will be readmitted to the hospital 30 days after being released.

![](/images/Regression.png)
![](/images/Confusion.png)

# [Land Use Around Wisconsin](https://github.com/Jonnyboyy808/Wisconsin_land_use) 
- This project explores how land is utilized in Wisconsin. Some of the various land types are open water, deciduous forest, and developed land.  
- Created a python module that pulls the data from a SQLite3 database, a zip file, and numpy matrices representing land use.  
- Regressed land usage codes on latitude, in order to see how much of a specified land type should be expected as a percentage of total land as one goes one degree farther north.
- Used linear regression to predict what percentage of an image will contain one of the usage codes passed in as an argument for a given year, returning the Wisconsin city with the highest predicted percentage. 
- Created a plotting method that allows one to pass in a specific city and see every land usage code and its respective percentage makeup of the city over the years. 

![](/images/Madison.png)
![](/images/city_plot.png)

# [SEC's EDGAR Data Pipeline and Visualizations](https://github.com/Jonnyboyy808/Edgar_Data)
- This project focuses on compressing EDGAR web logs. EDGAR is the SEC's database for public companies to file incomes statements and other reports. These logs contain anonymized IP addresses of the visitors.
- Sampled a percentage of a csv file containing data for 1/01/2020 and added a country column to the csv that linked each IP address to its corresponding country using regex.
- Visualized the world's EDGAR traffic per hour, as well as each specific continent's EDGAR per hour using GeoPandas.
- Generated an animation showing how the world's EDGAR traffic changes each hour of the day, with darker shading representing more EDGAR traffic. 

![](/images/8pm.png)
![](/images/Europe.png)

# [Analyzing Rolling Stone Magazine's Greatest 500 Songs Website With Flask](https://github.com/Jonnyboyy808/Flask_data_website)
- The data hosted uses Rolling Stone's Greatest 500 Songs of all Time list. 
- Produced a browse page bringing visitors to a dataframe, including data such as the song name, artist(s), producer(s) and writer(s). 
- Created an API page that allows data to be queried in order to generate custom information.
- Included a donate link and an email subscription option that allows users to sign up for a mailing list. 

![](/images/Datasite_Homepage.png)
![](/images/Browse_DF.png)
![](/images/API.png)

# [Analyzing the Geography of Countries and Their Capitals](https://github.com/Jonnyboyy808/Country_and_Capital_Geography-)
- The data scraped was from [techslides](http://techslides.com/list-of-countries-and-capitals).
- Put the data into Pandas dataframes and analyzed various pieces of information, such as the most landlocked countries, the countries with the highest/lowest birth/death rates, and their capitals' population density and distance to the closest coast. 
- Inserted the dataframes into a SQLite3 database to be queried and visualized on several things, including the number of countries per continent, population per continent, and highest/lowest GDP per country.
- Generated scatterplots, such as phone usage vs GDP per capita or literacy rates vs GDP per capita.

![](/images/Death:Birth%20rate%20DF.png)
![](/images/Death-birth-rates.png)

