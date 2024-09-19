import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as py
from google.colab import files

# Step 1: Upload the file
uploaded = files.upload()

# Step 2: Extract the uploaded file name
uploaded_file_name = list(uploaded.keys())[0]

# Step 3: Check the file type by inspecting the first few lines
try:
    # Try reading it as a text file to detect the format
    with open(uploaded_file_name, 'r') as file:
        content = file.readlines()[:10]
        print("File format check (first 10 lines):")
        print(''.join(content))  # Print the first 10 lines of the file

        # If we detect commas or tabs, handle accordingly
        if ',' in content[0]:
            print("\nDetected CSV format.")
            df = pd.read_csv(uploaded_file_name)
        elif '\t' in content[0]:
            print("\nDetected TSV format.")
            df = pd.read_csv(uploaded_file_name, delimiter='\t')
        else:
            print("\nFile format is unclear from inspection. Proceeding with Excel check.")
except:
    print("File is not a plain text file, proceeding with Excel.")

# Step 4: If it's not CSV or TSV, try to load it as an Excel file
try:
    # First attempt to read as .xls using xlrd engine
    df = pd.read_excel(uploaded_file_name, engine='xlrd')
    print("\nLoaded as an .xls file using xlrd.")
except Exception as e_xls:
    print(f"Could not load as .xls: {e_xls}")

    try:
        # If .xls fails, try to read as .xlsx using openpyxl
        !pip install openpyxl  # Ensure openpyxl is installed for .xlsx files
        df = pd.read_excel(uploaded_file_name, engine='openpyxl')
        print("\nLoaded as an .xlsx file using openpyxl.")
    except Exception as e_xlsx:
        print(f"Could not load as .xlsx: {e_xlsx}")
        print("\nError: Unable to load the file. Please ensure it's a valid CSV, TSV, or Excel file.")

# Step 5: Display the first few rows of the DataFrame
if 'df' in locals():  # Check if the DataFrame was successfully loaded
    print("\nData loaded successfully:")
    print(df.head())
else:
    print("\nDataFrame was not loaded.")
