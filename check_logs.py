# Open the log file in read mode
with open('visitor_ips.log', 'r') as file:
    # Read all lines in the file
    log_data = file.readlines()

# Print each line (log entry)
for entry in log_data:
    print(entry)
