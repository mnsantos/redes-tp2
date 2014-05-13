#for scapy warnings
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#

from scapy.all import *
import sys

if __name__ == '__main__':
	pkt = IP(dst = sys.argv[1]) / ICMP()
	#print pkt.show2()
	#traceroute(sys.argv[1])
	sr1(pkt)
