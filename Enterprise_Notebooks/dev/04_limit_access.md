# Security and Access


### Limiting Access

Within a project you can limit access to folders and files to subsets of the project team. Controlling access is done from the Workbench application. In the Workbench application, <right-click> on the file or folder you wish to limit access. A window will be presented. Select "Permissions".

![wakariui](img/permissions_menu.png)

In the window that is displayed, uncheck the permissions you wish to remove. The available permissions are Read, Write, and Execute. If you remove all permissions the individual will not be able to access the file. After making the changes you want click <Submit> to make the changes permanent.

![wakariui](img/permissions_setting.png)


You should receive a window informing you that the change was made.
![wakariui](img/permissions_success.png)

### Give Team Member Access

If a folder or file is protected you can give users on the project access to the file/folder. To give the user permissions to read, write, and/or execute a file you use the same permissions window used to remove access. To give a user access you click the "Add" button first.

![wakariui](img/permissions_add.png)

A new line will be added to the window with a default username of "new".

![wakariui](img/permissions_add_line.png)

Change the username to the username of the team member you want to grant access and select the access you wish them to have and then click the "submit" buton.

![wakariui](img/permissions_add_filled_out.png)

Note: If the user is in the Workbench application they may need to refresh the view to see the newly added access.

### Protected Sharing - Sharing Outside of Team

It is possible to share with individuals who are not part of the team in a controlled manner. To be able to share with an individual they need to have a user id that you can add using the permissions process [above](#limitingaccess). Sharing with individuals outside the team is a four step process performed from the **Workbench** application.

1. Copy or move the file to your home directory.
2. Give user Read & Execute access to your home directory.
3. Add the user to the file's permissions.
4. Have user add directory to their workbench.

#### Copy or move the file to your home directory.

You can find your home directory in the Workbench by looking at the file tree. Your home folder is the one with your username at the bottom. Move or copy the file to this folder. People outside the team will not be able to see the file.

#### Give user Read & Execute access to your home directory

Using the [steps above](#addaccess), give the user Read and Execute access to your home folder. In this case the individual is not on the team but the same steps apply. This will allow the user to see files in your home folder but not access them. You only have to do this the first time you share anything with this specific user. If you want to have files the user cannot see place them inside a folder within your home folder and do not give access to the subfolder.

#### Add the user to the files permissions

You need to add the user to the files permissions using the steps found above in the [Give Team Member Access](#addaccess) section. Once you do this the user will, depending on the access you grant, be able to see, read, change, and execute the file. If it is a folder the user will be able to see and access the folder.

#### Have user add directory to their workbench

The user can now add your home directory to their workbench file browser. To do this have the user click on the show directory button at the top of the file tree in the workbench.

![wakariui](img/workbench_add_shared_folder_1.png)

In the window that pops up the user should add the string **/home/yourusername** in the text box and <click> the **Add** button.

![wakariui](img/workbench_add_shared_folder_2.png)

After clicking add the added folder will appear below the text field. The user can now close the window by clicking on the "x" in the upper right or by clicking outside the window.

![wakariui](img/workbench_add_shared_folder_3.png)

Once the user refreshes the workbench using the refresh button, ![wakariui](img/refresh_button.png)  
they will see the shared file.

![wakariui](img/workbench_add_shared_folder_4.png)
