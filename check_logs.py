# Open the log file in read mode
with open('visitor_ips.log', 'r') as file:
    # Read all lines in the file
    log_data = file.readlines()

# Print each line (log entry)
ip_list = set()
for entry in log_data:
    ip_list.add(entry)

for ip in ip_list:
    print(ip)