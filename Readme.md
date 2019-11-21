This is a Readme for the fitbit project by JaVale and Klay.

Background: The purpose of the this project was to examine data extracted from multiple CSVs located on a thumb drive. 

ADMINISTRATIVE NOTES:

Prophet Documentation: https://facebook.github.io/prophet/
Prophet is an open source software released by facebooks Core Data Science Team.  We implemented it in Python. It is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects.

The following install are necessary for the ability to replicate the files in the repository:

conda install pystan

conda install -c conda-forge fbprophet

ORDER OF OPERATIONS:

Inside the repository, there are a number of .CSV files, several .py files, and several .ipynb files. The flow of the .ipynb files is as follows:

fitbit_baseline_model.ipynb: This notebook includes the acquisition, preparation, exploration, and initial baseline modeling of the data. This file contains the baseline model that we then used to compare against our Prophet model. 

prophet_validation_train_test: This notebook includes the acquisition, preparation, and modeling of our data using the Prophet model from Facebook. We evaluate the MSE and RMSE for each target variable.

IT IS RECOMMENDED THAT YOU READ THROUGH THE NOTEBOOK FIRST AND ADHERE TO THE CAUTION BELOW TO SMOOTHLY REPLICATE THE DATA.

**** CAUTION ****

In order for this notebook to be replicated and generate the data, follow the following steps:

Under the markdown section that states, "Set column names to 'ds' and 'y' in order to feed into Prophet", the y value = target value. To generate the subsequent forecasts, predicitions, MSE and RMSE, you WILL NEED TO CYCLE THROUGH EACH TARGET VARIABLE ONE AT A TIME. 

You will need to run the validation on each target variable. After calculating the RMSE for each target variable and generating a graph, comment out that code to prevent re-running the cell. Once those two cells have been commented out, revert back to the "Set column names to 'ds' and 'y' in order to feed into Prophet" markdown and begin anew with your next target variable. 


prophet_modeling_predictions.ipynb:

This notebook generates the predictions for the next 14 days of information and writes the values to a .CSV file titled: missing_2_weeks_predictions.csv



NOTES ABOUT THE BASELINE MODEL:

DATA COLLECTION: 

Data was collected using the acquire.get_fitbit_data() function located in the acquire.py file in the repository. This file collects and concats 8 .csv files into one dataframe consisting of 225 rows and 10 initial columns. 

DATA PREPARATION:

Data was first prepped by renaming the columns for easier readability and typing. Nulls were checked and it was discovered there were no nulls in the initial data set. 

The date column was converted to a date_time for time series analysis. All object columns were convereted to 'int' or 'float' after undergoing string replacement therapy.


FEATURE ENGINEERING:

Several new columns were created to enhance the discovery process and further the understanding of the data. The most significant of these features were:

df['percent_not_worn'] = ((1440 - (df.minutes_fairly_active + df.minutes_lightly_active + df.minutes_sedentary + df.minutes_very_active))/1440)*100

This feature allowed the team to analyze how often the tracking device was worn throughout the day as a percentage of the day.

df['bmr'] = df.calories_burned - df.activity_calories

BMR = Basal Metabolic Rate is defined as the rate at which your body uses energy when you are resting in order to keep vital functions going such as breathing. The rate at which your body uses energy to breath and stay warm is an example of your basal metabolic rate.

The purpose of this feature was to examine whether the subject's overall fitness level improved or regressed over time.

df['gait'] =(df.distance * 5280)/df.steps

This feature examined an overall activity level for a person. A higher gait rate would suggest that a person increased their stride, aka walking to jogging/ jogging to running. 


DATA SPLIT:
Split data around the original target features. 

Created 3 dataframes with different samples based on day, week, and month, but ended up only using the data sampled on a daily basis.  

Used split_store_data() from exercises to split our current dataframe. SET TRAIN PROP AT 81.5%.

Total obeservations should equal 225
Total number of training observations should equal 183.
Total number of test observations should equal 42.

REINDEX TRAIN AND TEST ON DATE.

In order to run our evaluate function, we were required to align our train and test sample values to be equal to one another. With tests observations already set at 42, it was most efficient to align our train data dates to produce a similiar number of observations. 

GENERAL NOTES ABOUT PROPHET MODELING:

Creating a function that looped through all target variable was a feature that we could not generate at the time of publication. This is why the notebook is very deliberate about generating the values for each target. 

*** LINK TO GOOGLE SLIDES PRESENTATION ***

https://docs.google.com/presentation/d/18SlqW_t5-04ZqB1FqqgdOOVimq_A_Dbd57pSYKSCIck/edit?usp=sharing