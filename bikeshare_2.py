import time
import pandas as pd
import numpy as np

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
    city = input("Would you like to see data for chicago, new york city or washington? ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("for which month? ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("for which day of the week? ").lower()

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        index_day = days.index(day)
        df = df[df['day_of_week'] == days[index_day].title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].value_counts().index[0]
    print('Most Common Month: ', months[popular_month-1])
    
    # TO DO: display the most common day of week
    popular_dow = df['day_of_week'].value_counts().index[0]
    print('Most Common Day Of Week: ', popular_dow)

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.value_counts().index[0]
    print('Most Frequent Start Hour:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().index[0]
    print('Most Commonly Used Start Station:', popular_start_station)
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().index[0]
    print('Most Commonly Used End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = df['Start Station'] + ' ' + df['End Station']
    print('Most frequent combination of start station and end station trip:', combination_start_end.value_counts().index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time:', total_time)
    
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    while True:
        try:
            print(df['Gender'].value_counts())
            break
        except KeyError:
            print("The washington file does not have Gender column")
            break
    

    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:
            print('Earliest year of birth', df['Birth Year'].unique()[-1])
            print('Most recent year of birth', df['Birth Year'].unique()[0])
            print("Most common year of birth:", df['Birth Year'].value_counts().index[0])
            break
        except KeyError:
            print("The washington file does not have Birth Year column")
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)
 
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            
            counter = 0
            while True:
                show_raw = input('\nWould you like to see raw data? Enter yes or no.\n')
                if show_raw.lower() == 'yes':
                    print(df[0+counter:5+counter])
                    counter += 5
                if show_raw.lower() == 'no':
                    break
                
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except KeyError:
            print("Invalid city input")

if __name__ == "__main__":
	main()
