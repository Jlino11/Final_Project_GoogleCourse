#This is the final activity for my portfolio 

#Function to read and transform from string a list
def Extract_allow(allow_list):
    
    #open the file that contains the allow list
    with open(allow_list, "r") as file:

        #To read the archive we use:
        text = file.read()
        
        #To parse the content from string at list
        text = text.split()

    return text


#Function to read and transform from string a list
def Extract_remove(remove_list):
    
    #open the file that contains the allow list
    with open(remove_list, "r") as file:

        #To read the archive we use:
        text = file.read()
        
        #To parse the content from string at list
        text = text.split()

    return text

#Function to iterate elements in a list
def iterate(anylist):
    #To interate in each element of the list
    for element in anylist:

        print(element, end=" ")

#Function to updates ip address that are allowed
def update_ips(list_to_allow, allow_list, remove_list):
    with open(list_to_allow, "w") as file:
        for element in allow_list:
            if element in remove_list:
                allow_list.remove(element)
        allow_list = "\n".join(allow_list)
        file.write(allow_list)
    
    with open(list_to_allow,"r") as file:
        text = file.read()
        return text

#I set the name of the archive in a variable
list_to_allow = "allow_list.txt"
allow_list = Extract_allow(list_to_allow)

#I set the name of the archive in a variable
list_to_remove = "remove_list.txt"
remove_list = Extract_remove(list_to_remove)

text = update_ips(list_to_allow, allow_list, remove_list)
print(text)

