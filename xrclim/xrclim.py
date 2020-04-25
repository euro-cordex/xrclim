"""Main module."""


from . import core
from . import utils

import pandas as pd

def fldmean(data, varname=None, keep_attrs=True, **kwargs):
    if 'keep_attrs' not in kwargs:
        kwargs['keep_attrs'] = True
    if utils.is_dataset(data):
        return core.fldmean_ds(data, varname, **kwargs)
    elif utils.is_dataarray(data):
        return core.fldmean_da(data, **kwargs)
    else:
        raise Exception('not an xarray dataset or datarray')


def timmean(data, keep_attrs=True, **kwargs):
    if 'keep_attrs' not in kwargs:
        kwargs['keep_attrs'] = True
    return data.mean(dim=['time'], **kwargs)

def monmean(data, keep_attrs=True, **kwargs):
    if 'keep_attrs' not in kwargs:
        kwargs['keep_attrs'] = True
    return data.resample(time='1MS').mean(dim='time', **kwargs)
