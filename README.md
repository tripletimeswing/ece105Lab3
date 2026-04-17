<!-- Create a README.md with these sections:
     1. Project title and one-sentence description
     2. Installation (activate ece105 conda env, pip install numpy matplotlib)
     3. Usage (python generate_plots.py)
     4. Example output (describe the three plots briefly)
     5. AI tools used and disclosure -->

# Sensor Data Analysis Script

A Python script that generates synthetic temperature sensor data from two sensors and creates a comprehensive visualization figure with scatter plots, histograms, and box plots for analysis.

## Installation

1. Activate the `ece105` conda environment:
   ```
   conda activate ece105
   ```

2. Install the required dependencies using conda or mamba:
   ```
   conda install numpy matplotlib
   # or
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the command line:
```
python generate_plots.py
```

The script will generate synthetic sensor data and automatically create and save the analysis plots.

## Example Output

The script produces a file named `sensor_analysis.png` containing a 1x3 subplot figure:

- **Left subplot (Scatter Plot)**: Shows temperature readings from Sensor A (blue) and Sensor B (orange) plotted against time (0-10 seconds), illustrating the temporal distribution of readings.
- **Middle subplot (Histogram)**: Displays overlaid histograms of the temperature distributions for both sensors, with vertical dashed lines indicating each sensor's mean temperature.
- **Right subplot (Box Plot)**: Presents side-by-side box plots comparing the statistical distributions of the two sensors, including a horizontal dashed line showing the overall mean temperature across both sensors.

The figure is saved at 150 DPI with tight bounding box for high-quality output.

## AI Tools Used and Disclosure

[Placeholder: Describe any AI tools or assistance used in developing this script, including how they were utilized and any relevant disclosures.]