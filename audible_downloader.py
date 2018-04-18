from urllib.request import urlopen
import sys
import re

def getFile(url):
	file_name = url.split('/')[-1]
	u = urlopen(url)
	f = ""
	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f = f + buffer.decode('utf-8')
	return f

def downloadFile(downloadURL):
	file = getFile(downloadURL)
	print("\n")
	resultURL = "http://cds.audible.com/download?" + file
	u = urlopen(resultURL)
	meta = u.info()
	tmp = meta["Content-Disposition"]
	match = re.search("(?<=filename=)([^_]+)", tmp)

	if (match and match.group(1)):
		filename = match.group(1) + ".txt"
		print ("Filename: " + filename)
		f = open(filename, "wt")
		f.write(resultURL)
		f.close()

	file_size = int(meta["Content-Length"])
	print("Filesize: {0} MB".format(file_size / 1024**2))

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