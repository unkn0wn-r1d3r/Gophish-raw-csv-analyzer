import csv
import os
from collections import defaultdict

def list_csv_files(directory):
    """List all CSV files in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith('.csv')]

def process_and_merge_csv(directory):
    """Process and merge CSV files from a directory."""
    message_types = ["Email Sent", "Email Opened", "Clicked Link", "Submitted Data"]
    email_data = defaultdict(lambda: {message: 0 for message in message_types})
    total_email_sent = 0

    for csv_file in list_csv_files(directory):
        file_path = os.path.join(directory, csv_file)
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first line (headers)
            next(reader)  # Skip the second line

            for row in reader:
                email = row[1]
                message = row[3]
                if message in message_types:
                    email_data[email][message] += 1
                    if message == "Email Sent":
                        total_email_sent += 1

    result = [{'email': email, **counts} for email, counts in email_data.items()]
    result.append({'Total Email Sent': total_email_sent})
    return result

# Replace 'path_to_your_directory' with the actual directory path
directory_path = input("Enter the CSV File Dir: ")
output = process_and_merge_csv(directory_path)
print(output)
