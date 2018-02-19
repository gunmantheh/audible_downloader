import urllib2
import sys
import re

#try:
#    if sys.argv[1]:
#        Name = str(sys.argv[1])
#
#except:
#    print "no argument given - using DERP"
#    Name = "http://cds.audible.com/download/admhelper?user_id=3we-an0509EY7MSBSMXVjdJH_G9zs6QriycbY2Nisbe0d7yRBwiuHwp6xcZi2w&product_id=BK_RECO_008291&domain=www.audible.com&order_number=D01-6901805-5485006&cust_id=3we-an0509EY7MSBSMXVjdJH_G9zs6QriycbY2Nisbe0d7yRBwiuHwp6xcZi2w&DownloadType=Now&transfer_player=1&title=Golden%20Son%3A%20Book%20II%20of%20the%20Red%20Rising%20Trilogy&codec=LC_64_22050_stereo&awtype=AAX"

def getFile(url):
	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	#meta = u.info()
	#print meta
	#file_size = int(meta.getheaders("Content-Length")[0])
	#print "Downloading: %s Bytes: %s" % (file_name, file_size)
	f = ""
	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f = f + buffer
	    #status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    #status = status + chr(8)*(len(status)+1)
	    #print status,

	return f

def downloadFile(downloadURL):
	file = getFile(downloadURL)
	print "\n"
	resultURL = "http://cds.audible.com/download?" + file
	u = urllib2.urlopen(resultURL)
	meta = u.info()
	tmp = meta.getheaders("Content-Disposition")[0]
	match = re.search("(?<=filename=)([^_]+)", tmp)

	if (match and match.group(1)):
		filename = match.group(1) + ".txt"
		print ("Filename: " + filename)
		f = open(filename, "wt")
		f.write(resultURL)
		f.close()

	file_size = int(meta.getheaders("Content-Length")[0])
	print ("Filesize: {0} MB".format(file_size / 1024**2))

	#file_name = url.split('/')[-1]
	#u = urllib2.urlopen(url)
	#f = open(file_name, 'wb')
	#meta = u.info()
	#file_size = int(meta.getheaders("Content-Length")[0])
	#print "Downloading: %s Bytes: %s" % (file_name, file_size)

	#file_size_dl = 0
	#block_sz = 8192
	#while True:
	    #buffer = u.read(block_sz)
	    #if not buffer:
	        #break

	    #file_size_dl += len(buffer)
	    #f.write(buffer)
	    #status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    #status = status + chr(8)*(len(status)+1)
	    #print status,

	#f.close()

def main():
	url = ""
	try:
		if (sys.argv[1]):
			url = sys.argv[1]
	except:
		print ("no url given")
		return 1

	downloadFile(url)

	return 0

if __name__ == "__main__":
    main()