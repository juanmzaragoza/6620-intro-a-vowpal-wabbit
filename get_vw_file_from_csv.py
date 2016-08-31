import getopt,sys, re, csv

# recibe un texto en formato csv con los siguiente campos
# "Id","ProductId","UserId","ProfileName","HelpfulnessNumerator","HelpfulnessDenominator","Prediction","Time","Summary","Text"
# devuelve un archivo en formati predictor | texto

def getLineVWFromCSVLine(lineCSV, isFileTest):

		if isFileTest:
			label = '1'
		else:
			label = lineCSV["Prediction"]

		return label + " '"+lineCSV["Id"]+" | " + cleanLine(lineCSV["Text"])

def cleanLine(line):
	return " ".join(re.findall(r'\w+', line,flags = re.UNICODE | re.LOCALE)).lower()

def getParameters():
	pathToCsvFile = ''
	pathToVWFile = ''
	isFileTest = 0

	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:o:t",["help","input-csv=","output-vw=","test"])
	except getopt.GetoptError:
		print('get_vw_file_from_csv.py -i <input-csv> -o <output-vw> -t')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('get_vw_file_from_csv.py -i <input-csv> -o <output-vw> -t')
			sys.exit()
		elif opt in ("-i", "--input-csv"):
			pathToCsvFile = arg
		elif opt in ("-o", "--output-vw"):
			pathToVWFile = arg
		elif opt in ("-t", "--test"):
			isFileTest = 1

	return (pathToCsvFile, pathToVWFile, isFileTest)

def main():
	files = getParameters()
	fileout_vw = open(files[1], 'w')

	with open(files[0]) as csvfile:
		reader = csv.DictReader(csvfile)
		print('Convritiendo.',end="")
		for line in reader:
			lineVW = getLineVWFromCSVLine(line,files[2])
			fileout_vw.write(lineVW + "\n")
			print('.',end="")

	fileout_vw.close()
	print("Archivo generado en "+files[1])

main()