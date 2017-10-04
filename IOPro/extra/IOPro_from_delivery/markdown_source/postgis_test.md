## Prerequisites
1. A PostGIS instance that is available and accessible.
2. Python 2.7 or 3.5 installed on PostGIS system.
3. The following python libraries are installed
	- unittest
	- testing.postgresql
	- pandas
	- numpy
	- sqlalchemy
	- pytest


## Test Steps  
1. SSH to the system with PostGIS installed.
2. Copy the IOPro test folder to the PostGIS system. 
3. **Run tests** using test_postGIS.py file in test data: `python /path/to/iopro/tests/test_postGIS.py`, such as *python /home/ec2-user/iopro/iopro/tests/test_postGIS.py*