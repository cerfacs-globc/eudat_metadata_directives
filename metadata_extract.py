# -*- coding: latin-1 -*-

#  Copyright CERFACS (http://cerfacs.fr/)
#  Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
#
#  Author: Christian Page (2017)

import json
from netCDF4 import Dataset, MFDataset

def netcdf_md_extract(in_file,
                      var_name,
                      md_list_file,
                      out_file
                      ):

# Extract list of Metadata Attributes to extract
    with open(md_list_file) as data_file:    
        md_list = json.load(data_file)

# Initialize output dict
    md_out = { "metadata": { "global": {}, var_name: {} } }

# Open NetCDF input file to parse
    srcfile = Dataset(in_file)

# Go through global attributes first, and extract
    for key, value in md_list["metadata"]["global"].items():
        if (value == True):
            try:
                md_out["metadata"]["global"][key] = getattr(srcfile, key)
            except AttributeError:
                md_out["metadata"]["global"][key] = ""

# Go through variable attributes. Extract.
    for key, value in md_list["metadata"]["variable"].items():
        if (value == True):
            try:
                md_out["metadata"][var_name][key] = getattr(srcfile.variables[var_name], key)
            except AttributeError:
                md_out["metadata"][var_name][key] = ""

# Close inpout file
    srcfile.close()

# Dump output in json
    with open(out_file, 'w') as fp:
        json.dump(md_out, fp, indent=2)
    fp.close()


