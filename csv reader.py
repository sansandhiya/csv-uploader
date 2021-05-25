import pandas as pd 
import os 
import glob 
path = os.getcwd() 
csv_files = glob.glob(os.path.join(path, "data.csv")) 
for i in csv_files:
	df = pd.read_csv(i)
	print(df)