![toolbar](img/anaconda-logo.png)

# Navigator Exercise \#3: Use R computer language in a Jupyter Notebook

It is possible to use R, the popular programing language for statistics,
in a Jupyter Notebook. To do so, we'll follow the exact
navigator-basic-workflow shown above.

## 1\. Create and activate a new environment for the package you want to
use. 

* Go to the Environments tab
* Click the "Create" button at the bottom left
* Give your new environment a descriptive name like "R essentials".
* After it has finished installing, highlight your new environment name to activate it.

## 2\. Search for and install the packages you want. 

* You want both R language and R essentials, which are available in the channel named MRO.
* Show uninstalled packages by selecting "All" from the drop-down menu.
* Then add the MRO channel to your channel list
    * click "Channels",
    * clicking "Add"
    * select the white box that appears and typing "mro" and the enter key
    * click "Update channels".
* Now in the search box when you type "r" or "r-es" the package name "r-essentials" appears in your search results.
* Check the box and from the drop-down menu that appears, select "Mark for installation". 
* Repeat for the "r" package and any other packages you wish to install.
* Click the Apply button that appears at the bottom right. 
* A dialog box appears asking you to confirm, so click the "Ok" button to install R language and R Essentials.

## 3\. Open and use the new R language package. 

Note that Jupyter supports languages other than Python, including R:

* Open Jupyter Notebook...
    * From the Environments tab, 
    * Highlight your new environment name
    * Click the Open icon
    * Select "Open with Jupyter Notebook." 
* Create a new notebook with the R language
    * From the Jupyter Notebook top menu, 
    * choose *New -&gt; R*. 

* To execute R code, paste the following code into the first cell:

```r
library(dplyr) 
iris
```

* Click *Cell -&gt; Run Cells* from the menu bar or press *Ctrl-Enter*.
* This will show the iris data table.
* To plot the data, click *+* to open a second cell, then paste the following code into the cell:

```r
library(ggplot2) 
ggplot(data=iris, aes(x=Sepal.Length, y=Sepal.Width, color=Species)) + geom_point(size=3)
```

* Again, click *Cell -&gt; Run Cells* from the menu bar or press *Ctrl-Enter*

--

