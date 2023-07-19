import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_gc(x_list, y_list, y_err_list=None, save_as=None):
    plt.clf()
    font = {"fontname":"Monospace", "size":12}

    plt.figure(figsize=(10,10))    

    # Adding a grid
    plt.grid(True, which='both', color='0.75', linestyle='-.')

    # Plot with error bars if error data is provided
    if y_err_list is not None:
        plt.errorbar(x_list, y_list, yerr=y_err_list, color="black", label="Data")
    else:
        plt.plot(x_list, y_list, color="black", label="Data")
    
    plt.title("Analysis of Flux Variation: \nGrowth Curves for Potential Variable Stars", **font)
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

	filename = "gc.txt"

	radius_list = []
	flux_list = []

	file = open(filename, "r")

	for line in file:

		line = line.split()

		radius = line[0]
		radius = float(radius)
		radius_list.append(radius)

		flux = line[1]
		flux = float(flux)
		flux_list.append(flux)

	plot_gc(radius_list, flux_list)

# Any fits file 

