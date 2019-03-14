import csv  
import json  

try:

	# file output
	jsonfile = open('file.json', 'w')
    
    # csv register 2017
	csvfile_2017 = open('scopus2017.csv', 'r')
	fieldnames = ("Authors","Author(s) ID", "Title", "Year","Source title", "Cited by", "Link", "Abstract", "Author Keywords",  "Document Type", "Source")
	reader = csv.DictReader( csvfile_2017, fieldnames)

	count = 0
	for row in reader:
		if count >= 1:
			if count <= 850:
				json.dump(row, jsonfile)
				jsonfile.write("\n")
				count+=1
			else:
				break
		else:
			count+=1
			continue

	# csv register 2018
	csvfile_2018 = open('scopus2018.csv', 'r')
	fieldnames = ("Authors","Author(s) ID", "Title", "Year","Source title", "Cited by", "Link", "Abstract", "Author Keywords", "Index Keywords")
	reader = csv.DictReader( csvfile_2018, fieldnames)

	count = 0
	for row in reader:
		if count >= 1:
			if count <= 850:
				json.dump(row, jsonfile)
				jsonfile.write("\n")
				count+=1
			else:
				break
		else:
			count+=1
			continue

	# csv register 2019
	csvfile_2019 = open('scopus2019.csv', 'r')
	fieldnames = ("Authors","Author(s) ID", "Title", "Year","Source title", "Cited by", "Link", "Abstract", "Author Keywords",  "Document Type", "Source")
	reader = csv.DictReader( csvfile_2019, fieldnames)

	count = 0
	for row in reader:
		if count >= 1:
			if count <= 800:
				json.dump(row, jsonfile)
				jsonfile.write("\n")
				count+=1
			else:
				break
		else:
			count+=1
			continue

except Exception as Error:
	print(Error)
