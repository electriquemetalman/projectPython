#lab 2
#bol1 = True
#bol2 = False
#comp = 4j
#num1 = 4.5
#num2 = 4
#result = num1/num2
#print(result)
#print("python has tree numeric type: int, float, and complex")
#print(str(bol1) + " is from the data type " + str(type(bol1)))
#print(str(bol2) + " is from the data type " + str(type(bol2)))
#print(str(comp) + " is from the data type " + str(type(comp)))
#print(str(num1) + " is from the data type " + str(type(num1)))
#print(str(num2) + " is from the data type " + str(type(num2)))

#lab 3
#exercice 1
#myString = "bonjour stiving"
#print (type(myString))
#print (myString + " is of the data type string " + str(type(myString)))

#exercice 2
#firstString = "water"
#secondString = "fall"
#tirthString = firstString + secondString
#print ("this  is a string " + str(type(tirthString)) + tirthString)

#exercice 3
#name = input ("wath is your name ?")
#print(name)

#exercice 4
#name = input ("wat is your name ?")
#olor = input ("wath is your favorise color ?")
#animal = input ("wat is your favorise animal ?")
#print("{}, you like a {} {}!".format(name,color,animal))

#lab 4
#exercice 1
#myFruitList = ["banane","avocat","papay","pasteque"]
#print(myFruitList)
#print(type(myFruitList))
#print(myFruitList[0])
#print(myFruitList[1])
#print(myFruitList[2])
#print(myFruitList[3])
#myFruitList[0] = "orange"
#print(myFruitList[0])

#exercices 2
"""
myFinalAnswerTuple = ("bonbon", "biscuit", "chocolat")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print (myFinalAnswerTuple[0])
"""
#exercice 3
"""
myFovoriteFruitDictionary = {
    "marco" : "banane",
    "marcel" : "tomate",
    "marchal" : "papaye",
}

print (myFovoriteFruitDictionary)
print (type(myFovoriteFruitDictionary))
print (myFovoriteFruitDictionary["marco"])
print (myFovoriteFruitDictionary["marcel"])
print (myFovoriteFruitDictionary["marchal"])
"""

#lab 5
myMixedTypeList = [18 , 202458, 1.12, True, "My dog is on the bed", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}". format(item,type(item)))

#lab 6
"""
import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

myInventoryList = []

with open('C:\japprendvue\car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column name are: {", ".join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'processed {lineCount} lines.')         
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")  

"""

#lab 7
#exercice 1

