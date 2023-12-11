# Project Description
- Mobile apps are everywhere. They are easy to create and can be lucrative. Because of these two factors, more and more apps are being developed. In this project, you will do a comprehensive analysis of the Android app market by comparing over ten thousand apps in Google Play across different categories. You'll look for insights in the data to devise strategies to drive growth and retention. The data for this project was scraped from the Google Play website. While there are many popular datasets for Apple App Store, there aren't many for Google Play apps, which is partially due to the increased difficulty in scraping the latter as compared to the former. The data files are as follows:

	- apps.csv: contains all the details of the apps on Google Play. These are the features that describe an app.
	- user_reviews.csv: contains 100 reviews for each app, most helpful first. The text in each review has been pre-processed, passed through a sentiment analyzer engine and tagged with its sentiment score.

## INSTRUCTIONS
- You work as a `Data Analyst` for a finance company which is closely eyeing the Android market before it launches its new app into Google Play. You have been asked to present an analysis of Google Play apps so that the team gets a comprehensive overview of different categories of apps, their ratings, and other metrics.

	- This will require you to use your data manipulation and data analysis skills.

Your three questions are as follows:

- Read the apps.csv file and clean the Installscolumn to convert it into integer data type. Save your answer as a DataFrame apps. Going forward, you will do all your analysis on the apps DataFrame.


- Find the number of apps in each category, the average price, and the average rating. Save your answer as a DataFrame app_category_info. Your should rename the four columns as: Category, Number of apps, Average price, Average rating.


- Find the top 10 free FINANCE apps having the highest average sentiment score. Save your answer as a DataFrame top_10_user_feedback. Your answer should have exactly 10 rows and two columns named: App and Sentiment Score, where the average Sentiment Score is sorted from highest to lowest.
