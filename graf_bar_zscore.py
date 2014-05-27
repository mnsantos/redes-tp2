import sys
import os
import Gnuplot.gp

	set terminal pdf enhanced
	set output 'bar.pdf'

	set style data histogram
	set style histogram cluster gap 1

	set style fill solid border rgb "black"
	set auto x
	set yrange [0:*]
	plot 'info.dat' using 2:xtic(1) title col, \
	        '' using 3:xtic(1) title col