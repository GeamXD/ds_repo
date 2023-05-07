#Project Description
Time series data is everywhere; from temperature records, to unemployment rates, to the S&P 500 Index. Another rich source of time series data is Google Trends, where you can freely download the search interest of terms and topics from as far back as 2004. This project dives into manipulating and visualizing Google Trends data to find unique insights.

In this project’s guided variant, you will explore the search data underneath the Kardashian family's fame and make custom plots to find how the most famous Kardashian/Jenner sister has changed over time. In the unguided variant, you will analyze the worldwide search interest of five major internet browsers to calculate metrics such as rolling average and percentage change.

## Instructions
Using Google Trends, you've been asked to generate a report on changes in browser popularity since 2004. There are five browsers you'll be looking into: Firefox, Safari, Chrome, Internet Explorer, and Opera. For the report, you need to calculate three key metrics:
	- Find the six month rolling average (a.k.a. simple moving average) for each date and browser in the dataset. Save your answer as pandas DataFrame called rolling_six with the column Month as the index. Null values are acceptable for dates where a rolling six month average can't be generated.

	- Similar to above, create a DataFrame called pct_change_quarterly with the percentage change from the previous quarter for each date and browser. The values should be in percentage format, so 5 instead of 0.05. Since Chrome launched in late 2008, only include dates during or after 2009.

	- From the earlier questions, you can see that even though Chrome eventually overtook Firefox, Chrome's growth has had its fair share of ups and downs. You will illustrate this by comparing Chrome's annual Google Trends performance in 2009, 2012, 2015, and 2018 in a DataFrame called chrome_trends. It should hold the search interest for Chrome with four columns for each year and twelve rows for each month of the year.

# Plotting your answers
To make the report, you can visualize your DataFrames using pandas.DataFrame.plot. This is not tested so customize your plots as you wish! Here are examples:
rolling_six.plot(title="6 Month Rolling Avg")
pct_change_quarterly.plot(subplots=True, figsize=(12,8))
chrome_trends.plot(title="Chrome Search Performance in 2009, 2012, 2015 & 2018")
