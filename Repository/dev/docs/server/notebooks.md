IPython notebook support in Anaconda repository
===============================================

As of Anaconda repository version 2.3.0, you can upload notebooks to
your Anaconda repository instance.

Uploading notebooks
-------------------

You can upload notebooks to your user account using the following
command:

    anaconda upload -p my-notebook my-notebook.ipynb

You can then view your notebook by browsing to the associated user
account on your Anaconda repository installation.

You can also upload a new version of your notebook by uploading it with
the version switch included:

    anaconda upload -p my-notebook -v 1.1 my-notebook.ipynb

Notebook-related functionality inside Anaconda repository is still in
early development; the ability to view and run notebooks inside Anaconda
repository will become available as the project progresses.

At present you can share, download and then run the notebooks as you
would other packages or files.
