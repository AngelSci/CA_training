### Streaming data with Bokeh Server + Spark

### What is Spark?

#### Create new conda environment
```bash
source activate acluster
```

#### Log into Anaconda Cloud
```bash
conda install anaconda-client -n root
anaconda login
conda install anaconda-cluster -c anaconda-cluster
```

#### Configure anaconda cluster locally
Edit `~/.acluster/providers.yaml` to include your:
- aws access key
- aws secret key
- private ssh key (e.g. ~/.ssh/mykey.pem)

Clone code from example git repository

```bash
git clone https://github.com/ContinuumIO/iqt-delivery
cd iqt-delivery/bokeh/spark_streaming/
cp taxi_profile.yaml ~/.acluster/profiles.d/
```

#### Create cluster on Amazon Web Services
```bash
acluster create iqt_cluster --profile taxi_profile 
acluster install spark-standalone
acluster conda install numpy, pandas, bokeh==0.11.1, pyproj
```

Verify you can ssh into the master node and take **note of public ip address**
```bash
acluster ssh
exit
```

#### Add example code to copy scripts cluster master node
```bash
ls *.{sh,py} | xargs -I{} acluster put {} /home/ubuntu/{}
```

#### SSH into machine and download source data.  start dashboard, and start mock taxi streaming
```bash
acluster ssh
bash setup_data.sh
```

#### start dashboard on cluster (don't forget --port and --host options)
```bash
bokeh serve dashboard.py --port 8081 --host <your-server-host>:8081
```

open web browser on local machine. To start session, browse to: *http://your-server-host:8081/dashboard

Start streaming
```bash
python taxi_stream.py /taxidata
```
