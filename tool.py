#for scapy warnings
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#

from scapy.all import *
import sys

if __name__ == '__main__':
	ans,unans = sr(IP(dst = sys.argv[1], ttl=4) / ICMP(type=13))
	#ans.make_table(lambda (s,r): (s.dst, s.ttl, r.src ))
	ans.summary()
