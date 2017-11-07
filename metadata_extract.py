# -*- coding: latin-1 -*-

#  Copyright CERFACS (http://cerfacs.fr/)
#  Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
#
#  Author: Christian Page (2017)

import sys
import os

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


