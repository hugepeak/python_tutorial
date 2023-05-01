import csv

# Function to read a CSV file
def read_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Function to modify CSV data
def modify_csv(data):
    for row in data:
        # Modify the data here (e.g., change a specific column value)
        # For example, changing the first column value to uppercase
        row[0] = row[0].upper()

# Function to save data to a CSV file
def save_csv(file_name, data):
    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
    print("CSV file saved successfully!")

# Example usage
file_name = 'example.csv'

# Read the CSV file
csv_data = read_csv(file_name)

# Modify the CSV data
modify_csv(csv_data)

# Save the modified data to a new CSV file
new_file_name = 'modified_example.csv'
save_csv(new_file_name, csv_data)
