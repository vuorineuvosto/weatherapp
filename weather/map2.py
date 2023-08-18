#####################################################################################################
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


# Your weather_data list
def plot_points(weather_data, city, second_axis):
    
    #get different measurepoint data from parsed weather_data
    symbols, temperatures, windspeed, time = zip(*weather_data)
    #get number of measurepoints 
    x_indices = np.arange(len(symbols))
    bar_width = 0.4

    #create figure and axis for it
    fig, ax1 = plt.subplots()

    #path for every single weather symbol / already in correct order so no matching name to code neccessary
    image_paths = ["symbols/" + symbol + ".png" for symbol in symbols]

    #display measurepoint weather symbols for x-axis
    for i, image_path in enumerate(image_paths):
        image = plt.imread(image_path)
        imagebox = OffsetImage(image, zoom=0.15)
        ab = AnnotationBbox(imagebox, (i, 0.4), frameon=False)
        ax1.add_artist(ab)

    #first bar
    ax1.bar(x_indices, temperatures, width=bar_width, align="center", label="Temperature", color="orange")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Temperature (°C)")
    
    #second bar
    ax2 = ax1.twinx()
    ax2.bar(x_indices + bar_width, windspeed, width=bar_width, align="center", label=second_axis, color="blue")
    ax2.set_ylabel(second_axis)

    #set bars in the "middle" & x-axis labels
    ax1.set_xticks(x_indices + bar_width / 2)
    ax1.set_xticklabels(time, rotation=50)

    #combine legends (temp && windspeed or mintemp)
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc="upper left")

    plt.title(f"Current Weather in {city}")
    #plt.tight_layout()
    plt.show()
#####################################################################################################