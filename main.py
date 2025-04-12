from log_parser import LogParser  # Importing the LogParser class from log_parser.py

def main():
    # Initialize the LogParser with the path to the log file
    parser = LogParser('sample_log.txt')
    
    # Load the log file into memory
    parser.load_logs()
    
    # Extract log entries from the loaded logs
    entries = parser.extract_entries()
    
    # Generate a summary of log entries grouped by log level
    summary = parser.count_by_level(entries)

    # Display a summary of log levels and their counts
    print("\n📝 Log Summary:")
    for level, count in summary.items():
        print(f" - {level}: {count} entries")

    # Prompt the user to filter log entries by a specific log level
    level_to_filter = input("\n🔧 Enter log level to filter (e.g., ERROR), or press Enter to skip: ").strip()
    filtered_log_entries = entries  # Start with all entries
    if level_to_filter:
        # Filter the entries by the specified log level
        filtered_log_entries = parser.filter_by_level(entries, level_to_filter)
        print(f"\n🔎 Showing only {level_to_filter.upper()} entries")

    # Prompt the user to filter log entries by a specific message
    message_to_filter = input("\n🔍 Enter a keyword to filter messages, or press Enter to skip: ").strip()
    filtered_message_entries = entries
    if message_to_filter:
        # Filter the entries by the specified message
        filtered_message_entries = parser.filter_by_message(entries, message_to_filter)
        print(f"\n🔍 Showing entries containing '{message_to_filter}'")

    # Display the detailed filtered log entries
    print("\n🔍 Detailed Log Entries:")
    for entry in filtered_log_entries:
        print(f"[{entry['timestamp']}] {entry['level']} - {entry['message']}")
    
     # Display the detailed filtered message entries
    print("\n🔍 Detailed Log Entries:")
    for entry in filtered_message_entries:
        print(f"[{entry['timestamp']}] {entry['level']} - {entry['message']}")
    

    # Export the filtered or unfiltered log entries to a CSV file
    parser.export_to_csv(filtered_message_entries)
    print("\n📁 Filtered entries exported to log_output.csv")
    

if __name__ == '__main__':
    # Entry point of the script
    main()
