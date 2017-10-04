## Prerequisites
1. A GreenPlum instance that is available and accessible.
2. Python 2.7 or 3.5 installed on PostGIS system.
3. The following python libraries are installed
	- unittest
	- testing.postgresql
	- pandas
	- numpy
	- sqlalchemy
	- pytest


## Test Steps  
1. SSH to the system with GreenPlum installed.
2. Copy the IOPro test folder to the GreenPlum system.
3. Add the user `jayvius` to the Greenplum database with DB CREATE access
	-	`createuser –p jayvius`
	-	Answer ‘y’ to the “allow to create databases? (y/n)” question
*Alternatively can add by connecting the database as gpadmin*
		-	`psql postgres`
		-	at psql prompt: `CREATE USER javius WITH PASSWORD 'pivotal' CREATEDB`
  To verify run the `\du` command at the psql prompt.
	- Enter `\q` to exit.
4. Logged in as gpadmin edit /usr/local/greenplum-db/greenplum_path.sh file and comment out python path being set (PYTHONPATH and PYTHONHOME variables)
5. Run the `setup_postgresql_data_greenplum.py` file
3. **Run tests** using test_PostgresAdaptor.py file in test data: `python /path/to/iopro/tests/test_PostgresAdaptor.py --pg-user jayvius password pivotal`, such as *python /home/ec2-user/iopro/iopro/tests/test_PostgresAdaptor.py*
