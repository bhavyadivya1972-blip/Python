''' List Comprehension'''

poem = ['aao' , 'millo' , 'sillo' , 'salo' , 'kachhe' , 'dhaage' , 'race' , 'lagalo']

letter_cont_o = [ item for item in poem if 'o' in item]
print(letter_cont_o) # Output: ['aao', 'millo', 'sillo', 'salo']

letter_cont_4 = [ item for item in poem if len(item) == 4]
print(letter_cont_4) # Output: ['salo', 'race']