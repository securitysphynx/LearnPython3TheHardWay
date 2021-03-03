import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    #line is the result of the line being read from the language file defined in the first argument passed to the function.
    line = language_file.readline()
    # this if only runs if line = 1 which means if line exists. 
    if line:
        #This is the second function. See below for it's explanation.
        print_line(line, encoding, errors)
        #Important note - this is calling the function from inside the function. This will go on forever, UNTIL the if statement evaluates as false. 
        return main(language_file, encoding, errors)

# print line takes the line variable defined in the main() function, and also takes arguments for encoding and errors, which are the same as those that are provided to main.
def print_line(line, encoding, errors):
    #This strips the training \n on the line string. 
    next_lang = line.strip()
    #Encode Bytes: 
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #Decode Strings:
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    #in each iteration of the lines in the file, it will output the bytes and the string. The if line will prevent this loop from going indefinitely. 
    print(cooked_string, "    <============>   ", raw_bytes)

# You could also tell it to open something provided by the user, as an input? 
languages = open("languages.txt", encoding="utf-8")

#This calls the function, with it's arguments.  I'm still not sure about error? 
main(languages, input_encoding, error)