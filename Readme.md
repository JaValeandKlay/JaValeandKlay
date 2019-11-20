This is a Readme for the fitbit project by JaVale and Klay.

Background: The purpose of the this project was to examine data extracted from multiple CSVs located on a thumb drive. 

ADMINSTRATIVE NOTES:

The following install are necessary for the ability to replicate the files in the repository:

conda install pystan

conda install -c conda-forge fbprophet



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


