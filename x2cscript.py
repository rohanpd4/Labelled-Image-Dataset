import xml.etree.ElementTree as ET
import csv

tree = ET.parse("600.xml")
root = tree.getroot()

# open a file for writing

Resident_data = open('BoundingBox.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []

count = 0
for member in root.findall('object'):
	resident = []
	address_list = []
	if count == 0:
		name = member.find('name').tag
		resident_head.append(name)
		Address = member[4].tag
		print(Address)
		resident_head.append(Address)
		csvwriter.writerow(resident_head)
		count = count + 1

	name = member.find('name').text
	resident.append(name)
	xmin = member[4][0].text
	address_list.append(xmin)
	ymin = member[4][1].text
	address_list.append(ymin)
	xmax = member[4][2].text
	address_list.append(xmax)
	ymax = member[4][3].text
	address_list.append(ymax)
	resident.append(address_list)
	csvwriter.writerow(resident)
Resident_data.close()
