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

    for index in range(0,data_range):
    # For loop to iterate through the list to find the first tuple with Harrisonburg city in it

        tuple = data[index]         # Create tuple variable from the index of the data
        if tuple[1] == "Harrisonburg city":     # Check to see if second item is Harissonburg city
            # If true, print out the date and number of cases
            print("Harrisonburg's first case was on " + tuple[0] + ", with " + str(tuple[3]) + " case(s).")
            break

    for index in range(0,data_range):
    # Same methodology as for loop above
        tuple = data[index]
        if tuple[1] == "Rockingham" and tuple[2] == "Virginia":
            print("Rockingham's first case was on " + tuple[0] + ", with " + str(tuple[3]) + " case(s).\n")
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
    HBurg_list = []

    for index in range(0,data_range):
    # For loop to iterate through the list to find the first tuple with Harrisonburg city in it

        tuple = data[index]         # Create tuple variable from the index of the data
        if tuple[1] == "Harrisonburg city":     # Check to see if second item is Harissonburg city
            HBurg_list.append(tuple)

    HBurg_list_length = len(HBurg_list)

    HBurg_new_cases_max = 0
    HBurg_new_cases_day = 0
    HBurg_worst_day_index = 0
    HBurg_worst_day = ''

    for index in range (1, HBurg_list_length):
        tuple_day = HBurg_list[index]
        tuple_previous_day = HBurg_list[index - 1]

        day = tuple_day[3]
        previous_day = tuple_previous_day[3]

        HBurg_new_cases_day = day - previous_day

        if HBurg_new_cases_day > HBurg_new_cases_max:
            HBurg_new_cases_max = HBurg_new_cases_day
            HBurg_worst_day_index = index
            HBurg_worst_day = tuple_day[0]

    Rock_list = []

    for index in range(0,data_range):
    # For loop to iterate through the list to find the first tuple with Harrisonburg city in it

        tuple = data[index]         # Create tuple variable from the index of the data
        if tuple[1] == "Rockingham" and tuple[2] =="Virginia":     # Check to see if second item is Harissonburg city
            Rock_list.append(tuple)

    Rock_list_length = len(Rock_list)

    Rock_new_cases_max = 0
    Rock_new_cases_day = 0
    Rock_worst_day_index = 0
    Rock_worst_day = ''

    for index in range (1, Rock_list_length):
        tuple_day = Rock_list[index]
        tuple_previous_day = Rock_list[index - 1]

        day = tuple_day[3]
        previous_day = tuple_previous_day[3]

        Rock_new_cases_day = day - previous_day

        if Rock_new_cases_day > Rock_new_cases_max:
            Rock_new_cases_max = Rock_new_cases_day
            Rock_worst_day_index = index
            Rock_worst_day = tuple_day[0]

    print("Harrisonburg's worst day was " + HBurg_worst_day + ", with " + str(HBurg_new_cases_max) + " new cases.")
    print("Rockingham's worst day was " + Rock_worst_day + ", with " + str(Rock_new_cases_max) + " new cases.\n")

    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    data_range = len(data)
    HBurg_list = []

    for index in range(0,data_range):
    # For loop to iterate through the list to find the first tuple with Harrisonburg city in it

        tuple = data[index]         # Create tuple variable from the index of the data
        if tuple[1] == "Harrisonburg city":     # Check to see if second item is Harissonburg city
            HBurg_list.append(tuple)

    HBurg_list_length = len(HBurg_list) - 3

    HBurg_new_cases_max = 0
    HBurg_new_cases_day = 0
    HBurg_worst_day_index = 0
    HBurg_worst_day = ''

    for index in range (4, HBurg_list_length):
        for indc in range (-3, 3):
            tuple_day = HBurg_list[index + indc]
            tuple_previous_day = HBurg_list[index + indc - 1]

            day = tuple_day[3]
            previous_day = tuple_previous_day[3]

            HBurg_new_cases_day += day - previous_day

        if HBurg_new_cases_day > HBurg_new_cases_max:
            HBurg_new_cases_max = HBurg_new_cases_day
            HBurg_worst_day_index = index
            HBurg_worst_day = tuple_day[0]
        HBurg_new_cases_day = 0

    Rock_list = []

    for index in range(0, data_range):
    # For loop to iterate through the list to find the first tuple with Harrisonburg city in it

        tuple = data[index]         # Create tuple variable from the index of the data
        if tuple[1] == "Rockingham" and tuple[2] == "Virginia":     # Check to see if second item is Harissonburg city
            Rock_list.append(tuple)

    Rock_list_length = len(Rock_list) - 3

    Rock_new_cases_max = 0
    Rock_new_cases_day = 0
    Rock_worst_day_index = 0
    Rock_worst_day = ''

    for index in range (4, Rock_list_length):
        for indc in range(-3, 3):
            tuple_day = Rock_list[index + indc]
            tuple_previous_day = Rock_list[index + indc - 1]

            day = tuple_day[3]
            previous_day = tuple_previous_day[3]

            Rock_new_cases_day += day - previous_day

        if Rock_new_cases_day > Rock_new_cases_max:
            Rock_new_cases_max = Rock_new_cases_day
            Rock_worst_day_index = index
            Rock_worst_day = tuple_day[0]
        Rock_new_cases_day = 0

    HBurg_start_tuple = HBurg_list[HBurg_worst_day_index - 3]
    HBurg_start = HBurg_start_tuple[0]

    HBurg_end_tuple = HBurg_list[HBurg_worst_day_index + 3]
    HBurg_end = HBurg_end_tuple[0]

    Rock_start_tuple = Rock_list[Rock_worst_day_index - 3]
    Rock_start = Rock_start_tuple[0]

    Rock_end_tuple = Rock_list[Rock_worst_day_index + 3]
    Rock_end = Rock_end_tuple[0]

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


