name = "Ayush Agrawal"
print(name[0:4])
# for negative sliceing 
print(name[0:-4])
print(name[len(name)-5:len(name)])
#prints the length of var
print(len(name))
# String are immutable which mean string cannot be changed so a new string is made



# for upper case 
a = "tatya @@@@@"
print(a.upper())
# for lower case
print(a.lower())
# to strip from end
print(a.rstrip("@"))
# to replace for all occurences
print(a.replace('tatya',"panner"))
# to splite a string
print(a.split(" "))
# to capitalize 
print(a.capitalize())
#  to print a center text
print(a.center)
# to count a specific occurences
print(a.count("@"))
# to chech a string end 
print(a.endswith("@"))
# to find a character
print(a.find("a"))