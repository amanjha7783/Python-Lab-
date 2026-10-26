import xarray as xr

file = "sample.nc"

ds = xr.open_dataset(file)

print(ds)