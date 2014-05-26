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
	a = html[html.find("LatLng(")+7:html.find("LatLng(")+7+20]
	b = a.find(",")
	latitud = a[: b]
	a = a[b+1:b+10]
	b = a.find(")")
	longitud = a[: b]
	return [pais,ciudad,latitud,longitud]

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
		self.latitud = ""
		self.longitud = ""

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
		print "Latitud: "+self.latitud
		print "Longitud: "+self.longitud
		print "---------------------"

def esDistintaRuta(ruta1,ruta2):
	for i in range(0,len(ruta1)):
		if ruta1[i].ip != ruta2[i].ip:
			return 1
	return 0

def calczscore(rtt, rttprom, desvio):
	return (rtt-rttprom)/desvio

def calcDesvio(rttprom, rtts):
	suma = sum([(i - rttprom)**2 for i in rtts])
	return math.sqrt(suma/len(rtts))

def analizarRuta (host, count):
	ruta = []
	for i in range(1,65):
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
				h.ttl = i
				ans = []
		if respuestas != 0:
			if len(ruta)!=0:
				if ruta[-1].ip==h.ip:
					break
			location = getlocation(h.ip)
			h.pais = location[0]
			h.ciudad = location[1]
			h.latitud = location[2]
			h.longitud = location[3]					
			h.rttprom = sum(h.rtts)/len(h.rtts)
			h.desvio = calcDesvio(h.rttprom, h.rtts)
			ruta.append(h)
	return ruta

if __name__ == '__main__':

	r = analizarRuta(sys.argv[1], sys.argv[2]) #host, count

########## calculo de zscore ##############################
	rtts = [i.rttprom for i in r]
	rttsuma = sum(rtts)
	rttmedia = rttsuma/len(r)
	desvio = calcDesvio(rttmedia,rtts)
	for i in r:
		i.zscore = calczscore(i.rttprom, rttmedia, desvio)
###########################################################
########## mostrar ruta ###################################
	for i in r:
		i.mostrar()
###########################################################		

	f = open("files/"+sys.argv[1]+".csv","w")
	print >> f, "TTL,IP,RTT(prom),Desviacion Estandar,ZRTT,Location"
	for i in r:
		string = str(i.ttl)+","+str(i.ip)+","+str(i.rttprom)+" ms,"+str(i.desvio)+","+str(i.zscore)+","+str(i.pais)
		if i.ip=="192.168.1.1":
			string = str(i.ttl)+","+str(i.ip)+","+str(i.rttprom)+" ms,"+str(i.desvio)+","+str(i.zscore)+",*"
		if len(i.ciudad)!=0:
			string = string+":"+str(i.ciudad)
		print >>f, string

	f1 = open("files/"+sys.argv[1]+"_coordenadas.csv","w")
	print >>f1, "Mapa,Pais"
	for i in r:
		if i.ip!="192.168.1.1":
			print >>f1, str(i.latitud)+" "+str(i.longitud)+","+str(i.pais)

################verificar ruas alternativas################				

#	routes=[]
#	for i in range(0,3):
#		routes.append(analizarRuta(sys.argv[1], sys.argv[2])) #host, count
#
#	for i in routes:
#		print [x.ip for x in i]
#
#	rutasAlternativas = [x for x in routes if esDistintaRuta(x,r)]
#	for i in rutasAlternativas:
#		print [x.ip for x in i]


