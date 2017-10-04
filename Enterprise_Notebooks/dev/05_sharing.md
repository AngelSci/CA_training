# Sharing in Anaconda Enterprise Notebooks

### Public and Private

Anaconda Enterprise Notebooks supports both public and private sharing.

Any content placed in the "public" folder in a project will be publicly accessible via its URL.

Additionally, a project can be made "public" which means anyone with access to the system will have a
read-only view of all the project assets.

Team members within a project have read-and-write access to all project assets by default.  It is, however,
possible to make use of file system access controls to limit who can access which files.  This can be done
either from the command line or using the Workbench, by right clicking on a file.

### Jupyter Notebooks

In addition to the general project sharing capabilities described above, Jupyter Notebooks can be published
to Anaconda Repository.  This will automatically version the notebook and allow you to set access controls on
who can view the notebook.  The cloud icon with an arrow in it will allow you to do this, provided you have
already logged in to Anaconda Repository.  This can be done from the command line by executing <tt>anaconda login</tt>
or, alternatively, you can use the login UI provided by the nbextension, althought if you are not in a secure connection,
we strongly recommend to use the command line approach.
