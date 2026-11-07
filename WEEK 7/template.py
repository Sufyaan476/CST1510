"""
RECORD CHECK  -  my version
===========================

Name  :  Nunkoo Sufyaan 
Lane  :  AI 
Date  :  07/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

def parse_line(raw_line):
    """function that takes a line with different information, cleans it and returns it as a dictionary"""
    strip = raw_line.strip()
    datasetname_part, rest = strip.split(",", 1)
    datasetname = datasetname_part.strip().lower()
    rest = rest.lower().split(",")

    dict = {}
    for piece in rest:
        key, value = piece.split("=")
        dict[key.strip()] = float(value.strip())

    dictionary = {"datasetname": datasetname, "age": dict['age'], "rating" :dict['rating']}
    return dictionary

def status_of(rating, age):
    """function that returns the status of the record"""
    if age >= rating:
        return "OK"
    else:
        return "FLAGGED"
     

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

# Creating my own data file called 'my_raw_file.txt' that contains all raw and messy records.  
with open("my_raw_file.txt", "w") as f:
    f.write("  Survey_2026 , rating=4 , age=23  \n")
    f.write("Survey_2025 ,Rating=10 , age=21\n")
    f.write("   Survey_2024 ,   rating=12 ,age=10    \n")
    f.write("    Survey_2023 , Rating=18 , Age=24 \n")
    f.write("Survey_2022 ,    rating=15 ,Age=14       \n")
    f.write(" Survey_2021 ,Rating=21 ,              Age=29    ")


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

# global variable 'count_flagged', used to count the number of 'flagged' records, is initialised to 0.
count_flagged = 0

with open("my_raw_file.txt") as f:
    # Looping through the whole file and storing each record in a dictionary.
    for line in f:
        record = parse_line(line)
        status = status_of(record['rating'], record['age'])
        if status == "FLAGGED":
            count_flagged +=1
        print(f"{record} : {status}")

print(f"{count_flagged} records were flagged.")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
