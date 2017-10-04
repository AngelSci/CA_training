# Search and Recommendations

### Search
You can search for projects and files using the Search box at the top of the screen. When you are viewing a project home page, the Search box will search for files within the current project. Otherwise, it will search for projects containing files that match your search criteria. Note that your search results will only include files and projects which you have permissions to view. To search just enter a string to use and press enter.
<center>
![search_box](img/search_box.png)
</center>

After pressing enter you will see the results. Clicking on the plus ("+") icon will show the files that the search returned for the given project.
The results are limited to public projects and those private projects to which you have at least view access. If you click on a file the file will open for you to view.

<center>
![search_results_expansion](img/search_results_expansion_icon.png)

![search_results_detail](img/search_results_details.png)
</center>

Clicking on the project name instead of the plus ("+") sign will take you to the project.

#### Saving Search
You can save a search for future use. At the top of the search results clicking on the "save this search" text will save the search.
The "save this search" text will change to read "stored".

<center>
![save_search](img/save_search.png)
</center>

<center>
![save_search_saved](img/save_search_saved.png)
</center>

The saved search can then be found in the "Saved Searches" box on your home page that lists all the projects for which you are a contributor.
To remove the saved search click the "x" next to the name of the search.

<center>
![saved_searches](img/saved_searches.png)
</center>

#### Additional Search Information
Currently these types of files are included in search results:

* .py: Python source files
* .ipynb: IPython/Jupyter notebooks
* .txt: plain text files
* .md: Markdown files

You can use any of the following search constructs:

* Ordinary words will match the full-text contents of any file
* Wildcards are permitted (`John*` will match `John` and `Johnny`)
* Combine queries using `AND` or `OR`, and group them using parentheses.

You can also search in specific metadata fields:

* `imports:name` will match files that import the module 'name'
* `uses:name` will match files that reference the identifier 'name'. Referenced names include functions and globals imported from other modules, as well as the names of methods invoked on any object.
* `defines:name` will match files that define the identifier 'name'. Defined names include functions defined at global scope, class names, and method names within classes.
* `acl:user` will match files that the user named 'user' has read access to.


Files that are modified while a project is running will automatically be re-indexed. Normally, this will occur shortly after the files are modified. If you create or update a large number of files (for example, cloning a git repository or copying a directory), the search results may take several minutes to update.

If files are modified while the project is not running, they will be re-indexed once the project is started.

### Tagging

#### Adding and Removing Tags
**Tags** can used as a way to group like projects, as a way to identify a project so that it is easier to find at a later date, and as a
way to let others know about a project. On any project you have access to you can create, and remove, *tags* to that are associated with that project.
To add a *tag* go to the projects main page. In the "Tags" box on the right of page enter the name of *tag* you wish at add and click the "Add" button.
The new *tag* will be added and show up in the "Tags" list. To remove a *tag* from a project click on the "x" next to the *tag's* name.
<center>
![tag_add](img/tag_add.png)

![tag_added](img/tag_added.png)
</center>

If the *tag* was not already visible from your main home page in the "Tag" list it will be added. If the *tag* already was showing because another
project had the *tag*, then the number next to the *tag* name will be incremented.

<center>
![tag_on_dashboard](img/tag_on_dashboard.png)
</center>

#### List Projects with Tag
Just click on a *tag* name and a list of projects with that *tag* will be shown. The results list will show those public projects and private projects
that you have access to which also have that *tag*. Clicking on a project will take you to that project's home page.

<center>
![tag_click](img/tag_click.png)

![tag_results](img/tag_results.png)
</center>

### Starring and Most Popular Projects
If you see a project you can **star** the project. To star a project just click the *star* icon at the upper right on the project page.
To unstar a project just click the *star* again. Adding and removing stars on a project does not affect anyone else's stars that they may have added.

![star](img/star.png)

When you star a project it makes it more likely that the project will appear in the **Top Rated** project list on the Dashboard home page.
The number next to the project in the Top Rated list is the number of stars that have been given to that project. Clicking on a project
in the list will take you to a view of that project's home page.

![star_list](img/star_list.png)

### Recommendations and Related Projects
On a project's home page there is a "Related Projects" list on the right side of the page below the Team list. The projects listed
in this section are automatically based on how similar their fiels are to the project being viewed.

<center>
![recommended_projects](img/recommended_projects.png)
</center>

The recommendation engine leverages the search functionality to locate similar files and projects. In determining what should be listed in the
*Related Projects* lists the recommendation engine gets the existing files in the project. The terms found in those documents are weighted
to determine which ones are to be used for the "likeness" search. A search is then performed, with extra weighting given to the *uses* and *imports* keywords,
find the files, and the related projects, that are most similar to the current project's files. The results are scored and the top scoring matches are displayed
for public projects and those private projects to which you have access. The recommendation is driven by the how similar the files are between the projects.

### Collaborators
The home page has a section that lists your top collaborators. This list is composed of those collaborators that share the most projects
in common with you. If you click on one of the collaborators you will be taken to a view of their home page where you can see those projects
that they are contributors on that you also have access to view, including all public projects they are contributors on.

<center>
![top_collaborators](img/top_collaborators.png)
</center>
