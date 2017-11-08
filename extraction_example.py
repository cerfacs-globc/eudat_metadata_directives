# Example of extracting metadata from a list of attributes and dumping results into a JSON file

import metadata_extract

metadata_extract.netcdf_md_extract("/scratch/globc/page/cyclone_tracking/data_era_interim/psl_1d_19790101_20161231_ERAI.nc","psl","metadata_selection.json","metadata_out.json")
