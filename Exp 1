import ipywidgets as widgets
from IPython.display import display
slider = widgets.IntSlider(
    value=50,
    min=0,
    max=100,
    step=1,
    description='Value:'
)
output = widgets.Output()
def on_value_change(change):
    output.clear_output()
    with output:
        print(f'Slider value is {change["new"]}')
slider.observe(on_value_change, names='value')
