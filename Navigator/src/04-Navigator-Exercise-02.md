![toolbar](img/anaconda-logo.png)

# Navigator Exercise \#2: Use QGrid with Yahoo S&P 500 data

QGrid is a dataframe viewer for Jupyter notebook. To test your
installation, use QGrid to display S&P 500 stock market data.

To install QGrid follow the instructions on how to install a package above, but install "qgrid" instead of "biopython".

Open a Jupyter Notebook and paste the following Python code into the first code cell:

```python
# Import needed modules
import qgrid
import pandas as pd
from pandas.io.data import get_data_yahoo

# Prevents the grid from being too large
pd.set_option('display.max_rows', 8)

# Retrieve data from Yahoo
spy = get_data_yahoo(symbols='SPY', start=pd.Timestamp('2011-01-01'), 
                     end=pd.Timestamp('2014-01-01'), adjust_price=True) 
# Display data
spy
```

To run the code click *Cell -&gt; Run Cells* from the menu bar or use
the keyboard shortcut *Ctrl + Enter*.

This returns a Pandas `DataFrame` containing the daily prices for the S&P 500 for the dates `1/1/2011 - 1/1/2014` and displays the first and last four rows of
the DataFrame.

![image](img/navigator-tutorial06.png)

Thanks to <https://github.com/quantopian/qgrid> and
<http://nbviewer.jupyter.org/gist/TimShawver/b4bc80d1128407c56c9aifor>
example code.

--