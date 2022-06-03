import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    


     # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        
    while True:
        city = input("\nPlease choose one of these city for filter by 'chicago, new york city, wahshington'\n").lower()
        if city not in CITY_DATA:
            print("Sorry, The input was not valid ! Please try again")
        else:
            break
            
     # TO DO: get user input for month (all, january, february, ... , june)
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("\nPlease choose one of these months for filter by january, february, march, april, may, june or type 'all' if you want to see all these months\n").lower()
        if month in months:
            break
        else:
            print("Sorry, The input was not valid ! Please try again")
             
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday
    
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while True:
        day = input("\nWhich day do you like to filter by sunday, monday, tuesday, wednesday, thursday, friday, saturday or you can type 'all'\n").lower()
        if day in days:
            break
        else:
            print("Sorry, The input was not valid ! Please try again")
            
    print('-'*40)
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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        
         # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
        # filter by day of week if applicable
    if  day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    
    return df

def display_raw_data(df):
    """
    Displays subsequent rows of data according to user answer
    Args:
        df - Pandas dataFrame containing city data filtered by month and day returned from load_data() function
    """
    i = 0
    answer = input('Would you like to display the first 5 rows of data? yes/no: ').lower()
    pd.set_option('display.max_columns', None)
    
    while True:
        if answer =='no':
            break
        print(df[i:i+5])
        answer = input('Would you like to display the first 5 rows of data? yes/no: ').lower()
        i += 5




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['month'].mode()[0]
    print('The most common month:', calendar.month_name[common_month])


    # TO DO: display the most common day of week
    
    common_day = df['day_of_week'].mode()[0]
    print('The most common day:', common_day)


    # TO DO: display the most common start hour
    
    common_hour = df['hour'].mode()[0]
    print('The most common hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station:', common_start_station)


    # TO DO: display most commonly used end station
    
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    
    combination_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent start and end station:', combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time/3600, "hour")


    # TO DO: display mean travel time
    
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', average_travel_time/60, "Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print('Count of user type:', df['User Type'].value_counts())


    # TO DO: Display counts of gender
    
    try:
        count_gender = df['Gender'].value_counts()
        print('Count of Gender:', count_gender)
    except KeyError:
        print('Sorry, No data about gender and birth year available for Washington')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        earliest_year = int(df['Birth Year'].min())
        print('Earliest year birth day:', earliest_year)
    except KeyError:
        print('Sorry, No data about gender and birth year available for Washington')
        
    try:
        recent_year = int(df['Birth Year'].max())
        print('Most recent year birth day:', recent_year)
    except KeyError:
        print('Sorry, No data about gender and birth year available for Washington')
    
    
    try:
        common_year = int(df['Birth Year'].mode()[0])
        print('Most common year birth day:', common_year)
    except KeyError:
        print('Sorry, No data about gender and birth year available for Washington')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()