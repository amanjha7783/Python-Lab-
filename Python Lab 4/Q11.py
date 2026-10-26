# Write a python script to print the current date and time

from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the current date and time
print("Current Date and Time:", current_time)
