import csv
import sys

#----------------------------------------------------------------------
def csv_reader_zscore(file_obj, file):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
    	print >>file, row[1]+"-"+row[5]+" "+row[4]

def csv_reader_rtt(file_obj, file):
	"""
	Read a csv file
	"""
	reader = csv.reader(file_obj)
	for row in reader:
		print >>file, row[1]+" "+row[2]+" "+row[3]
	        

 
#----------------------------------------------------------------------
if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f_obj:
    	file=open(sys.argv[1]+"_bar_zscore.csv", "w")
        csv_reader_zscore(f_obj, file)
    with open(sys.argv[1], "rb") as f_obj:
    	file1=open(sys.argv[1]+"_bar_rtt.csv", "w")
    	csv_reader_rtt(f_obj, file1)
