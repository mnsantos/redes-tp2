import sys
import numpy as np
import matplotlib.pyplot as plt

def graficador(ips,zscores):
	print len(ips)
	print len(zscores)

	n = len(ips)
	index = np.arange(n)

	bar_width = 0.8
	opacity = 0.4

	rects1 = plt.bar(index, zscores, alpha=opacity, color='red')

	plt.xlabel('Direcciones de IP')
	plt.ylabel('zrtt')

	plt.ylim([-1.8,2])
	plt.title('zscore x IP')
	plt.xticks(index+bar_width+0.4, ips)
	plt.xticks(rotation = -75)
	plt.legend()
	plt.tight_layout()
	plt.savefig("graficos/zscore")	
	plt.show()

if __name__ == "__main__":
	ips = []
	zscores = []
	with open(sys.argv[1]) as f:
		i = 0
		for line in f:
			if i!=0:	
				line = line.split()
				ips.append(line[0])
				zscores.append(line[1])
			i = i+1

		zscores = [float(z) for z in zscores]
		graficador(ips,zscores)


