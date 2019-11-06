#import regular expressions
import re
#allows us to count occurrencies of words
import collections

text = open('file_io/book.txt').read().lower()
#findall method ensures that all occurrences of the pattern are found.
# \w+ => w = anything that isn`t a white space, + = one or more
#So for every occurrence of one or more characters that are not whitespace, we view as a word. we may get false positives from there but it works fine for this example
words = re.findall('\w+', text)
#counter method from collections counts how many occurrences there are and the most_common() methor limits the results to 10 words
print(collections.Counter(words).most_common(10))