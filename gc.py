import matplotlib.pyplot as plt

def plot_gc(x_list, y_list):

	plt.clf()
	font = {"fontname":"Monospace", "size":12}

	plt.figure(figsize=(10,10))	
	plt.plot(x_list, y_list, color="black")

	plt.title("Growth Curve", **font)
	plt.xlabel("Radius [px]", **font)
	plt.ylabel("Flux [ADU]", **font)
	plt.xticks(**font)
	plt.yticks(**font)

	plt.show()

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

# stack-20230615-10x60s.fit
#
# gc example
# 	a = 14:03:49.8256 --> 210.95761
# 	d = 54:09:06.344  --> 54.15176
#
# galaxy center
#	a = 14:03:12.5495 --> 210.80229
#	d = 54:20:57.273  --> 54.34924
#
# supernova
#	a = 14:03:38.5393 --> 210.91058
#	d = 54:18:42.210  --> 54.31172
#
# d = sqrt((x2 - x1)^2 + (y2 - y1)^2)