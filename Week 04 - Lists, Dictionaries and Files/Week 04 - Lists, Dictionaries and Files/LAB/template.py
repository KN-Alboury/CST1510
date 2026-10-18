"""
RECORD CHECK  -  my version
===========================

Name  : Khadja Alboury Ndiaye
Lane  :  AI
Date  : 14/10/2026

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

def check_record(value, limit):
    """Return the difference, percent, and status"""
    difference = value - limit
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, difference, percent, status):
    """Print the report"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  Difference:\t{difference:>10.2f}")
    print(f"  Percent:\t{percent:>10.2f}")
    print(f"  Status:\t{status:>10}")
    print("=" * 34)


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

records = [
       {"label": "R-001", "value": 50.0, "limit": 100.0},
       {"label": "R-002", "value": 90.0, "limit": 100.0},
       {"label": "R-003", "value": 150.0, "limit": 100.0},
   ]

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], difference, percent, status)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
