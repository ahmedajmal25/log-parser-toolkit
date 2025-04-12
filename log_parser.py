import re  # Importing the regular expressions module for pattern matching
import csv  # Importing the CSV module for exporting data to CSV files

class LogParser:
    def __init__(self, filepath):
        """
        Initializes the LogParser with the given file path.
        Args:
            filepath (str): Path to the log file.
        """
        self.filepath = filepath
        self.logs = []  # List to store the raw log lines

    def load_logs(self):
        with open(self.filepath, 'r') as f:
            for line in f:
                yield line.strip()


    def extract_entries(self):
        pattern = r'\[(.*?)\] (\w+) - (.*)'
        parsed = []

        for line in self.load_logs():
            match = re.match(pattern, line)
            if match:
                timestamp, level, message = match.groups()
                parsed.append({
                    'timestamp': timestamp,
                    'level': level,
                    'message': message
                })

        return parsed


    def count_by_level(self, entries):
        """
        Counts the number of log entries for each log level.
        Args:
            entries (list): List of parsed log entries.
        Returns:
            dict: A dictionary with log levels as keys and their counts as values.
        """
        count = {}  # Dictionary to store counts by log level
        for entry in entries:
            level = entry['level']  # Get the log level of the entry
            count[level] = count.get(level, 0) + 1  # Increment the count for the level
        return count

    def export_to_csv(self, entries, filename='log_output.csv'):
        """
        Exports the parsed log entries to a CSV file.
        Args:
            entries (list): List of parsed log entries.
            filename (str): Name of the output CSV file (default: 'log_output.csv').
        """
        with open(filename, mode='w', newline='') as csvfile:
            # Define the CSV column headers
            fieldnames = ['timestamp', 'level', 'message']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # Write the header row
            for entry in entries:
                writer.writerow(entry)  # Write each log entry as a row

    def filter_by_level(self, entries, target_level):
        """
        Filters log entries by a specific log level.
        Args:
            entries (list): List of parsed log entries.
            target_level (str): The log level to filter by (e.g., 'INFO', 'ERROR').
        Returns:
            list: A list of log entries matching the target level.
        """
        # Filter entries where the level matches the target level (case-insensitive)
        return [entry for entry in entries if entry['level'] == target_level.upper()]
    def filter_by_message(self, entries, target_message):
        """
        Filters log entries by a specific log message.
        Args:
            entries (list): List of parsed log entries.
            target_message (str): The message to filter by.
        Returns:
            list: A list of log entries containing the target message.
        """
        # Filter entries where the message contains the target message (case-insensitive)
        return [entry for entry in entries if target_message.lower() in entry['message'].lower()]
