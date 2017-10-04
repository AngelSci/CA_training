# HOWTO Configure and User a Local Conda Channel

## Build Conda package for several platforms:

```bash
cd Desktop
conda build my_recipe 
```

Copy package file to Desktop to do more work on it:

```bash
pkg_path=/Users/jvestuto/anaconda/conda-bld/osx-64/constants-0.0.1-py35_0.tar.bz2
cp $pkg_path ~/Desktop/
```

Convert osx-64 package to a win-64 package

```
cd Desktop
conda convert constants-0.0.1-py35_0.tar.bz2 -p win-64
ls ~/Desktop/win-64/*.bz2
```

## Create a Channel Path, Platform Subdirs

Make new empty dir for custom channel

```bash
mkdir ~/Desktop/my_channel
mkdir ~/Desktop/my_channel/osx-64
mkdir ~/Desktop/my_channel/win-64
```

Copy package files into this new channel:


```bash
cd ~/Desktop
cp constants-0.0.1-py35_0.tar.bz2 my_channel/osx-64
cp win-64/constants-0.0.1-py35_0.tar.bz2 my_channel/win-64
```

## Index your Channel Subdirs

Now index the new channel dirs:

```bash
cd ~/Desktop
conda index my_channel/osx-64 my_channel/win-64
```

## Do not list Channel in condarc!

DO NOT list the `file://` URL for the channel in your `~/.condarc` file.

```
# Contents of .condarc
channels
- defaults
```

## Test Channel by Searching

Now test it by searching for the package name: the `--override-channels` is **required** -- it will skip the `defaults` if specified in `.condarc`

```bash
[jvestuto:~ ] $ conda search -c file://Users/jvestuto/Desktop/my_channel constants --override-channels

Using Anaconda Cloud api site https://api.anaconda.org
Fetching package metadata .....
constants                    0.0.1                    py35_0  file://Users/jvestuto/Desktop/my_channel/osx-64
```

## Install Package from Channel

Now install it! Again, you mist use `--override-channels` flag, and yet, you are using a `-c` channel flag and a `file://` URL in the command line. Not intuitive.

```bash
(test-channel) [jvestuto:~ ] $ conda install -c file://Users/jvestuto/Desktop/my_channel constants --override-channels

Using Anaconda Cloud api site https://api.anaconda.org
Fetching package metadata .....
Solving package specifications: ..........

Package plan for installation in environment /Users/jvestuto/anaconda/envs/test-channel:

The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    constants-0.0.1            |           py35_0           3 KB  file://Users/jvestuto/Desktop/my_channel

The following NEW packages will be INSTALLED:

    constants: 0.0.1-py35_0 file://Users/jvestuto/Desktop/my_channel

Proceed ([y]/n)?
```

# The End