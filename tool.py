#for scapy warnings
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#

from scapy.all import *
import sys
import math
import urllib

def getlocation(ip):
	response = urllib.urlopen("http://www.geoiptool.com/es/?IP="+str(ip))
	html = response.read()
	a = html[html.find("Pa&iacute;s")+22:html.find("Pa&iacute;s")+100]
	b = a.find("<")
	pais = a[: b]
	a = html[html.find("Ciudad")+17:html.find("Pa&iacute;s")+100]
	b = a.find("<")
	ciudad = a[: b]
	return [pais,ciudad]	

class Hop:
	def __init__(self):
		self.ip = 0
		self.ttl = 0
		self.rttprom = 0
		self.desvio = 0
		self.rtts = []
		self.zscore = 0
		self.pais = ""
		self.ciudad = ""

	def mostrar(self):
		print "---------Hop---------"
		print "ip: "+str(self.ip)
		print "ttl: "+str(self.ttl)
		print "rttprom: "+str(self.rttprom)
		print "desvio: "+str(self.desvio)
		print "rtts: "+str(self.rtts)
		print "zscore: "+str(self.zscore)
		print "pais: "+self.pais
		print "ciudad: "+self.ciudad
		print "---------------------"

def calczscore(rtt, rttprom, desvio):
	return (rtt-rttprom)/desvio

def calcDesvio(rttprom, rtts):
	suma = sum([(i - rttprom)**2 for i in rtts])
	return math.sqrt(suma/len(rtts))

def analizarRuta (host, count, ttl):
	ruta = []
	for i in range(1,int(ttl)+1):
		respuestas = 0
		for j in range(0,int(count)):
			if j==2 and respuestas==0:
				print "------------------------------------"
				print "Hop con ttl=" + str(i) + " no responde"
				print "------------------------------------"
				break
			pkt = IP(dst = host, ttl=i)  / ICMP()
			ans,unans = sr(pkt, timeout=2)
			if len(ans)!=0:
				respuestas = respuestas + 1
				if respuestas == 1:
					h = Hop()
				rtt = (ans[0][1].time-ans[0][0].sent_time)*1000
				h.rtts.append(rtt)
				h.ip = ans[0][1].src
				location = getlocation(h.ip)
				h.pais = location[0]
				h.ciudad = location[1]
				h.ttl = i
				ans = []
		if respuestas != 0:		
			h.rttprom = sum(h.rtts)/len(h.rtts)
			h.desvio = calcDesvio(h.rttprom, h.rtts)
			ruta.append(h)
	
	for i in ruta:
		i.mostrar()

if __name__ == '__main__':
	analizarRuta(sys.argv[1], sys.argv[2], sys.argv[3]) #host, count and ttl
