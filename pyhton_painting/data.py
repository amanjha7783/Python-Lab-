from netCDF4 import Dataset

# Open the file
data = Dataset("sample.nc", "r")

# Show information about the file
print(data)

# List all variables
print(data.variables.keys())

# List dimensions
print(data.dimensions.keys())