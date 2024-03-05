#   Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence:0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" 
# pull apart the line to extract the floating-point number on the line. 
# Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.

# add egg
# Sometimes when programmers get bored or want to have a bit of fun, they add a harmless
# Easter Egg to their program Modify the program that prompts the user for the file name so 
# that it prints a funny message when the user types in the exact file name "na na boo boo". 
# The program should behave normally for all other files which exist and don't exist.

fname = input('File Name is: ')
count = 0
stotal = 0
searchabout = 'X-DSPAM-Confidence:'

try:
    fhost = open(fname)
except:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    else:
        print('File cannot be opened:', fname)    
    exit()


for line in fhost: 
    if line.startswith(searchabout):
        count = count + 1
        stotal = stotal + float(line[len(searchabout)+1:])
if count == 0:
    exit()
print('average spam confidence:', stotal / count)
