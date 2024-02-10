# Project Description
Almost every web service you join will require you to come up with a password. But what makes a good password? In June 2017 the National Institute of Standards and Technology (NIST) published publication 800-63B titled Digital Identity Guidelines: Authentication and Lifecycle Management. This publication doesn't tell you what is a good password, but it does have specific rules for what is a bad password.

In this project, you will take a list of user passwords and, using publication 800-63B, you will write code that automatically detects and flags the bad passwords.

## Instructions
You are a data analyst working with the IT team at your company. After a recent data breach, the IT team has decided to strengthen password requirements. They've asked you to write a script to analyze the company's employees logins and identify which employees need to update their password. This will require you to use your string manipulation and regular expression skills.

### Your two questions are as follows:
	- What percentage of users have invalid passwords? Save your answer as a variable, bad_pass, in the form of a float rounded up to two decimals (e.g., 0.18).
	- Which users need to change their passwords? Save your answer as a pandas Series consisting of the usernames in alphabetically ascending order called email_list. This will be used to automate email notifications to employees.
