# Dictonary examples to learn from

# creates a dictionary
# with numbers as key
# values as numbers
num_as_key = {0: [{5: 4, 2: 8},
                  {1: 7, 2: 9}],
              1: [{23: 523, 1000: 22},
                  {25: 33, 43: 32}]}

# creates a dictionary
# with stings as key
# values as numbers
string_as_key = {'first': [{5: 4, 2: 8},
                           {1: 7, 2: 9}],
                 'second': [{23: 523, 1000: 22},
                            {25: 33, 43: 32}]}

# creates a dictionary
# with numbers as key
# values as lists of numbers
list_of_numbers = {'10': [[50, 400, 20, 80],
                          [1, 70, 2, 9]],
                   '20': [[23, 5203, 11200, 22],
                          [25, 303, 43, 32]]}
#CHALLANGE make your own Dictonary and print the values out. Try chaning the keys
# and try changing or expanding the values
first_dictionary = {'third': [10, 15, 20, 25, 30],
                    'fourth': [2, 4, 6, 8, 12]}
# printing  lists of data and keys in a few ways
# using items() method
print("accessing  lists of data and keys in a few ways")
print("accessing a dictionary with a number as the key")


#for key, values in num_as_key.items():
#CHALLANGE make a condition to set 1 of the Dictonaries to a new variable
#for i in values:
# print(key, " : ", i)
b = first_dictionary

for key, values in b.items():
 # print(key, " : ", i)
  for i in values:
      a = 'third'
      print(key, " : ", i)
      if(key == a):
          print(i+1)
    #print(i)
      if(key == 'fourth'):
         print(i+3)
    #    print(i[0])
    #if(i > 10):
    #print("im high")

    #for key, values in list_of_numbers.items():
    #for lists in values:
    #print(lists)
    ##print(lists[0])
    #if(lists[0] < 25):
    #print("im low")

    #for key, values in Second_dictionary.items():
    #for i in values:
    #print(list)  # notice the loop is going over values for each key

print("now accessing with a sting based key")

for key, values in string_as_key.items():
    for i in values:
        print(key, " : ", i)

print("*removed printing the key twice*")

for key, values in string_as_key.items():
    for i in values:
        print(i)

print("Now what if only use key instead of key, values?")
for key in string_as_key.items():
    print(key)

print("with second loop, notice both lists are printed at once, one key is printed")
for key in string_as_key.items():
    print(key)
    for values in key:
        print(values)

print("a Dictonary with lists as the value")

for key, values in list_of_numbers.items():
    for lists in values:
        print(lists)
        print(lists[0])
        if(lists[0] < 25):
          print("im low")
