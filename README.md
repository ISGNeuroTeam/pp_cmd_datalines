# pp_cmd_datalines
Postprocessing command "datalines"
## Description
Command accepts csv as first argument and create dataframe from it.

### Arguments
- data - positional argument, string, required, csv as string.
- sep - keyword argument, string, not required, default is `,`. Separator in csv

### Usage example
```
query: datalines "a,b,c\n1.2,2,3\n2.3,4,5", sep=","

     a  b  c
0  1.2  2  3
1  2.3  4  5

```

## Getting started
### Installing
1. Create virtual environment with post-processing sdk 
```bash
    make dev
```
That command  
- downloads [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates link to current command in postprocessing `pp_cmd` directory 

2. Configure `otl_v1` command. Example:  
```bash
    vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/otl_v1/config.ini
```
Config example:  
```ini
[spark]
base_address = http://localhost
username = admin
password = 12345678

[caching]
# 24 hours in seconds
login_cache_ttl = 86400
# Command syntax defaults
default_request_cache_ttl = 100
default_job_timeout = 100
```

3. Configure storages for `readFile` and `writeFile` commands:  
```bash
   vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/readFile/config.ini
   
```
Config example:  
```ini
[storages]
lookups = /opt/otp/lookups
pp_shared = /opt/otp/shared_storage/persistent
```

### Run datalines
Use `pp` to run datalines command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  datalines "a,b,c\n1.2,2,3\n2.3,4,5"
```
## Deploy
Unpack archive `pp_cmd_datalines` to postprocessing commands directory