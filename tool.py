#for scapy warnings
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#

from scapy.all import *
import sys


def ping (host, count, ttl):
	rttstotal = []
	rttsprom = []
	for i in range(1,int(ttl)+1):
		sumrtt = 0
		respuestas = 0
		rtts = []
		for j in range(0,int(count)):
			if j==3 and respuestas==0:
				break
			print "count: "+str(j)
			print "ttl: "+str(i)
			pkt = IP(dst = host, ttl=i)  / ICMP()
			ans,unans = sr(pkt, timeout=1)
			if len(ans)!=0:
				respuestas = respuestas + 1
				rtt = (ans[0][1].time-ans[0][0].sent_time)*1000
				rtts.append(rtt)
				sumrtt = sumrtt + rtt				
				hop = ans[0][1].src
				ans = []
			else:
				print "No hubo respuesta"
		if respuestas!=0:		
			rttstotal.append([hop,rtts])
			rttprom = sumrtt/respuestas
			rttsprom.append([hop,rttprom])

	for i in rttstotal:
		print i

	print rttstotal		


if __name__ == '__main__':
	ping (sys.argv[1], sys.argv[2], sys.argv[3]) #host, count and ttl

