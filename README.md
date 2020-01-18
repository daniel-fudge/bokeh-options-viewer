# bokeh-options-viewer
This is a quick little [Bokeh](https://docs.bokeh.org/en/latest/index.html) tool to visualize options parameterizations 
for Reinforcement Algorithms.  Created to assist in the group project for FINE6800 - Options, Futures & Other Derivative 
Securities as part of my Schulich Concurrent MBA and Financial Engineering degree.
https://schulich.yorku.ca/specializations/financial-engineering/

Much of this code was inspired by the "sliders" web app in the Bokeh [gallery](https://github.com/bokeh/bokeh/tree/master/examples/app).

## How to run on Local PC   
1. Clone repo to PC.
   ```shell script
   git clone https://github.com/daniel-fudge/bokeh-options-viewer.git
   ```
   
1. Install [Anaconda3](https://www.anaconda.com/distribution/).

1. Create and activate a virtual environment.
   ```shell script
   conda update conda
   conda create -n bokeh 
   conda activate bokeh
   conda install bokeh
   ```
   
1. Launch viewer into default browser window.
   ```shell script
   cd bokeh-options-viewer
   bokeh serve --show viewer.py
   ```

1. [OPTIONAL] Launch viewer and then open in a browser window.
   ```shell script
   cd bokeh-options-viewer
   bokeh serve viewer.py
   ```
   Open `http://localhost:5006/viewer` in browser (Chrome Tested)

## License
This code is copyright under the [MIT License](LICENSE).

## Contributions
Please feel free to raise issues against this repo if you have any questions or suggestions for improvement.
