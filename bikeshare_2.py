import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New york city': 'new_york_city.csv',
              'Washington': 'washington.csv' }




def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    global city
    global month
    global day

    while True:
        city = input('Please select a city (chicago, new york city, washington) ').capitalize()
    
        if city == 'Chicago' or city == 'New york city' or city == 'Washington':
            break
        else:
            print("Please enter a valid answer")
            continue

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('Please select a month (all, january, february, ... , june) ').capitalize()
    
        if month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May'or month == 'June' or month =='All':
            break
        else:
            print("Please enter a valid answer")
            continue
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
# Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday
    while True:
        day = input('Please select a day of a week  (all, monday, tuesday, ... sunday) ').capitalize()
        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday'or day == 'All' :
            break
        else:
            print("Please enter a valid answer")
            continue
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month == 'All':
        if day == 'All':
            return df
        else:
            df = df[df['day_of_week'] == day]
            return df 
    else:
        if day =='All':
            df = df[df['month'] == month]
            return df
        else:
            df = df[df['month'] == month]
            df = df[df['day_of_week'] == day]
            return df

    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'All' :
        common_month = df['month'].value_counts().idxmax()
        count_1=df['month'].value_counts()[common_month]
        print('Most common month:', common_month)
        print('count: ' ,count_1)

    # display the most common day of week
    if day == 'All' : 
        common_day = df['day_of_week'].value_counts().idxmax()
        count_2=df['day_of_week'].value_counts()[common_day]
        print('Most common day:', common_day)
        print('count: ' ,count_2)

    # display the most common start hour
    common_hour = df['hour'].value_counts().idxmax()
    count_3=df['hour'].value_counts()[common_hour]
    print('Most Frequent Start Hour:', common_hour)
    print('count: ' ,count_3)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start = df['Start Station'].value_counts().idxmax()
    count_1 = df['Start Station'].value_counts()[common_start]
    print('Most common used start station:', common_start)
    print('count: ' ,count_1)

    # display most commonly used end station

    common_end = df['Start Station'].value_counts().idxmax()
    count_2 = df['End Station'].value_counts()[common_end]
    print('Most common used End station:', common_end)
    print('count: ' ,count_2)

    # display most frequent combination of start station and end station trip

    common_station = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('Most frequent combination of start and end stations trip \n :', common_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("Total travel time: ",total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: ",mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    Count_user = df['User Type'].value_counts()
    print(Count_user)

    # Display counts of gender
    if city == 'Chicago' or city == 'New york city':
        Count_gender = df['Gender'].value_counts()
        print(Count_gender)

    # Display earliest, most recent, and most common year of birth
    if city == 'Chicago' or city == 'New york city':
        most_earliest=df['Birth Year'].min()
        print("Most earliest birth year: ",most_earliest)
        
        most_recent=df['Birth Year'].max()
        print("Most recent birth year: ",most_recent)
        most_common_year=df['Birth Year'].value_counts().idxmax()
        print("Most common year of birth: ",most_common_year)

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
