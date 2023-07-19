import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_gc(x_lists, y_lists, labels, y_err_lists=None, save_as=None):
    plt.clf()
    font = {"fontname":"Monospace", "size":12}

    plt.figure(figsize=(10,10))    

    # Adding a grid
    plt.grid(True, which='both', color='0.75', linestyle='-.')

    for i in range(len(x_lists)):
        # Plot with error bars if error data is provided
        if y_err_lists is not None:
            plt.errorbar(x_lists[i], y_lists[i], yerr=y_err_lists[i], label=labels[i])
        else:
            plt.plot(x_lists[i], y_lists[i], label=labels[i])

    plt.title("Analysis of Flux Variation:\nGrowth Curves for Potential Variable Stars", **font)
    plt.xlabel("Radius [px]", **font)
    plt.ylabel("Flux [ADU]", **font)
    
    plt.xticks(**font)
    plt.yticks(**font)

    # Using scientific notation for large numbers
    plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
    
    # Add a legend
    plt.legend(loc="best")

    # Show the plot
    plt.show()

    # Save the plot as an image file if filename is provided
    if save_as is not None:
        plt.savefig(save_as, dpi=300, format='png')

    return 


if __name__ == "__main__":

    filenames = ["gc.txt"]
    labels = ["Data 1", "Data 2", "Data 3", "Data 4", "Data 5"]

    radius_lists = []
    flux_lists = []

    for filename in filenames:

        radius_list = []
        flux_list = []

        with open(filename, "r") as file:
            for line in file:

                line = line.split()

                radius = line[0]
                radius = float(radius)
                radius_list.append(radius)

                flux = line[1]
                flux = float(flux)
                flux_list.append(flux)

        radius_lists.append(radius_list)
        flux_lists.append(flux_list)

    plot_gc(radius_lists, flux_lists, labels)
