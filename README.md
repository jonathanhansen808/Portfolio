# Jonathan Hansen's Portfolio

# [America's Pastime Stadium Reviews Website](https://americaspastime-99f97.web.app) 
- This project was created by Peter Kennedy and I, and is hosted by Google Firebase and built on Bulma and JavaScript. 
- The site consolidates information and rankings on all 30 team stadiums in the MLB.
- Users must sign up or sign in in order to leave or see a review on the site. Firebase was leveraged here to store user's account credentials and to allow users to upload pictures with their reviews. 
- Be sure to check out some of the cool stadiums featured like the Chicago Cubs or San Francisco Giants.  

![](/images/home.png)
![](/images/pit.png)

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

# [Analyzing the Evolution of a Git Repository](https://github.com/Jonnyboyy808/.py_Program_Complexity)
- The repository I analyzed contained a python program wc.py that counted the words of a text passed in. 
- Analzyed how the .py file had grown and changed over time, including who had made what changes to each commit of repository. 
- Passed three test strings into my own function "run_wc" that runs every commit of wc.py to see which commits matched the expected output and which did not. 
- Randomly generated X number of words and chose Y number of unique words from X on which to run the different versions of wc.py, in order to test the performance of the various commits at different complexities.
- Visualized the difference in complexity as the chosen words got increasingly unique for the two fastest versions of wc.py.

![](/images/Complexity_DF.png)
![](/images/Complexity.png)


# [Analyzing the Geography of Countries and Their Capitals](https://github.com/Jonnyboyy808/Country_and_Capital_Geography-)
- The data scraped was from [techslides](http://techslides.com/list-of-countries-and-capitals).
- Put the data into Pandas dataframes and analyzed various pieces of information, such as the most landlocked countries, the countries with the highest/lowest birth/death rates, and their capitals' population density and distance to the closest coast. 
- Inserted the dataframes into a SQLite3 database to be queried and visualized on several things, including the number of countries per continent, population per continent, and highest/lowest GDP per country.
- Generated scatterplots, such as phone usage vs GDP per capita or literacy rates vs GDP per capita.

![](/images/Death:Birth%20rate%20DF.png)
![](/images/Death-birth-rates.png)

