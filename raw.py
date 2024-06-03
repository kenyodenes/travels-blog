import pandas as pd
import csv
# Function to parse rows based on event type
def parse_row(row):
    event_type = row[1]
    if event_type == 'buy':
        return {
            'Date_Time': row[0],
            'Event_Type': row[1],
            'User_Id': row[2],
            'Price': row[3]
        }
    elif event_type == 'subscribe':
        return {
            'Date_Time': row[0],
            'Event_Type': row[1],
            'User_Id': row[2]
        }
    elif event_type == 'read':
        if len(row) == 6:
            return {
                 'Date_Time': row[0],
                 'Event_Type': row[1],
                'Country': row[2],
                'User_Id': row[3],
                'Source': row[4],
                'Topic': row[5]
            }
        elif len(row) == 5:
            return {
                'Date_Time': row[0],
                'Event_Type': row[1],
                'Country': row[2],
                'User_Id': row[3],
                'Topic': row[4]
            }
    return None


# List to hold each row's data dictionary
data_raw = []
# Path to the CSV file
file_path = '/content/data.csv'
# Read and parse the CSV file
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        row_data = parse_row(row)
        if row_data:
            data_raw.append(row_data)
# Convert list of dictionaries to DataFrame
data = pd.DataFrame(data_raw)
# Display the DataFrame
print(data.head())
