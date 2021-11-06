import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    current_year = df['Year']
    current_sea_level = df['CSIRO Adjusted Sea Level']

    recent_year = df.loc[df['Year'] >= 2000, 'Year']
    recent_sea_level = df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level']

    res = linregress(current_year, current_sea_level)
    recent_res = linregress(recent_year, recent_sea_level)

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.scatter(current_year, current_sea_level, label='Current data')

    # Create first line of best fit
    new_year = [i for i in range(1880, 2051)]
    new_res = [res.intercept + res.slope * i for i in new_year]

    ax.plot(new_year, new_res, color='red', label='Line from 1800s')

    # Create second line of best fit
    new_recent_year = [i for i in range(2000, 2051)]
    new_recent_res = [recent_res.intercept + recent_res.slope * i for i in new_recent_year]

    ax.plot(new_recent_year, new_recent_res, color='yellow', label='Line from 2000s')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return fig.gca()
