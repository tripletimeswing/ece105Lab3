# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

import numpy as np
import matplotlib.pyplot as plt

def generate_data(seed):
    """
    Generate synthetic temperature sensor data and timestamps.

    Parameters
    ----------
    seed : int
        Random seed for the NumPy random number generator to ensure
        reproducible results.

    Returns
    -------
    sensor_a : ndarray of shape (200,)
        Temperature readings from Sensor A, normally distributed with
        mean 25°C and standard deviation 3°C.
    sensor_b : ndarray of shape (200,)
        Temperature readings from Sensor B, normally distributed with
        mean 27°C and standard deviation 4.5°C.
    timestamps : ndarray of shape (200,)
        Timestamps uniformly distributed between 0 and 10 seconds.
    """
    rng = np.random.default_rng(seed=seed)
    n = 200
    timestamps = rng.uniform(0, 10, n)
    sensor_a = rng.normal(25, 3, n)
    sensor_b = rng.normal(27, 4.5, n)
    return sensor_a, sensor_b, timestamps


# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """
    Plot scatter plot of sensor readings vs timestamps on the given Axes.

    Parameters
    ----------
    sensor_a : array-like
        Temperature readings from Sensor A.
    sensor_b : array-like
        Temperature readings from Sensor B.
    timestamps : array-like
        Time values for the readings.
    ax : matplotlib.axes.Axes
        The Axes object to draw the plot on.

    Returns
    -------
    None
        Modifies the Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, label='Sensor A', alpha=0.7)
    ax.scatter(timestamps, sensor_b, label='Sensor B', alpha=0.7)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Temperature Readings Over Time')
    ax.legend()
    ax.grid(True)


def plot_histogram(sensor_a, sensor_b, ax):
    """
    Plot overlaid histogram of sensor temperature distributions on the given Axes.

    Parameters
    ----------
    sensor_a : array-like
        Temperature readings from Sensor A.
    sensor_b : array-like
        Temperature readings from Sensor B.
    ax : matplotlib.axes.Axes
        The Axes object to draw the plot on.

    Returns
    -------
    None
        Modifies the Axes object in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='blue')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='orange')
    ax.axvline(np.mean(sensor_a), color='blue', linestyle='--', linewidth=2, label='Sensor A Mean')
    ax.axvline(np.mean(sensor_b), color='orange', linestyle='--', linewidth=2, label='Sensor B Mean')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Overlaid Histograms of Sensor Temperature Distributions')
    ax.legend()

def plot_boxplot(sensor_a, sensor_b, ax):
    """
    Plot side-by-side box plot of sensor distributions on the given Axes.

    Parameters
    ----------
    sensor_a : array-like
        Temperature readings from Sensor A.
    sensor_b : array-like
        Temperature readings from Sensor B.
    ax : matplotlib.axes.Axes
        The Axes object to draw the plot on.

    Returns
    -------
    None
        Modifies the Axes object in place.
    """
    ax.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'])
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, color='red', linestyle='--', linewidth=2, label=f'Overall Mean: {overall_mean:.2f}°C')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Side-by-Side Box Plot of Sensor Distributions')
    ax.legend()

def main():
    """
    Generate sensor data and create a figure with a 2x2 grid of subplots: scatter, histogram, box plot, and summary statistics.

    Generates synthetic sensor data using a fixed seed, creates a 2x2 subplot figure,
    calls the plotting functions for three subplots, adds summary statistics to the fourth,
    adjusts the layout, and saves the figure as 'sensor_analysis.png' at 150 DPI with tight bounding box.

    Returns
    -------
    None
    """
    sensor_a, sensor_b, timestamps = generate_data(seed=2022)
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0, 0])
    plot_histogram(sensor_a, sensor_b, axes[0, 1])
    plot_boxplot(sensor_a, sensor_b, axes[1, 0])
    
    # Summary statistics in the fourth subplot
    axes[1, 1].axis('off')
    axes[1, 1].text(0.05, 0.95, 'Summary Statistics:', transform=axes[1, 1].transAxes, fontsize=12, verticalalignment='top')
    axes[1, 1].text(0.05, 0.85, f'Sensor A: Mean = {np.mean(sensor_a):.2f}°C, Std = {np.std(sensor_a):.2f}°C', transform=axes[1, 1].transAxes, fontsize=10)
    axes[1, 1].text(0.05, 0.75, f'Sensor B: Mean = {np.mean(sensor_b):.2f}°C, Std = {np.std(sensor_b):.2f}°C', transform=axes[1, 1].transAxes, fontsize=10)
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    axes[1, 1].text(0.05, 0.65, f'Overall Mean = {overall_mean:.2f}°C', transform=axes[1, 1].transAxes, fontsize=10)
    
    plt.tight_layout()
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')

if __name__ == '__main__':
    main()