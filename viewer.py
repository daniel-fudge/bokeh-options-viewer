""" Viewer for options trades.  Please see README.md for detailed instructions."""

import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure

# Set the initial stock price to 100, real data can be scaled to the same
k = 100.0

# Create starting data option trade
a_i = 5
b_i = 5
n_i = 1
p_i = 1
x_i = np.array([0.0, k - a_i - b_i, k - a_i, k + a_i, k + a_i + b_i, 10*k])
y_i = np.array([0.0, 0.0, b_i, b_i, 0.0, 0.0]) - p_i
source = ColumnDataSource(data=dict(x=x_i, y=y_i))

# Set up option plots
plot = figure(plot_height=800, plot_width=800, title="Iron Condor",
              tools=",box_zoom, crosshair, pan, reset, save, wheel_zoom", x_range=[0.0, 2*k], y_range=[-2*b_i, 2*b_i])
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

# Set up widgets
a_slider = Slider(title="1st Strike (a)", value=a_i, start=0, end=a_i*4, step=a_i/20)
b_slider = Slider(title="2nd Strike Delta (b)", value=b_i, start=0, end=b_i*4, step=b_i/20)
n_slider = Slider(title="Number of options (n)", value=n_i, start=-5, end=5, step=0.1)
p_slider = Slider(title="Option Price", value=p_i, start=0.0, end=10, step=0.1)


# Set up callbacks
def update_data(attrname, old, new):

    # Get the current slider values
    a = a_slider.value
    b = b_slider.value
    n = n_slider.value
    p = p_slider.value

    # Generate the new lines
    x = np.array([0.0, k - a - b, k - a, k + a, k + a + b, 10 * k])
    y = n * (np.array([0.0, 0.0, b, b, 0.0, 0.0]) - p)
    source.data = dict(x=x, y=y)


for w in [a_slider, b_slider, n_slider, p_slider]:
    w.on_change('value', update_data)

# Set up layouts and add to document
inputs = column(a_slider, b_slider, n_slider, p_slider)

curdoc().add_root(row(inputs, plot, width=1200))
curdoc().title = "viewer"
