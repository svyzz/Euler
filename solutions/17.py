import inflect
ie = inflect.engine()

# List comprehension
[a for a in range(1, 5)]
print sum([len(ie.number_to_words(i).replace('-', '').replace(' ', '')) for i in range(1, 1001)])
    

###################################
# l = 0

# for i in range (1, 1001):
#     l += len(ie.number_to_words(i).replace('-', '').replace(' ', ''))

    
# print l
