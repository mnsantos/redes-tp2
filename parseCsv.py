import csv
import sys

#----------------------------------------------------------------------
def csv_reader(file_obj, file):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
    	print >>file, row[1]+"-"+row[5]+" "+row[4]
        

 
#----------------------------------------------------------------------
if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f_obj:
    	file=open(sys.argv[1]+"_bar_zscore.csv", "w")
        csv_reader(f_obj, file)