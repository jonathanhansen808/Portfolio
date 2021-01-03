# Jonathan Hansen's Portfolio

# [Project 7: Hospital Readmission Machine Learning](https://github.com/Jonnyboyy808/Hospital_readmission)
- This project looks at the relationship between length of stay and readmission for hospital patients with diabetes. 
- Generated heat maps showing the commonalities of admission source to discharge disposition. 
- Regressed the number of days in the hospital on the number of prior visits. 
- Used one-hot encoding to make categorical variables numeric in order to regress the number of days spent in the hospital on additional factors including race, gender, and age.
- Performed logistic regression to predict whether a patient will be readmitted to the hospital 30 days after being released.

![](/images/Regression.png)
![](/images/Confusion.png)

# [Project 6: Wisconsin Land Use](https://github.com/Jonnyboyy808/Wisconsin_land_use) 
- This project explores how land is utilized in Wisconsin. The original dataset includes data on the entire United States; however, for this project, I focused solely on the state of Wisconsin. 
- Created a python module that pulls the data from a SQLite3 database, a zip file, and numpy matrices representing land use.  
- Created a connection class with methods that allows one to return the names, years, and various land usage code arrays from specific numpy files. 
- Regressed land usage codes on latitude, in order to see how much of a given land type should be expected as a percentage of total land as one goes one degree farther north.
- Used linear regression to predict what percentage of an image will contain one of the usage codes passed in as an argument for a given year, returning the Wisconsin city with the highest predicted percentage. 
- Created a plotting method that allows one to pass in a specific city and see every land usage code and its respective percentage makeup of the city over the years. 

![](/images/Madison.png)
![](/images/city_plot.png)

# [Project 5: SEC's EDGAR Data Pipeline and Visualizations](https://github.com/Jonnyboyy808/Edgar_Data)
- This project focuses on compressing EDGAR web logs. EDGAR is the SEC's database for public companies to file incomes statements and other reports. These logs contain anonymized IP addresses of the visitors.
- Sampled a percentage of zip file containing data for 1/01/2020 as a csv file and added a country column that linked each IP address to its corresponding country using regex.
- Visualized the world's EDGAR traffic per hour, as well as each specific continent's EDGAR per hour using GeoPandas.
- Generated an animation showing how the world's EDGAR traffic changes throughout each hour of the day, with darker shading representing more EDGAR traffic. 

![](/images/8pm.png)
![](/images/Europe.png)

# [Project 4: Building a Data Website with Flask](https://github.com/Jonnyboyy808/Flask_data_website)
- The data hosted uses The Rolling Stone's Top 500 songs of all time list. 
- Produced a browse page bringing visitors to a dataframe hosting data, such as the song name, artist(s), producer(s) and writer(s). 
- Created an API page that allows one to query their own data to get their desired custom information.
- Included a donate link and an email subscription option that allows users to sign up for a mailing list. 

![](/images/Datasite_Homepage.png)
![](/images/Browse_DF.png)
![](/images/API.png)

# [Project 3: Web Scraping with Selenium From a Flask-implemented Website](https://github.com/Jonnyboyy808/hunting_for_treasure)
- The website the information was scraped from was created for a class projct.
- Created a scraper class that included an easter_egg method to scrape a specific website to find hidden text between <span> tags that concatenate to a secret message.
- Designed a depth-first search and binary-first search  methods, dfs_pass and bfs_pass, that search on the website's homepage to collect hidden letters and concatenate them to seperate passwords.
- Designed a protected_df method to enter passwords on the homepage, which will then return a dataframe of all the information hidden on the page shown when the password is entered. 
  
![](/images/Homepage.png)
![](/images/Protected_df.png)
  
# [Project 2: Analyzing the Evolution of a Git Repository](https://github.com/Jonnyboyy808/.py_Program_Complexity)
- The repository I analyzed contained a python program wc.py that counted the words of a text passed in. 
- Analzyed how the .py file had grown and changed over time, including who had made what changes to each commit of repository. 
- Passed three test strings into my own function "run_wc" that runs every commit of wc.py to see which commits matched the expected output and which did not. 
- Randomly generated words X number of words and chose Y number of unique words from X to run the different versions of wc.py on, in order to test the performance of the various commits at different complexities.
- Visualized the difference in complexity as the chosen words got more and more unique for the two fastest versions of wc.py.

![](/images/Complexity_DF.png)
![](/images/Complexity.png)


# [Project 1: Analyzing the Geography of Countries and Their Capitals](https://github.com/Jonnyboyy808/Country_and_Capital_Geography-)
- The data scraped was from http://techslides.com/list-of-countries-and-capitals.
- Put the data into Pandas dataframes and analyzed various things, such as the most landlocked countries, the countries with the highest/lowest birth/death rates, and capital's population density and distance to their closest coast. 
- Dumped the dataframes into a SQLite3 database to be queried and visualized on several things, including the number of countries per continent, population per continent, highest/lowest GDP per country.
- Generated scatterplots, such as phone usage on GDP per capita or GDP per capita on literacy rates. 

![](/images/Death:Birth%20rate%20DF.png)
![](/images/Death-birth-rates.png)

