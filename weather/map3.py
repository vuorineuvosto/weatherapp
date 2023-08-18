import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def plot_curret(weather_data, city):

    #get different measurepoint data from parsed weather_data
    symbol, temperature, windspeed, time = zip(*weather_data)

    #create figure and axis for it
    fig, ax = plt.subplots()
    ax.axis("off")

    #add a single image for correspoding weather
    image_path = "symbols/" + symbol[0] + ".png"
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=0.5)
    ab = AnnotationBbox(imagebox, xy=(0.5, 0.75), frameon=False)
    ax.add_artist(ab)

    annotations = [
        f"Temperature: {temperature[0]}°C",
        f"Windspeed: {windspeed[0]}m/s",
        f"Time: {time[0]}"
    ]

    for i, text in enumerate(annotations):
        ax.annotate(text, xy=(0.5, 0.5 - i * 0.15), ha="center", fontsize=12)


    plt.title(f"Current Weather in {city}")
    plt.show()
#####################################################################################################