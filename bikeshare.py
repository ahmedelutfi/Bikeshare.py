import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chic': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'wa': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chic for chicago,ny for new york city,wa washington). HINT: Use a while loop to handle invalid inputs
    city=input("Please input your destination city as shown (chic if chicago,ny if new york,wa if washington\n\n :)").lower()
    while city not in CITY_DATA.keys():
        print("Please check your input to be one of these (chic or ny or wa) ")
        city=input("Please input your destination city as shown (chic if chicago, ny if new york city, wa if washington\n\n:) ").lower()
    choices = ['month', 'day', 'both', 'none'] 
    # TO know the filters
    filter= input('would you like to filter the raw data in day or month or both or none ?').lower()
    if filter not in choices:
        print('Try again with valid filter')
        input('would you like to filter the raw data in day or month or both or none ?').lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    monthslist=['january', 'february', 'march', 'april', 'may', 'june', 'all']
    if filter =='month' or filter=='both':
        while True:
            month = input("choose the month:(january,february,march,april,may,june,or all) " ).lower()
            if month in monthslist :
                break
            else:
                print("Please check your month again as shown above ")
   
       
   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayslist=['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    if filter =='day' or filter=='both':
        while True:
            day = input("input a day(saturday,sunday,monday,tuesday,wednesday,thursday,friday, all)  ").lower()
            if day in dayslist :
                break
            else:
                print("please check your day again as shown above!")
    

    print('-'*32)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
 
    #Convert start time column to date_time 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extract month, day of week, hour from start time to make set of columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
         monthslist=['january', 'february', 'march', 'april', 'may', 'june']
         month =monthslist.index(month) + 1
         df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    df

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\n Let's do some statistic calculations to know the most frequent time of travel ...\n")
    start_time = time.time()

    # TO DO: display the most common month
    print('the highest popular month is :{}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("the highest popular day is :{}".format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    print("the most common hour of start is :{}".format(df['hour'].mode()[0]))


    print("\nThis took time in %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nHere some statistics for the most popular stations and trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: ', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most popular endno station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_group =df.groupby(['Start Station','End Station'])
    combine_stat =common_group.size().sort_values(ascending=False).head(1)
    print('The most popular combination between start and end stations :\n',combine_stat)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTotal and average Trip Duration respectively...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())
    print(df['Trip Duration'].mean())


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nHere some statistics calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
   
# TO DO: Display earliest, most recent, and most common year of birth

    if city !='wa':
        print(df['Gender'].value_counts())
        print(df['Birth Year'].mode()[0])
        print(df['Birth Year'].max())
        print(df['Birth Year'].min())
        
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw(df):
    raws=input("would you like to display new raws of data ? yes or no ")
    if raws.lower()=='yes':
        nu=0
        while True:
            print(df.iloc[nu: nu+5])
            nu+=5
            ask=input('Next new raws ? yes or no ')
            if ask.lower() !='yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            print('Thank you, we hope to follow our new updates! ')
            break


if __name__ == "__main__":
	main()

