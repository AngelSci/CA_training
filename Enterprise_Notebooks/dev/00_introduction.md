# Anaconda Enterprise Notebooks Overview


### We Believe

* We believe data should be shareable, and analysis should be repeatable.
* We believe reproducibility should extend beyond just code to include the runtime environment, the configuration, and the input data.
* We believe programmers, scientists, and analysts should spend their time analyzing data, and working together, not working to set up a system.

### Anaconda Enterprise Notebooks

Accessed through any modern web browser, AEN provides quick access to tools and working environments needed to get started developing and collaborating with you team on analysis projects.


### Team Focus

Anaconda Enterprise Notebooks is team focused.

* You can create team projects and use them to share analysis code and results with your team
* You can add any Anaconda Enterprise Notebooks user to your project as a team member.
* There is no limit on the number of team members you can have on a project.
* Team members have full access to the project applications, files and services.
* All projects have a project drive that team members share.
* Team members also have full access to their Anaconda Enterprise Notebooks home directory.

### Projects

Anaconda Enterprise Notebooks projects are a powerful way to collaborate.

Anaconda Enterprise Notebooks projects support teams working on a shared node with a shared drive and a common python environment.

![wakariui](img/index_project_overview.png)

After you create a Anaconda Enterprise Notebooks account, you can create as many projects as you'd like.

* Each project has a unique team member list that you manage.
* There is no limit on the number of team members you can add to a project.
* Each new project comes with a shared project drive that team members can easily and securely access.
* Your Anaconda Enterprise Notebooks home directory is mounted to all your projects.

### Example User Profile with Projects

![wakariui](img/index_profilescreen.png)

### Features

* Each project includes access to the available applications that are visible on the project home screen.
* Projects can be public or private, for access control.
* On the *Dashboard* main page you can see all your projects and the projects for which you are a contributor.

![dashboard](img/dashboard_main.png)

It addition to listing projects, there are lists of popular tags, those you collaborate the most with, top rated projects, and your list of saved searches.

More information about these sections can be found in the documentation on Projects.

### Applications

There are many applications available for Anaconda Enterprise Notebooks that come standard with all projects.  Currently, these applications include the following:

*  a workbench (which includes a file manager, terminal, and editor in one window).
*  A notebook viewer application
*  a terminal
*  Jupyter Notebook

![wakariui](img/index_app_icons.png)

Each application opens on a new window or tab of your browser.  All applications within a project have simultaneous access to your home directory and project drive. This gives you much more flexibility to set up your workspace the way you want.

### Python Environments

Python Environments are at the heart of each Anaconda Enterprise Notebooks project.  When Anaconda Enterprise Notebooks is installed a default root environment is created and used as the default enviroment for all projects.  The root environment is created and owned by an administrator so it cannot be changed by individual users.  When a user needs a custom environment that is different than the root env they must create a new env and set their project to use it.

##### Environment Locations

Environments may exist in various locations:

  * root (/opt/wakari/anaconda)
  * root envs (/opt/wakari/anaconda/envs)
  * home directory
  * project envs directory
  * any arbitrary path

##### Default Project Environments

A new environment named `default` is created within each new project. The default environment is a clone of the root environment that is writable by members of the project team.

If needed, your administrator can create a customized default project environment. If the directory `/opt/wakari/anaconda/envs/default` exists, it will be cloned instead of the root environment. For example, the administrator can use the command

```
conda create -p /opt/wakari/anaconda/envs/default python=3.4 numpy scipy pandas
```

to create a new default environment with those packages. Subsequently created projects would use a copy of that environment instead of a copy of the root environment.