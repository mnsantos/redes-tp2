import sys
import numpy as np
import matplotlib.pyplot as plt

def graficador_1(ips,rtts,sds):

	n = len(ips)
	index = np.arange(n)

	bar_width = 0.4
	opacity = 0.4

	rects1 = plt.bar(index, rtts, alpha=opacity, color='blue', yerr= sds)

	plt.xlabel('Direcciones de IP')
	plt.ylabel('RTT promedio')

	plt.ylim([0,700])
	plt.title('RTT x IP')
	plt.xticks(index+bar_width+0.4, ips)
	plt.xticks(rotation = -60)
	plt.legend()
	plt.tight_layout()
	plt.savefig("graficos/rtt")	
	plt.show()

def graficador_2(data):

if __name__ == "__main__":
	ips = []
	rtts = []
	sds = []
	with open(sys.argv[1]) as f:
		for line in f:
			line = line.split()
			ips.append(line[0])
			rtts.append(line[1])
			sds.append(line[3])

	rtts = [float(r) for r in rtts]		
	sds = [float(s) for s in sds]
	graficador_1(ips,rtts,sds)		