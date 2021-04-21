## Metis Project I: Exploratory Data Analysis

### What is the framing question of your analysis, or the purpose of the model/system you plan to build?
            
What relationships exist between foot traffic trends of NYC’s subway stations, and trends in sale prices for properties closest to those subway stations, between May 05, 2010 and December 31, 2019? 

### Who benefits from exploring this question or building this model/system?

Real estate developers, or anyone interested in acquiring property in NYC.

### What dataset(s) do you plan to use, and how will you obtain the data?

MTA Turnstile Data, collected in 4 hour increments - estimated to be 95,761,349 rows  
http://web.mta.info/developers/turnstile.html  
Detailed Annual Sales Reports by Borough - estimated to equal ~89 M  
https://www1.nyc.gov/site/finance/taxes/property-annualized-sales-update.page  
    
I plan to collect the data using BeautifulSoup and collate it into Vaex-powered DataFrames.

### What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?

An individual sample for the first dataset would include all of the entrances and exits for an entire station over one four-hour period. An individual sample for the second would be one sale for one property, which includes the full address, borough, sale price, and purchase date. 

### If modeling, what will you predict as your target?

I expect to find that a difference in one dataset (increase or decrease in foot traffic or average price per square foot) will predate a difference in another. 

### How do you intend to meet the tools requirement of the project?

After using BeautifulSoup to scrape the appropriate sites for datasets, I plan to start analysis with Vaex, a Python library used as a substitute for Pandas when working with substantial data sets. Depending on my data needs, I may research Hadoop or another big data solution. I’m also using geopy, another Python library, to attach geographic coordinates to stations and property addresses. Lastly, I’m using haversine, another Python library, to calculate the distances between properties and MTA stations to find the closest station(s) to each property. 

### Are you planning in advance to need or use additional tools beyond those required?

I’m leaving the option open to scale my tool use as needed.

### What would a minimum viable product (MVP) look like for this project?

I used a correlation analysis to describe the year-over-year change in property sale prices, categorized by type of property. The result suggests that foot traffic can be used to predict property value changes six months in advance. 
