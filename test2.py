# import enchant
# import itertools
#
#
# uk = enchant.Dict("en_UK")
# us = enchant.Dict("en_US")
#
# def get_input():
#   global MIN_LEN
#   a=input('enter the word: ')
#   MIN_LEN=len(a)
#   pqw=sorted(set(a.rstrip('\r\n')))
#   return pqw
#
# def gen_permutations(ent):
#   tuples = map(lambda i: itertools.permutations(ent,i), range(MIN_LEN,len(ent)+1))
#   arrr= [["".join(j) for j in i] for i in tuples]
#   return list(itertools.chain(*arrr))
#
# def filter_dict(words):
#   return [x for x in words if uk.check(x) or us.check(x)]
#
# for i in filter_dict(gen_permutations(get_input())):
#   print (i)

import enchant

dictionary = enchant.Dict("en_US") #also available are en_GB, fr_FR, etc

 # prints True
 #prints False

print(dictionary.check("Hello"))
print(dictionary.check("Helo"))