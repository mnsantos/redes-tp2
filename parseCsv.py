import csv
import sys
import shlex

#----------------------------------------------------------------------
def csv_reader_zscore(file_obj, file):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        location = shlex.split(row[6])[0]
        if location == "United":
            location = "USA"
        if location == "Argentina":
            location = "ARG"
        print >>file, row[1]+"-"+location+" "+row[4]

def csv_reader_rtt(file_obj, file):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        location = shlex.split(row[6])[0]
        if location == "United":
            location = "USA"
        if location == "Argentina":
            location = "ARG"
        print >>file, row[1]+"-"+location+" "+row[3]
            

 
#----------------------------------------------------------------------
if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f_obj:
        file=open(sys.argv[1]+"_bar_zscore.csv", "w")
        csv_reader_zscore(f_obj, file)
    with open(sys.argv[1], "rb") as f_obj:
        file1=open(sys.argv[1]+"_bar_rtt.csv", "w")
        csv_reader_rtt(f_obj, file1)
