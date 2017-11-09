#!/usr/bin/env python3
#
# Example of extracting metadata from a list of attributes and dumping results into a JSON file

import os
import requests
import tempfile
import metadata_extract

object_url = 'http://www.cerfacs.fr/~page/psl_Amon_CNRM-CM5_rcp45_r1i1p2_200601-203512.nc'

response = requests.get(object_url, stream=True)

# Throw an error for bad status codes
response.raise_for_status()

with tempfile.NamedTemporaryFile(delete=False) as handle:
    for block in response.iter_content(1024):
        handle.write(block)

metadata_extract.netcdf_md_extract(handle.name, "psl", "metadata_selection.json", "metadata_out.json")

os.unlink(handle.name)
