import os
import filecmp
from dateutil.relativedelta import *
from datetime import date

# TEST COMMIT 

def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	data = []
	doc = open(file, 'r')
	keys = doc.readline()
	for line in doc:
		line = line.split(",")
		student = dict()
		student["First"] = line[0]
		student["Last"] = line[1]
		student["Email"] = line[2]
		student["Class"] = line[3]
		student["DOB"] = line[4]

		data.append(student)
	doc.close()
	return data
	

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	sortedData = sorted(data, key=lambda k: k[col])
	topPerson = sortedData[0]
	return (topPerson["First"] + " " + topPerson["Last"])



def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	freshCount = 0
	sophCount = 0
	juniorCount = 0
	senCount = 0

	for item in data: 
		if item["Class"] == "Freshman":
			freshCount += 1
		elif item["Class"] == "Sophomore":
			sophCount += 1
		elif item["Class"] == "Junior":
			juniorCount += 1
		else: 
			senCount += 1
	countList = list()
	freshTuple = ("Freshman", freshCount)
	countList.append(freshTuple)
	sophTuple = ("Sophomore", sophCount)
	countList.append(sophTuple)
	junTuple = ("Junior", juniorCount)
	countList.append(junTuple)
	senTuple = ("Senior", senCount)
	countList.append(senTuple)
	sortedList = sorted(countList, key=lambda k: k[1], reverse=True)
	return sortedList

def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	months = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, 
		'9':0, '10':0, '11':0, '12':0}

	for student in a:
		DOB = student["DOB"]
		#print("date: " + str(DOB))
		dateList = DOB.split("/")
		month = dateList[0]
		#print("Month: " + month)
		months[month] += 1
		#print(months)
	print(months)

	sortedMonths = sorted(months, key=lambda k: (int(k[])), reverse=True)
	return sortedMonths[0][0]


def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	pass

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():

	data = getData('P1DataA.csv')
	print("Type of Data: ")
	mySort(data,'First')

	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
