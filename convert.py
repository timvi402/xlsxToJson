import pandas as pd
import sys

input_file = sys.argv[sys.argv.index('-i') + 1]
output_file = sys.argv[sys.argv.index('-o') + 1]

# Load the Excel file
df = pd.read_excel(input_file, engine='openpyxl')

# Convert the DataFrame to JSON
json_str = df.to_json(orient='records')

# Write the JSON to a file
with open(output_file, 'w') as json_file:
    json_file.write(json_str)
