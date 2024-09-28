import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)
    plt.plot(years_extended, intercept + slope * pd.Series(years_extended), 'r', label='Best Fit (All Data)')
    

    # Create second line of best fit
    data_recent = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    plt.plot(years_recent, intercept_recent + slope_recent * pd.Series(years_recent), 'g', label='Best Fit (Since 2000)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()