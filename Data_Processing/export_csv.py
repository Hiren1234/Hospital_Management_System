# Now I have exproted the file
import pandas as pd
import os

from Data_Processing.clean_data import df

os.makedirs("Output", exist_ok=True)

df.to_csv("Output/patient_data.csv", index=False)
print("CSV exported Successfully")
