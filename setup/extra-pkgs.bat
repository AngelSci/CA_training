rem Install extra packages that live on class-specific AWS repo
call conda install -c sharedpackages accelerate-dldist accelerate-gensim accelerate-skimage -y
call conda install -c bcollins bokeh-geo -y
rem Current version of datashader is available at repo.continuum.io
rem as of 2016-AUG-18, datashader 0.4.0 is in the bokeh channel
call anaconda config --set default_site binstar
call conda install -c bokeh datashader
call anaconda config --set default_site aws

