#Create a CSV file by entering user-id and password, read and search the password for given userid

#importing csv module
import csv

#opening the csv file, with write privilleges
with open("Q8.csv", "w") as obj:

    fileobj = csv.writer(obj)

    fileobj.writerow(["User Id", "password"])

    #running loop for taking user input

    while(True):

        user_id = input("enter id: ")

        password = input("enter password: ")

        record = [user_id, password]

        fileobj.writerow(record)

        x = input("press Y/y to continue and N/n to terminate the program\n")

        if x in "Nn":

            break

        elif x in "Yy":

            continue

#opening csv file with read privilliges
with open("Q8.csv", "r") as obj2:

    fileobj2 = csv.reader(obj2)

    given = input("enter the user id to be searched\n")

    for i in fileobj2:

        next(fileobj2)

        # print(i,given)

        if i[0] == given:

            print(i[1])

            break#Create a CSV file by entering user-id and password, read and search the password for given userid
