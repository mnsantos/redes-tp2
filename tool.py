#for scapy warnings
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#

from scapy.all import *
import sys

if __name__ == '__main__':

	for i in range(0,20):
		pkt = IP(dst = sys.argv[1], ttl=1)  / ICMP()
		ans,unans = sr(pkt, timeout=1)

		if len(ans)!=0:
			print "src: " + ans[0][0].src + " respuesta: " + ans[0][1].src
			print str((ans[0][1].time-ans[0][0].sent_time)*1000) +" ms" #RTT
			print ans[0][0].id
			ans = []
		else:
			print "No hubo respuesta"
		
		#ans.summary()
		#unans.summary()
