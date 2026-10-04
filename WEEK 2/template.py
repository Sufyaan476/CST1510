"""
RECORD CHECK  -  my version
===========================

Name  : Nunkoo Sufyaan 
Lane  :  AI      
Date  : 02/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

dataset_name = input ("Enter the dataset name: ")
rows_loaded = float(input("Enter number of rows loaded: "))
rows_expected = float (input("Enter number of rows expected: "))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = rows_loaded - rows_expected
percent = ((rows_loaded/rows_expected)*100)

# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

end_message = "quit"
count_OVERLIMIT = 0
message = input("enter 'quit' if you want to end the program: ")
while message != "quit":
    dataset_name = input ("Enter the dataset name: ")
    rows_loaded = float(input("Enter number of rows loaded: "))
    rows_expected = float (input("Enter number of rows expected: "))
    difference = rows_loaded - rows_expected
    percent = ((rows_loaded/rows_expected)*100)
    if percent >= 100:
        status = "OVER LIMIT"
        count_OVERLIMIT +=1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print ()
    print ("=" * 34)
    print (f"  RECORD CHECK  -  {dataset_name}")
    print ("=" * 34)
    print (f"rows loaded    :   {rows_loaded:>10}")
    print (f"rows expected  :   {rows_expected:>10}")
    print (f"Difference     :   {difference:>10.2f}")
    print (f"Percent        :   {percent:>10.2f}%")
    print (f"Status         :   {status:>10}")
    print ("=" * 34)
    message = input ("enter 'quit' if you want to end the program: ")

print (count_OVERLIMIT, " records had over limit percentages")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
