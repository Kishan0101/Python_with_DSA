heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
# 1. Find lenghts of heros
a = len(heros)
print(a)

# Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

#You realize that you need to add 'black panther' after 'hulk',
   #so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)

# Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.

heros[1] = 'doctor'
heros[2] = 'strange'
print(heros)

#Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros.sort()
print(heros)