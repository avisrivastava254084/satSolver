main_array = ['and'] # array where the new type would be stored
temp_list = list() #for conversion fo line

with open('input_file.txt') as f:
    file_content = f.readlines() #reading the file

file_content = [x.strip() for x in file_content] 
file_content = file_content[2:len(file_content)] # ignoring the first two lines of the file
for line in file_content:
    temp_list = ['or']
    line = list(map(int, line.strip().split(' '))) # converting the characters in the line to int
    line = line[0:len(line)-1] # ignoring the zeroes at the end 
    for char in line:
        if char < 0:
            temp_list.append(['not',str(abs(char))]) # if negative adding the NOT and string of abs of the number
        else:
            temp_list.append(str(char)) # if positive just adding the string of the number
    main_array.append(temp_list)


for j in main_array:
    print(j)
