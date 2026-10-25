"""
RECORD CHECK  -  my version
===========================

Name  :  Nunkoo Sufyaan
Lane  :  AI 
Date  :  24/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

class Record:
    def __init__(self, dataset_name, rows_loaded, rows_expected):
        """method that initialises the respective attrubutes to its specific objects"""
        self.dataset_name = dataset_name
        self.rows_loaded = rows_loaded
        self.rows_expected = rows_expected

    def status(self):
        """this method calculates 'rows_loaded' as a percentage of 'rows_expected' and returns the status of the record in the object"""
        percent = ((self.rows_loaded/self.rows_expected)*100)
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

    over_limit_count = 0


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

# creating my own data file named 'my_own_data_file.txt' and populated with my own data
with open ("my_own_data_file.txt", "w") as f:
    f.write(f"survey-2009, 84, 3993\n")
    f.write(f"survey-2010, 2882, 3990\n")
    f.write(f"survey-2011, 7229, 292\n")
    f.write(f"survey-2012, 822, 89389\n")
    f.write(f"survey-2013, 8412, 39931\n")
    f.write(f"survey-2017, 8128, 23932\n")
    f.write(f"survey-2018, 7127, 39312\n")
    f.write(f"survey-2020, 21812, 1233\n")
    f.write(f"survey-2022, 282, 3921\n")
    f.write(f"survey-2023, 2198, 123\n")
    f.write(f"survey-2025, 292, 38121")


records = [] 
def load_records(path):
    """function that takes record lines from a file and converts them into a list of objects of class 'Record'"""
    try:
        with open (path) as f:
            for line in f:
                dataset_name, rows_loaded, rows_expected = line.strip().split(",")
                records.append(Record(dataset_name, float(rows_loaded), float(rows_expected)))
            return records
    except FileNotFoundError:
        print(f"{path} has not been found")
        return (records)
            
load_records("my_own_data_file.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.dataset_name}")
    print("=" * 34)

    print(f"dataset name : {record.dataset_name:>10}")
    print(f"rows_loaded  : {record.rows_loaded:>10}")
    print(f"dataset name : {record.rows_expected:>10}")
    print(f"status       : {record.status():>10}")

    print("=" * 34)

    if record.status() == "OVER LIMIT":
        Record.over_limit_count += 1

print (f"{Record.over_limit_count} records are OVER LIMIT")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
