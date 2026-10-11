"""
RECORD CHECK  -  my version
===========================

Name  :  Nunkoo Sufyaan
Lane  :  AI 
Date  :  10/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# function that returns 'status'
def status_of(percent):
    if percent >= 100:
        return("OVER LIMIT")
    elif percent >= 90:
        return("WARNING")
    else:
        return("OK")

# function that returns difference and percent
def check(rows_loaded, rows_expected):
    difference = rows_loaded - rows_expected
    percentage = ((rows_loaded/rows_expected)*100)
    return difference, percentage

# function that outputs everything
def print_report(label, rows_loaded, rows_expected, difference, percentage, status):
    print(f"rows_loaded      :   {rows_loaded:>10.2f}")
    print(f"rows_expected    :   {rows_expected:>10.2f}")
    print(f"difference       :   {difference:>10.2f}")
    print(f"percent          :   {percentage:>10.2f}%")
    print(f"status           :   {status:>10}")
    


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

dataset_name = input("enter the dataset name: ")
rows_loaded = float (input("enter the number of rows loaded: "))
rows_expected = float(input("enter the number of rows expected: "))


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.


# function 'check' is called with parameter 'rows_loaded' and 'rows_expected' 
difference, percentage = check(rows_loaded, rows_expected)  

# function 'status_of' is called with parameter 'percentage'
status = status_of(percentage)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

# global variable 'over_limit_count' ,that keeps tracks of OVER LIMIT records, is defined and initialised to 0
over_limit_count = 0

# the label 'quit' to stop or not is entered in variable 'message'
message = input("enter 'quit' if you want program to stop or type anything else to continue: ")
while message != "quit":

    label = input("enter the name of the label: ")
    dataset_name = input("enter the dataset name: ")
    rows_loaded = float (input("enter the number of rows loaded: "))
    rows_expected = float(input("enter the number of rows expected: "))

    difference, percentage = check(rows_loaded, rows_expected)
    status = status_of(percentage)

    if status == "OVER LIMIT":
        over_limit_count +=1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print_report(label, rows_loaded, rows_expected, difference, percentage, status)

    print("=" * 34)

    # 'message' appears after each cycle to verify if the program needs to end
    message = input("enter 'quit' if you want program to stop or type anything else to continue: ")


print (over_limit_count, " records have OVER LIMIT percentages.") 


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
