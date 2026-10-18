"""
RECORD CHECK  -  my version
===========================

Name  :  Nunkoo Sufyaan
Lane  :  AI
Date  :  17/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.


def check_record(rows_loaded, rows_expected):
    """function that returns difference, percent and status"""
    difference = rows_loaded - rows_expected
    percentage = ((rows_loaded/rows_expected)*100)
    if percentage >=100:
        status = "OVER LIMIT"
    else:
        status = "OK"
    return difference, percentage, status

def print_report(rows_loaded, rows_expected, difference, percentage, status):
    """function that outputs everything"""
    print(f"rows_loaded      :   {rows_loaded:>10.2f}")
    print(f"rows_expected    :   {rows_expected:>10.2f}")
    print(f"difference       :   {difference:>10.2f}")
    print(f"percent          :   {percentage:>10.2f}%")
    print(f"status           :   {status:>10}\n")


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

# records is initialised as an empty list
records = []   
# global variable 'status' is initialised as an empty string
status = ""

# my own data file named 'my_data_file' has been created and populated with 5 lines of data
with open("my_data_file.txt","w") as f:
    f.write(f"survey-2020, 432, 3424\n")
    f.write(f"survey-2022, 863, 9793\n")
    f.write(f"survey-2024, 237, 872\n")
    f.write(f"survey-2025, 2772, 822\n")
    f.write(f"survey-2026, 7282, 828\n")

def load_records(path):
    """function that tries to open a given file using its relative path and returns an appropriate message if file does not exist"""
    try:
        with open(path) as f:
            for line in f:
                dataset_name, rows_loaded, rows_expected = line.strip().split(",")
                records.append({"dataset_name": dataset_name, "rows_loaded": float(rows_loaded), "rows_expected": float(rows_expected)})
            return records

    except FileNotFoundError:
        print(path, " was not found")
        print([])

load_records("my_data_file.txt")

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# global variable 'count_OVERLIMIT' is initialised to 0
count_OVERLIMIT = 0

with open("new_records.txt", "w") as f:

    for i in range(len(records)):
        difference, percent, status = check_record(records[i]["rows_loaded"], records[i]["rows_expected"])
        if status == "OVER LIMIT":
            count_OVERLIMIT +=1
        print_report(records[i]["rows_loaded"], records[i]["rows_expected"], difference, percent, status)
        f.write(f"{records[i]["dataset_name"]}, {status}\n")


print(count_OVERLIMIT, "records have over-limit percentages")



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
