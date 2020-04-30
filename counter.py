"""
Simple python script that takes in a text input and counts
the number of lines in the document for you
"""

# Thank you to: https://stackoverflow.com/a/17303428 for this color class!
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# Take in the user input using the newline character
# to signal a new line in the stored string to bypass
# the exiting of the file write method
print()
print()
print()
print (color.BLUE + "Enter what you want to check the lines of:" + color.END)
print (color.BOLD + "When finished, simply hit enter on an empty line." + color.END)
print ("-----")
userInput="\n".join(iter(input,""))
print ("-----")

# fileName variable to store the name of the .txt file we 
# will be writing to and counting the lines of
fileName = "counter.txt"
# Write the user input to counter.txt; creates the 
# file if it doesnt exist
with open (fileName, "w") as f:
  f.write (userInput)


# Counter iniitialized to count the # of lines in the file
counter = 0
# For loop that runs through the normal reader of the doc text file
for line in open(fileName, 'r'):
        counter += 1
if counter == 1:
    print(color.RED + "There was" + color.END, color.BOLD + str(counter) + color.END, color.RED + "line." + color.END)
else:
    print(color.RED + "There were" + color.END, color.BOLD + str(counter) + color.END, color.RED + "lines." + color.END)

print()
