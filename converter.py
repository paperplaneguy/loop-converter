
print("Enter the for loop. Terminate with an empty line.")

# get the for loop from input.
code = ""
line = input()
while line != "":
    code += line
    line = input()

# if there is no for loop, exit.
if code.find("for") == -1:
    print("No for loop found.")
    exit()

temp = code[code.find("(") + 1:code.find(")")]
# remove the initializer list, conditon and the statement from temp and remove the remaining space.
init_list = temp[0:temp.find(";") + 1]; temp = ' '.join(temp[temp.find(";") + 1:].strip().split())
condition = temp[0:temp.find(";")];     temp = ' '.join(temp[temp.find(";") + 1:].strip().split())
statement = temp[0:temp.find(";") + 1]

# strip the main code
code = ' '.join(code[code.find(")") + 1:].strip().split())

# print the result
print("{0};".format(init_list))
print("do {")
print("\t{0}".format(code))
print("\t{0}".format(statement))
print("}} while({0});".format(condition))