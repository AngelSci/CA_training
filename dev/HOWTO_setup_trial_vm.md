## Trial VM info

1. Make sure you don't have any VMs running right now:  
> VBoxManage list runningvms

2. Make sure you don't have an aetrial_v2 VM paused: (none of the output should list aetrial_v2):  
> VBoxManage list vms

3. Go somewhere sensible to start a VM.  Your Downloads folder is not a good place.  Please consider something like:
>  mkdir ~/aetrial_v2  
>  cd ~/aetrial_v2

4. Check that you don't have any VM content in that location already:  
> ls -Flad .vagrant # should return nothing, or not found
> ls -Fla Vagrant* # should not be there

5. That is the "pre-flight check" portion.
Download the VPN-ONLY Vagrantfile (IOW, this is for internal use, not to use with the public or to put in public documentation):  
>  curl -o Vagrantfile http://filer.corp.continuum.io/~ijstokes/Vagrantfile.internal

6. Make sure you don't have any entry in /etc/hosts referring to anaconda-enterprise.trl, and if you do, delete them (use whatever editor you like, but it needs to be run as the root user to edit that file):  
>  sudo vim /etc/hosts

7. Now you need to start your VM, which will trigger the download.  You must be inside the directory you created in step 3 (which is where the curl command needed to be executed to download the Vagrantfile) -- for @StephenK if you download using a browser then either save the file to that step 3 directory or move it there after it has been downloaded (and rename it to Vagrantfile)
> vagrant up --provider virtualbox