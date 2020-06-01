#bikeshare.py refactoring 1.0
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
    print('Hello! Let\'s explore some US bikeshare data! \n')

 # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input("Enter  city name as  chicago, new york city or washington \n").lower()
        if city not in ('chicago','new york city', 'washington') :
            print("Your city name is not correct , please enter again : \n")
        else :
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month = input("Enter  month as \n  all, january, february, march, april, may, june \n").lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june') :
            print("Your month is not correct , please enter again : \n")
        else :
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("Enter  month as \n  all, monday , tuesday, wednesday ,thursday , friday, saturday, sunday : \n").lower()
        if day  not in ('all', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday','sunday') :
            print("Your day is not correct , please enter again : \n")
        else :
            break
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
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df,city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # TO DO: display the most common month if all month entered
    if(month == 'all'):
        start_time = time.time()
        popular_month = df['month'].mode()[0]
        count_month = max(df['month'].value_counts())
        months = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}
        popular_month= months[popular_month]
        print('Most Popular month:', popular_month.upper() , 'Count : ' , count_month ,'Filter city : {} month: {} : day {}'.format(city.upper(),month.upper(),day.upper()))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    # TO DO: display the most common day of week if all day entered
    if(day == 'all'):
       start_time = time.time()
       popular_day = df['day_of_week'].mode()[0]
       count_day = max(df['day_of_week'].value_counts())
       print('Most Popular day of week:', popular_day.upper(), 'Count : ' , count_day,'Filter city : {} month: {} : day {}'.format(city.upper(),month.upper(),day.upper()))
       print("\nThis took %s seconds." % (time.time() - start_time))
       print('-'*40)

    # TO DO: display the most common start hour
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    count_hour = max(df['hour'].value_counts())
    print('Most Popular hour:', popular_hour ,'Count : ' , count_hour, 'Filter city : {} month: {} : day {} '.format(city.upper(),month.upper(),day.upper()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,city,month,day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    count_start = max(df['Start Station'].value_counts())
    print('Most Popular start station:', popular_start ,'Count : ' , count_start ,'Filter city : {} month: {} : day {}'.format(city.upper(),month.upper(),day.upper()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    start_time = time.time()
    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    count_end = max(df['End Station'].value_counts())
    print('Most Popular end station :', popular_end ,'Count : ' , count_end ,'Filter city : {} month: {} : day {}'.format(city.upper(),month.upper(),day.upper()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    start_time = time.time()
    # TO DO: display most frequent combination of start station and end station trip
    df['CombTrip']= df['Start Station'] + df['End Station']
    popular_combtrip=df['CombTrip'].mode()[0]
    count_combtrip = max(df['CombTrip'].value_counts())
    print('Most Popular combination of start station and end station trip :', popular_combtrip ,'Count : ' , count_combtrip ,'Filter city : {} month: {} : day {}'.format(city.upper(),month.upper(),day.upper()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,city,month,day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()
    # TO DO: display total travel time
    total_duraiton = df['Trip Duration'].sum()
    print('Total Trip Duration:', total_duraiton ,'Filter city : {} month: {} : day {}'.format(city.upper(),month.upper(),day.upper()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    start_time = time.time()
    # TO DO: display mean travel time
    mean_duraiton = df['Trip Duration'].mean()
    print('Mean Trip Duration:', int(mean_duraiton) ,'Filter city : {} month: {} : day {}'.format(city.upper(),month.upper(),day.upper()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df,city,month,day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()
    # TO DO: Display counts of user types
    user_types =  df['User Type'].value_counts()

    for item in user_types.items() :
        print('User Type : ' , item )

    print('\n Filter city : {} month: {} : day {}'.format(city.upper(),month.upper(),day.upper()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    if city in ('chicago','new york city') :
        start_time = time.time()

        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        for item in gender.items():
             print('Gender : ' , item )
        print('\n Filter city : {} month: {} : day {} \n'.format(city.upper(),month.upper(),day.upper()))
        print('-'*40)
        # TO DO: Display earliest, most recent, and most common year of birth
        start_time = time.time()

        #Earlist Birth
        earliest_birth = df['Birth Year'].min()
        print('Earliest Birth Year :', int(earliest_birth) ,'Filter city : {} month: {} : day {} \n'.format(city.upper(),month.upper(),day.upper()))
        print('-'*40)
        #Recent Birt
        recent_birth = df['Birth Year'].max()
        print('Most Recent Birth Year :', int(recent_birth) ,'Filter city : {} month: {} : day {} \n'.format(city.upper(),month.upper(),day.upper()))
        print('-'*40)

        #Most Common Birth
        common_birth = df['Birth Year'].mode()[0]
        print('Most Common Birth Year :',  int(common_birth) ,'Filter city : {} month: {} : day {}'.format(city.upper(),month.upper(),day.upper()))
        print("\nThis took %s seconds." % (time.time() - start_time))


    else :
        print('There is no Gender or birtdate info for washington')

    print('-'*40)

def display_raw(df,city,month,day):
    """Displays raw data of selected filter."""
    print('\nDisplay raw data ...\n')
    count_rows=len(df)
    print('\n Total numbers of rows is : ', count_rows ,'\nFilter city : {} month: {} : day {} \n'.format(city.upper(),month.upper(),day.upper()))
    j=0
    for i in range(len(df)):
        print(df.iloc[[j+1,j+5]])
        j += 5
        print(i,j)
        more5=input("Do you want to see more 5 lines of raw data? yes or no \n").lower()
        if(more5 !='yes'):
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,city,month,day)
        station_stats(df,city,month,day)
        trip_duration_stats(df,city,month,day)
        user_stats(df,city,month,day)
        display_raw(df,city,month,day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
