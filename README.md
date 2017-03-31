# EmailAnalysis
ML for Email Analysis

Audience : For Individuals with Machine Learning and AI exp and   knowledge of Statistics and Probability.
 
What am I planning to do :

What do I want to measure? I suspect that more than 50% of the corporation was aware of the failure.

How will I measure ? I will use the classification and regression models to measure my hypothesis.

How will model’s  help to measure ? I will use the R2 and mean square error to validate my hypothesis (in this case I will see if the R2 value is higher than 0.5)

Extracting & Cleaning
1. Get the pst files and convert into simple text files or download from https://www.kaggle.com/wcukierski/enron-email-dataset/downloads/emails.csv.zip 
2. Clean each email file to restrict number of words in each message, normally one page contains max of 3000 words and beyond which are the encrypted form of attachment or the forwarded version of email which you will be able to find in some other inbox.
3. Now prepare a structured csv file using the cleaned file (text) from item #2 and include the person of interest (POI) indicator, you and list the POI by studying the SEC’s 10K from EDGAR, public records and newspaper article.
4. Creates the final structured email file by adding negative word column using the financial and legal negative word file these files are available in public domain and you can create negative word files of your own.
5. At this point you will have a CSV file containing the all email headers, message content(restricted to 3000 words), negative word in each email and count and % of negative word for each email ( later these count will be transformed to Classification for Classification models and will be used directly for regression models)

Modeling and Processing:

 

1. After processing data Run the Main Agent (python program), this agent depends on the below mentioned subagent and models

1.  Gets data from cleaned CSV file and separate data set for Training, Testing and SVM (normally the distribution is 80%, 10% and 10% , but for email analysis you will have to figure out what will be your training set and testing set , you have to be conscious about over-fitting and under-fitting)
2.  Now prepares data for classification, basically you will have to understand how the data set can be classified, some of the example may be negative word found vs not found etc. (there are many ways to classify and you will have to define your classification based on your analysis objective.). So now you have datasets for  training, testing , support vector by classification
3.  Similarly now  prepares data for regression (training, testing , support vector)
4.  Prepare a subagent to call regression and classification models
5.  Prepare a subagent to plots exploratory data for entire dataset , training and testing for both classification and regression. Model complexity etc.
6.  Execute subagent to call all   classification and regression models (depending on your analysis it can range from 2 to 12).
7.  Execute subagent to plots output for regression and classification
8.  Execute subagent to plots model complexity
9.  Execute subagent to calculates model complexity
