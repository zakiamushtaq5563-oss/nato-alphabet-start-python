# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
#TODO 1. Create a dictionary in this format:
alpha_file = pandas.read_csv("nato_phonetic_alphabet.csv")
print(alpha_file.to_string)
# list_alpha = alpha_file.readlines()
# print(list_alpha)
# {"A": "Alfa", "B": "Bravo"}
alpha_dict = {row.letter:row.code for (index, row) in alpha_file.iterrows()}
print(alpha_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the word ").upper()
# if "a" in user_input:
#     print("hi")
# list_phonetic = [value for (key, value) in alpha_dict.items() if key in user_input]
list_phonetic = [alpha_dict[letter] for letter in user_input ]
# for letter in user_input:
#     for (key, value) in alpha_dict.items():
#         if letter == key:
#             list_phonetic.append(value)
# list_phonetic_2 = [word  for (key, word) in alpha_dict.items() if key ]         
print(list_phonetic)
