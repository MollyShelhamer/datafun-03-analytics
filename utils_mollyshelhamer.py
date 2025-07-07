"""
File: utils_mollyshelhamer.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Molly Shelhamer

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics


#####################################
# Declare Global Variables
#####################################

# declare a boolean variables (have a value True or False)
has_municipal_clients: bool = True
has_international_clients: bool = True

# declare integer variables
number_of_employees: int = 50
years_in_operation: int = 10

# declare a floating point variables
average_deliverable_turnaround_hours: float = 4.7
average_client_satisfaction: float = 4.7

# declare lists of strings
map_types_offered: list = ["Permit", "Location", "Utility"]
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# declare lists of numbers to illustrate statistics skills
permit_acceptance_rate: list = [89.3, 92.9, 94.5, 84.1, 91.8]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Calculate basic statistics using built-in Python functions and the statistics module
min_score: float = min(permit_acceptance_rate)  
max_score: float = max(permit_acceptance_rate)  
mean_score: float = statistics.mean(permit_acceptance_rate)  
stdev_score: float = statistics.stdev(permit_acceptance_rate)

# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
PA Permits: Making Quality Maps
---------------------------------------------------------
Has Municipal Clients:      {has_municipal_clients}
Number of Employees:        {number_of_employees}
Map Types Offered:          {map_types_offered}
Permit Acceptance Rates:    {permit_acceptance_rate}
Minimum Acceptance Rate:    {min_score}
Maximum Acceptance Rate:    {max_score}
Mean Acceptance Rate:       {mean_score:.2f}
Standard Deviation of Acceptance Rates: {stdev_score:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_case.py")
    print(get_byline())
    print("END main() in utils_case.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()