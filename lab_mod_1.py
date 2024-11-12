#Creates function to return even or odd number based on input

def even_or_odd(number):
    answer = int(number)
    
    if answer % 2 == 0:
        return("Even")
    
    else:
        return("Odd")
    
#prints out answer to function called
print("Your number is "+ even_or_odd(82)+"!")

#Creates function to convert int to str
def number_to_string(num):
    answer = str(num)
    
    # Return a string of the number here!
    return answer

print("\nYour number in string form is "+ number_to_string(78.5))

#Creates a function that counts vowels in a string


def get_count(sentence):
    vowels = "aeiou"    
    
    #Creates a for loop that returns the number of vowels in a given string
    return sum(sentence.count(vowel)for vowel in vowels)
 
#Inputs the string to be counted       
string = ""

#prints empty line
print("\n")  

#prints number of vowels in the given string    
print("The number of vowels in this sentence is " + str(get_count(string)) +"!\n")
    