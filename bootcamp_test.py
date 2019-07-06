# Student Name/Author : Mohak Wathare
# Start Date : 7th July 2019
# Last Modified Date : 7th July 2019

# Function for accepting number list.
# Out : number list.
def input_numbers():
    # flag for checking list input termination
    check = True
    # list for storing integers
    list_of_elements = []
    print("Input numbers. Enter any character string to stop.")
    while(check):
        try:
            # accepting input
            element = int(input())
            # adding in list if valid input
            list_of_elements.append(element)
        except(RuntimeError, TypeError, ValueError):
            # breaking loop in case of invalid input
            check = False

    return list_of_elements


# Function for finding pairs from the number list.
# In : number list.
def find_pairs(list_of_elements):
    # looping through each element for checking pairs
    for i in range(len(list_of_elements)):
        num_i = list_of_elements[i]
        # second loop
        for j in range(i+1, len(list_of_elements)):
            num_j = list_of_elements[j]
            # checks for product being even and sum being odd
            if ((num_i * num_j) % 2 == 0) and ((num_i + num_j) % 2 != 0):
                print("{", num_i, ",", num_j, "}")


list_of_elements = input_numbers()
print("Pairs are - ")
find_pairs(list_of_elements)