
from . import utils

def spatial_dims(da, **kwargs):
    valid = ['lon', 'lat', 'rlon', 'rlat', 'x', 'y']
    spatial_coords = []
    for coord in da.coords:
        if coord in valid:
            spatial_coords.append(coord)
    return spatial_coords


def fldmean_da(da, **kwargs):
    """field mean of a DataArray.
    """
    if 'dim' not in kwargs:
        kwargs['dim'] = spatial_dims(da)
    if len(kwargs['dim']) == 2:
        return da.mean(**kwargs)
    else:
        return None

def fldmean_ds(ds, varname, **kwargs):
    result = ds.copy(deep=True)
    for data_var, da in ds.items():
        print(data_var)
        fldmean = fldmean_da(da, **kwargs)
        if utils.is_dataarray(fldmean):
            result[data_var] = fldmean
    return result

