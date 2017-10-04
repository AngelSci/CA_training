## Prerequisites
1. An Accumulo docker containiner is available or access to the Internet. See [https://github.com/mraad/accumulo-docker](https://github.com/mraad/accumulo-docker) for an Accumulo docker container.
2. **aws_ubuntu_single.yaml** file has been copied to the `~/.acluster` directory.
3. A cluster has been started - `acluster create test_cluster --profile aws_ubuntu_single`



## Test Steps  
1. SSH to the headnode: `acluster ssh`
2. Install Docker:
	- update apt-get repo: `sudo apt-get update`
	- install docker: `sudo apt-get install docker.io`
3. **Start Accumulo Docker Container**: `sudo docker run --name accumulo -i -t -P mraad/accumulo`  
	- Depending on the environment the machine is you may need to run `sudo docker run --name accumulo -i -t -P mraad/accumulo /bin/bash`
4. **Start services**: `/usr/local/accumulo/bin/accumulo proxy -p /usr/local/accumulo/proxy/proxy.properties`
5. **Run tests** using test_AccumuloAdapter.py file in test data: `python /path/to/iopro/tests/test_AccumuloAdapter.py`, such as *python /home/ec2-user/iopro/iopro/tests/test_AccumuloAdapter.py*