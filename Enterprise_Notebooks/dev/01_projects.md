# Projects

### Team Members

Being able to add team members to your projects makes collaboration easy in Anaconda Enterprise Notebooks.  Team members have full access to the project applications, files and services.  When a team member is added, their home directory is mounted to the project. There is no need to download and email data or scripts - your team members can work on the same files in the same environment as you!

### Creating New Projects
1. **Initiate Project Creation** - To create a new project, click on the new project icon on the right hand side of the upper Anaconda Enterprise Notebooks.  
![menu_bar](img/02_a_new_project_button_1.png)
or  
![menu_bar](img/02_b_new_project_button_2.png)

2. **Enter Project Information** - Enter the project name in the create project dialog that appears. The
project defaults to being private. You can change the project to be public at creation or at a later time.
![new_project_create](img/02_c_new_project_create_box.png)

Once you are satisfied with your choices/entries, click the *Next* button at the bottom right hand side of the window.

You will be taken to the home screen for your new project.  
![new_project_create](img/02_d_new_project_home.png)  

At this point, you can add team members to your project or start using applications.  
4.  **Start Project** - Newly created projects are **Stopped** by default. To start a project click on the **Projects Settings**
gear icon.  
![new_project_create](img/02_e_project_settings_icon.png)  

Clicking on this icon will open the project settings page. Click on the **Start** button.
You will need to refresh the page to see the button change from "Starting" to "Pause". When the button has changed to "Pause" and the project status icon has changed to a green circle the project has started.
![new_project_create](img/02_f_project_start.png)
![new_project_create](img/02_g_project_starting_up.png)
![new_project_create](img/02_h_project_started.png)

If the button changes to "Reset" and the project status icon is a "Yellow Triangle" then the project has encountered a problem and did not start.    
![new_project_create](img/02_i_project_start_problem.png)

Try clicking the "Reset" button. This will sometimes allow the project to start. If this does not work contact your administrator.

**Note**: The project status icon also appears next to the project name on the project homepage and the main Projects page.  
**Note**: Launching any of the apps will also start the project.


### Project Drive and Directory

Projects have a project drive attached that all team members can access.  At this time, the size of the project drive is not limited by Anaconda Enterprise Notebooks.  Please contact your system administrator if you find you do not have sufficent space.

Each project has a separate project directory on the project drive.  The project directory is a separate space from the owner's and team members' home directories for project files and data that team members share and have equal access to.

	Note: The path to your project directory is /projects/<project owner>/<project_name>

### Project Environment
The ability to have a custom environment for your project is one of the most powerful features that Anaconda Enterprise Notebooks Projects provide.

A project environment is like any Python environment you would create except it is integrated with the project so all project apps are aware of it and all project members have access to it.

By default a project uses a copy of either the root Anaconda environment or an administrator-defined custom environment.

Follow these steps to create a project environment:

	1> Open a terminal in the project
	2> conda create -n <env name> <list of packages to include in the env...>

**By default all environments created this way will be created under the project directory in the envs sub-directory.**

Use conda to add or changes the packages in your envs at any time.  See [conda docs](http://conda.pydata.org/docs) for more information.

You can create as many project envs as you need but only one env can be actively associated with the project at a time.

Now that the project env is created, use the Compute Config app on the project dashboard to assign it to the project and make it active. Note: you must specify the full path to the environment directory when assigning it to the project.

#### Python 3 Environments
Anaconda Enterprise Notebooks will create python 2.7 environments by default, but it is easy to override the default behavior and create a python 3 environment.

You can specify the python version when using conda to create the environment.

	conda create -n <env name> python=3 <list of packages to include in the env...>

Example:

	conda create -n py3 python=3 numpy scipy

All subsequent packages added to this environment will be the python 3 compatible versions.

### Project Settings

Project settings can be accessed through the icon next to your project's name on the project page.

![wakariui](img/project_settings.png)

#### Project

You'll find the current status of your project at the top. You can start or pause your project.  It is a good practice to pause your project whenever you're not using it, so you are not using resources others might need.

You'll also find the ability to update the project summary and description.  The Summary box accepts plain text. The Description Write tab accepts markdown syntax and you can see a preview of your description under the Preview tab of the Description section.  You'll need to hit the _Submit_ button at the bottom of the screen for your changes to the summary and description to take effect.

![wakariui](img/projects_project.png)

#### Team

Team members may be added or removed easily here.  Simply type in the username of someone you would like to include, then click the 'Add' button to the right of the entry box.

![wakariui](img/manage_team_members.png)

Removing team members is just as simple.  Click the red 'remove' link next to the name of the user you would like to remove.

#### Admin

Projects can be made private or public or deleted permanently from the Admin section of project settings.

![wakariui](img/project_admin.png)

#### Info

Info provides details about your project and the Datacenter it is running in.

![wakariui](img/project_info.png)

