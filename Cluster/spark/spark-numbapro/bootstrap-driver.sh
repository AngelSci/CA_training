sudo apt-get update
sudo apt-get install build-essential -y
sudo wget http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/cuda_7.0.28_linux.run
sudo chmod +x cuda_7.0.28_linux.run
sudo mkdir nvidia_installers
sudo ./cuda_7.0.28_linux.run -extract=`pwd`/nvidia_installers
cd nvidia_installers
sudo ./NVIDIA-Linux-x86_64-346.46.run -a -q -s

sudo bash -c 'cat >/etc/modprobe.d/blacklist-nouveau.conf <<EOL
blacklist nouveau
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off
alias lbm-nouveau off
EOL'

echo options nouveau modeset=0 | sudo tee -a /etc/modprobe.d/nouveau-kms.conf
sudo modprobe nvidia

sudo ./cuda-linux64-rel-7.0.28-19326674.run -noprompt
