import pandas as pd
import numpy as np

from bokeh.plotting import Figure
from bokeh.palettes import RdYlGn8
from bokeh.models import ColumnDataSource, HBox, VBoxForm, VBox
from bokeh.sampledata import us_states
from bokeh.models import BoxZoomTool, ResetTool, WheelZoomTool, PanTool, HoverTool
from bokeh.models.widgets import Slider, TextInput
from bokeh.io import curdoc


# data processing functions
def get_data(year=2013, data_dir='../../../data/Bokeh/college-scorecard-raw-data-030216/'):
    file = data_dir+'merged_' + str(year) + '_PP.csv'

    return pd.read_csv(file, encoding='iso-8859-1', na_values=['PrivacySuppressed'], dtype={'NPCURL':str})


def color_by(df, column, colors):
    ncolors = len(colors)

    c,b = pd.qcut(df[column], ncolors, labels=colors, retbins=True)

    return c,b


def size_by(df, column, nsizes=4):
    labels = np.arange(5, 5*nsizes+5, 5)

    s,b = pd.qcut(df[column], nsizes, labels=labels, retbins=True)

    return s,b


def filter_by(df, column=None, value=None):
    idx = df[column] < value

    return idx

def by_state(df, state):
    if state == '':
        return ~(df['STABBR'] == '__')
    else:
        return df['STABBR'] == state.strip()


# columndatasources
schools = ColumnDataSource(data=dict(name=[], lat=[], lng=[], cost=[], adm=[], size=[], color=[]))
states = ColumnDataSource(pd.DataFrame(us_states.data).T)
legend_source = ColumnDataSource(data=dict(bins_left=[], bins_right=[], colors=[]))
sizes_source = ColumnDataSource(data=dict(x=[], sizes=[]))

# Tools
hover = HoverTool(tooltips=[('name','@name'),('cost','@cost'), ('adm rate','@adm')], names=['schools'])
tools = [hover, PanTool(), WheelZoomTool(), ResetTool(), BoxZoomTool()]

# Widgets
admission = Slider(title='Maximum Admission Rate', start=0, end=100, value=100, step=1)
state = TextInput(title='State (abbv)', value='')

# plot
plot = Figure(title = 'College Scorecard', plot_width=850, y_range=(22,52), x_range=(-128,-63), tools=tools)
plot.patches('lons', 'lats', fill_color='white', line_color='blue', source=states)
plot.circle('lng', 'lat', color='color', alpha=0.6, size='size', source=schools, name='schools')

# include a color bar
legend = Figure(plot_height=120, plot_width=850, tools='', x_range=(0, 80000))
legend.title.text = 'Total Annual Cost'
legend.toolbar_location=None
legend.quad(left='bins_left', right='bins_right', top=0.5, bottom=0, fill_color='colors',  source=legend_source)

legend.xgrid.grid_line_color = None
legend.ygrid.grid_line_color = None
legend.yaxis.major_label_text_font_size = '0pt'
legend.yaxis.major_tick_line_color = None
legend.yaxis.minor_tick_line_color = None
legend.xaxis.minor_tick_line_color = None

# include a size legend
legend_s = Figure(plot_height=130, plot_width=850, tools='', x_range=(-0.1,1))
legend_s.title.text = 'Admission Rate'
legend_s.toolbar_location=None
legend_s.circle(x='x', y=0, size='sizes', fill_color='green', alpha=0.6, source=sizes_source)

legend_s.xgrid.grid_line_color = None
legend_s.ygrid.grid_line_color = None
legend_s.yaxis.major_label_text_font_size = '0pt'
legend_s.yaxis.major_tick_line_color = None
legend_s.yaxis.minor_tick_line_color = None
legend_s.xaxis.minor_tick_line_color = None

plots = VBox(plot,legend, legend_s)


df = get_data()
def update(attrname, old, new):

    idx = filter_by(df, 'ADM_RATE', admission.value/100)
    st = by_state(df, state.value)

    _df = df.loc[idx & st, ['INSTNM', 'LATITUDE', 'LONGITUDE', 'COSTT4_A', 'ADM_RATE']].dropna()
    _df['size'], size_bins = size_by(_df, 'ADM_RATE')
    _df['color'], cost_bins = color_by(_df, 'COSTT4_A', RdYlGn8)

    schools.data=dict(
        name = _df['INSTNM'],
        lat  = _df['LATITUDE'],
        lng  = _df['LONGITUDE'],
        cost = _df['COSTT4_A'],
        adm  = _df['ADM_RATE'],
        size = _df['size'].tolist(),
        color = _df['color'].tolist())

    legend_source.data=dict(
            bins_left = cost_bins[:-1],
            bins_right = cost_bins[1:],
            colors = RdYlGn8)

    sizes_source.data=dict(
            x = size_bins[:-1],
            sizes = _df['size'].value_counts().sort_index().index.tolist())


controls = [admission, state]
for control in controls:
        control.on_change('value', update)

inputs = HBox(VBoxForm(*controls), width=300)

update(None, None, None) # initial load of the data

curdoc().add_root(HBox(inputs, plots, width=1100))
