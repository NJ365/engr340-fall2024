import sys
import numpy as np
import pandas as pd

def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    # Find the length of the data list
    data_range = len(data)

    # For loop to iterate through the list to find the first instance with "Harrisonburg city"
    for index in range(0,data_range):

        # Check to see if second item is Harrisonburg city
        if data[index][1] == "Harrisonburg city":

            # If true, print out the date and number of cases
            print("Harrisonburg's first case was on " + data[index][0] + ", with " + str(data[index][3]) + " case(s).")

            # Stop searching through as the first day has been found
            break

    # Same methodology as for loop above for Rockingham
    for index in range(0,data_range):

        # Include a check for the State as there are multiple Rockingham counties
        if data[index][1] == "Rockingham" and data[index][2] == "Virginia":

            print("Rockingham's first case was on " + data[index][0] + ", with " + str(data[index][3]) + " case(s).\n")

            break

    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    data_range = len(data)

    # Create a new list that will only contain the days for Harrisonburg
    HBurg_list = []

    # For loop to iterate through the list to find the all days for Harrisonburg city
    # and add to HBurg_list
    for index in range(0,data_range):

        # Check to see if second item is Harrisonburg city
        if data[index][1] == "Harrisonburg city":

            # Add tuple to the end of list
            HBurg_list.append(data[index])

    # Find the total number of tuples in HBurg_list
    # To be used to look through this list
    HBurg_list_length = len(HBurg_list)

    # Variables that will define the characteristics of the worst day
    HBurg_new_cases_max = 0     # Total new cases of the worst day
    HBurg_new_cases_day = 0     # New cases on a given day (used in loop)
    HBurg_worst_day_index = 0   # Worst day's index in HBurg_List
    HBurg_worst_day = ''        # Date of the worst day

    # Iterate through the HBurg_List and find the number of new cases per day
    for index in range (1, HBurg_list_length):

        # Number of cases on day
        day = HBurg_list[index][3]

        # Number of cases on day before
        previous_day = HBurg_list[index - 1][3]

        # Difference between day and previous day -> change in cases -> number of new cases
        HBurg_new_cases_day = day - previous_day

        # Check to see if the number of new cases for the day is greater than the previously
        # found max number of new cases
        if HBurg_new_cases_day > HBurg_new_cases_max:

            # Update characteristic variables
            HBurg_new_cases_max = HBurg_new_cases_day
            HBurg_worst_day_index = index
            HBurg_worst_day = HBurg_list[index][0]


    # Same methodology as Harrisonburg section

    # Create a new list that will only contain the days for Rockingham
    Rock_list = []

    # For loop to iterate through the list to find the all days for Rockingham Virginia
    # and add to Rock_list
    for index in range(0,data_range):

        # Check to see if second item is Rockingham Virginia
        if data[index][1] == "Rockingham" and data[index][2] =="Virginia":

            # Add tuple to the end of list
            Rock_list.append(data[index])

    # Find the total number of tuples in Rock_list
    # To be used to look through this list
    Rock_list_length = len(Rock_list)

    # Variables that will define the characteristics of the worst day
    Rock_new_cases_max = 0      # Total new cases of the worst day
    Rock_new_cases_day = 0      # New cases on a given day (used in loop)
    Rock_worst_day_index = 0    # Worst day's index in Rock_List
    Rock_worst_day = ''         # Date of the worst day

    # Iterate through the HBurg_List and find the number of new cases per day
    for index in range (1, Rock_list_length):

        # Number of cases on day
        day = Rock_list[index][3]

        # Number of cases on day before
        previous_day = Rock_list[index - 1][3]

        # Difference between day and previous day -> change in cases -> number of new cases
        Rock_new_cases_day = day - previous_day

        # Check to see if the number of new cases for the day is greater than the previously
        # found max number of new cases
        if Rock_new_cases_day > Rock_new_cases_max:

            # Update characteristic variables
            Rock_new_cases_max = Rock_new_cases_day
            Rock_worst_day_index = index
            Rock_worst_day = Rock_list[index][0]

    # Print out results for Harrisonburg and Rockingham
    print("Harrisonburg's worst day was " + HBurg_worst_day + ", with " + str(HBurg_new_cases_max) + " new cases.")
    print("Rockingham's worst day was " + Rock_worst_day + ", with " + str(Rock_new_cases_max) + " new cases.\n")

    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    data_range = len(data)

    # Create a new list that will only contain the days for Harrisonburg
    HBurg_list = []

    # For loop to iterate through the list to find the all days for Harrisonburg city
    # and add to HBurg_list
    for index in range(0,data_range):

        # Check to see if second item is Harrisonburg city
        if data[index][1] == "Harrisonburg city":

            # Add tuple to the end of list
            HBurg_list.append(data[index])

    # Find the length of HBurg_list and reduce the length by three
    # Because the later for loop looks at a 7 day window
    # Strarting at 0 with +- 3 on either side
    HBurg_list_length = len(HBurg_list) - 3

    # Variables that will define the characteristics of the worst day
    HBurg_new_cases_max = 0     # Total new cases of the worst day
    HBurg_new_cases_day = 0     # New cases on a given day (used in loop)
    HBurg_worst_day_index = 0   # Worst day's index in HBurg_List
    HBurg_worst_day = ''        # Date of the worst day

    # Iterate through HBurg_list starting at day "4", index 3
    # Because this is the first variable to capture a whole week
    # Each loop looks at a one week range
    for index in range (3, HBurg_list_length):

        # Find the total number of new cases to the left and right of index
        for indc in range (-3, 3):

            # Number of cases on a day
            day = HBurg_list[index + indc][3]

            # Number of cases on the day before
            previous_day = HBurg_list[index + indc - 1][3]

            # Sum the total cases for the week
            HBurg_new_cases_day += day - previous_day

        # Check to see if the number of new cases for the week is greater than the previously
        # found max number of new cases
        if HBurg_new_cases_day > HBurg_new_cases_max:

            # Update characteristic variables
            HBurg_new_cases_max = HBurg_new_cases_day
            HBurg_worst_day_index = index
            HBurg_worst_day = HBurg_list[index][0]

        # Reset the total number of new cases for a given week
        HBurg_new_cases_day = 0

    # Same methodology as Harrisonburg section

    # Create a new list that will only contain the days for Harrisonburg
    Rock_list = []

    # For loop to iterate through the list to find the all days for Harrisonburg city
    # and add to HBurg_list
    for index in range(0, data_range):

        # Check to see if second item is Rockingham Virginia
        if data[index][1] == "Rockingham" and data[index][2] =="Virginia":

            # Add tuple to the end of list
            Rock_list.append(data[index])

    # Find the length of HBurg_list and reduce the length by three
    # Because the later for loop looks at a 7 day window
    # Strarting at middle day, index = 0, with +- 3 on either side
    Rock_list_length = len(Rock_list) - 3

    # Variables that will define the characteristics of the worst day
    Rock_new_cases_max = 0      # Total new cases of the worst day
    Rock_new_cases_day = 0      # New cases on a given day (used in loop)
    Rock_worst_day_index = 0    # Worst day's index in Rock_List
    Rock_worst_day = ''         # Date of the worst day

    for index in range (4, Rock_list_length):
        for indc in range(-3, 3):
            day = Rock_list[index + indc][3]
            previous_day = Rock_list[index + indc - 1][3]

            Rock_new_cases_day += day - previous_day

        if Rock_new_cases_day > Rock_new_cases_max:
            Rock_new_cases_max = Rock_new_cases_day
            Rock_worst_day_index = index
            Rock_worst_day = Rock_list[index][0]
        Rock_new_cases_day = 0

    HBurg_start = HBurg_list[HBurg_worst_day_index - 3][0]

    HBurg_end = HBurg_list[HBurg_worst_day_index + 3][0]

    Rock_start = Rock_list[Rock_worst_day_index - 3][0]

    Rock_end = Rock_list[Rock_worst_day_index + 3][0]

    print("Harrisonburg's worst week was from " + HBurg_start + " to " + HBurg_end + ", with " + str(HBurg_new_cases_max) + " new cases.")
    print("Rockingham's worst week was from " + Rock_start + " to " + Rock_end + ", with " + str(Rock_new_cases_max) + " new cases.")

    return

    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    dummy = 3

    #for (date, county, state, cases, deaths) in data:
        #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


