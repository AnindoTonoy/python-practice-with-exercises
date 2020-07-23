# This is a dictionary program which take the word from user as input.
# print the meaning as return to the user. The input word have to must
# be in this pre define dictionary or error will be thrown.

d1 = {'Set': "In mathematics, a set is a well-defined collection of distinct objects, considered as an object in its "
             "own right.",
      'Mutable': 'In astrology, mutable signs are associated with adaptability, flexibility and sympathy.',
      'Immutable': 'unchanging over time or unable to be changed.',
      'Object': 'a material thing that can be seen and touched.'}

your_input = input('Enter your word: ')
capitalize_input = your_input.capitalize()

print(f'The meaning of {capitalize_input} is:\n', d1[capitalize_input], end='')
