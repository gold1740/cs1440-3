import sys
from Report import Report

if len(sys.argv) < 2: 
	print(sys.argv[0], "DATA_DIRECTORY")
	exit("Directory not specified")


# initialize tracker variables
#################################################
num_areas = 0
gross_annual_wage = 0
max_annual_wage = ["", 0]
total_estab = 0
max_estab = ["", 0]
total_empl = 0
max_empl = ["", 0]

soft_num_areas = 0
soft_gross_annual_wage = 0
soft_max_annual_wage = ["", 0]
soft_total_estab = 0
soft_max_estab = ["", 0]
soft_total_empl = 0
soft_max_empl = ["", 0]


# Convert `area_titles.csv` into a dictionary
#############################################
num_areas = 0
area_titles = {}
file = open(sys.argv[1] + "area_titles.csv")
list = file.readlines()
for i in range (0, len(list)):
	line = list[i].split(',')
	for j in range(len(line)):
		line[j] = line[j].strip("\n").strip('\"')
	if (not line[0].isnumeric()) or line[0].endswith('000'):
		continue
	area_titles.update({line[0]: line[1] + ',' + line[2] if len(line) == 3 else ""})
file.close()


# Collect stats from `2017.annual.singlefile.csv`
#################################################
file = open(sys.argv[1] + "2017.annual.singlefile.csv")
list = file.readlines()
for i in list:
	i = i.split(',')
	if area_titles.get(str(i[0].strip('\"')), 0) == 0:
		continue
	if i[2] == '"10"' and i[1] == '"0"':	
		title = area_titles.get(i[0].strip('\"'))
		wage = int(i[10].strip('\"'))
		if wage > max_annual_wage[1]:
			max_annual_wage[0] = title
			max_annual_wage[1] = wage
		gross_annual_wage += wage
		estab = int(i[8].strip('\"'))
		if estab > max_estab[1]:
			max_estab[0] = title
			max_estab[1] = estab
		total_estab += estab
		empl = int(i[9].strip('\"'))
		if empl > max_empl[1]:
			max_empl[0] = title
			max_empl[1] = empl
		total_empl += empl
		num_areas +=1		
	if(i[2] == '"5112"' and i[1] == '"5"'):
		title = area_titles.get(i[0].strip('\"'))
		wage = int(i[10].strip('\"'))
		if wage > soft_max_annual_wage[1]:
			soft_max_annual_wage[0] = title
			soft_max_annual_wage[1] = wage
		soft_gross_annual_wage += wage
		estab = int(i[8].strip('\"'))
		if estab > soft_max_estab[1]:
			soft_max_estab[0] = title
			soft_max_estab[1] = estab
		soft_total_estab += estab
		empl = int(i[9].strip('\"'))
		if empl > soft_max_empl[1]:
			soft_max_empl[0] = title
			soft_max_empl[1] = empl
		soft_total_empl += empl
		soft_num_areas +=1
	
# Create the report object
##########################
rpt = Report()


# Fill in the report for all industries
#######################################
rpt.all.num_areas           = num_areas

rpt.all.gross_annual_wages  = gross_annual_wage
rpt.all.max_annual_wage     = (max_annual_wage[0], max_annual_wage[1])

rpt.all.total_estab         = total_estab
rpt.all.max_estab           = (max_estab[0], max_estab[1])

rpt.all.total_empl          = total_empl
rpt.all.max_empl            = (max_empl[0], max_empl[1])


# Fill in the report for the software publishing industry
#########################################################
rpt.soft.num_areas          = soft_num_areas

rpt.soft.gross_annual_wages = soft_gross_annual_wage
rpt.soft.max_annual_wage    = (soft_max_annual_wage[0], soft_max_annual_wage[1])

rpt.soft.total_estab        = soft_total_estab
rpt.soft.max_estab          = (soft_max_estab[0], soft_max_estab[1])

rpt.soft.total_empl         = soft_total_empl
rpt.soft.max_empl           = (soft_max_empl[0], soft_max_empl[1])


# Print the completed report
############################
print(rpt)
