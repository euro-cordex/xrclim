
import xarray as xr


def is_dataset(data):
    if type(data) is xr.core.dataset.Dataset:
        return True
    else:
        return False

def is_dataarray(data):
    if type(data) is xr.core.dataarray.DataArray:
        return True
    else:
        return False

