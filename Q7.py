# Write a Python program to implement a stack using list.

stack = [] #defining variable as a null list

#creating user defined function
def push(stack):

    # taking number of elements from the user
    number_of_elements = int(input("Enter number of elements: "))

    #loop to append the elements in stack
    for i in range(number_of_elements):
        element = int(input("Enter number: "))
        stack.append(element)

    print(stack)

#call function
push(stack)

