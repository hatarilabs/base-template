import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np

x,y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))

def run_plot(i):
	u = np.cos(x)*i
	v = np.sin(x)*i
	return ff.create_quiver(x, y, u, v)

fig = go.Figure()

# Add traces, one for each slider step
for step in np.arange(0, 5, 0.25):
	partial_fig = run_plot(step)
	fig.add_traces(partial_fig.data)

# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.show()