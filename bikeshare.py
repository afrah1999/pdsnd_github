import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    months=['january', 'february', 'march', 'april', 'may', 'june']
    days= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    not_valid=True
    while not_valid:
        city=input("Are you interested in seeing Chicago, Washington or New York data?\n").lower()
        if city in CITY_DATA:
            not_valid=False
        else:
            print("Please enter a valid city name\n")

    while True:
        filter=input("How would you like to filter the data? By month, day, or none at all? Type \"none\" for no time filter\n").lower().strip()

        if filter=="month":
            day='all'
        # get user input for month (all, january, february, ... , june)
            while True:
                month=input("During which month? January, February, March, April, May, or June?\n").lower()
                if month in months:
                    break
                else:
                    print("Please enter a valid month name\n" )
            break

        # get user input for day of week (all, monday, tuesday, ... sunday)
        elif filter=="day":
            month='all'
            while True:
                day=input("For wich day? Monday,Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n").lower()
                if day in days:
                    break
                else:
                    print("Please enter a valid day name\n")
            break

        elif filter=='none':
            day='all'
            month='all'
            break
        else:
            print("Please Enter a valid filter.\n")

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

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months= ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    day.title()
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df,month, day):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] =pd.to_datetime(df['Start Time'])
    if month == 'all':
        # display the most common month
        df['month'] =df['Start Time'].dt.month
        # find the most common hour (from 0 to 23)
        popular_month = df['month'].value_counts().idxmax()

        print('Most Frequent  month:', popular_month)

        df['hour'] =df['Start Time'].dt.hour
        # find the most common hour (from 0 to 23)
        popular_hour = df['hour'].value_counts().idxmax()

        print('Most Frequent Start Hour:', popular_hour)


    # display the most common day of week
    if day == 'all':

        df['day'] =df['Start Time'].dt.day_name()
        # find the most common hour (from 0 to 23)
        popular_day = df['day'].value_counts().idxmax()

        print('Most Frequent day:', popular_day)


        # display the most common start hour

        # extract hour from the Start Time column to create an hour column
        df['hour'] =df['Start Time'].dt.hour
        # find the most common hour (from 0 to 23)
        popular_hour = df['hour'].value_counts().idxmax()

        print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print("Most popular start station:", popular_start_station)

    # display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print("Most popular End station:", popular_end_station)


    # display most frequent combination of start station and end station trip
    df['frequent_combination']=df['Start Station']+' and '+df['End Station']
    frequent_combination=df['frequent_combination'].value_counts().idxmax()
    print("Most frequent combination of start station and end station trip:", frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['End Time'] =pd.to_datetime(df['End Time'])
    # display total travel time
    df['total_time']=df['End Time']-df['Start Time']
    total_time=df['total_time'].sum()
    print('Total travel time: ',total_time)

    # display mean travel time
    mean_time=df['total_time'].mean()
    print('Mean travel time: ',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()

    print('user_types: \n',user_types)


    # Display counts of gender
    if city != 'washington':
        Gender_counts = df['Gender'].value_counts()

        print('counts of gender: \n',Gender_counts)


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    try:
        while True:
            answer=input('Are you interested in viewing indivisual trip data? Enter yes or no.\n')
            if answer.lower()!= 'yes':
                break
            else:
                while True:
                    print(df.head(5))
                    more=input('Would you like to view more trip data? Enter yes or no.\n')
                    if more.lower()!= 'yes':
                        break
            break

    except Exception as e:
        print("Exception occurred: {}".format(e))



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_data(df)

        try:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except Exception as e:
            print("Exception occurred: {}".format(e))

if __name__ == "__main__":
	main()
