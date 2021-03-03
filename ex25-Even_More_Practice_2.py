# Imports the items defined in lp3thw_25_1.py as a moduleso that we can use it's defined functions.
# Could also use: from lp3thw_25_1 import *
import lp3thw_25_1  

sentence = "All good things come to those who wait."

words = lp3thw_25_1.break_words(sentence)
sorted_words = lp3thw_25_1.sort_words(words)
sorted_words
lp3thw_25_1.print_first_word(words)
lp3thw_25_1.print_last_word(words)
words
lp3thw_25_1.print_first_word(sorted_words)
lp3thw_25_1.print_last_word(sorted_words)
sorted_words
sorted_words = lp3thw_25_1.sort_sentence(sentence)
sorted_words
lp3thw_25_1.print_first_and_last(sentence)
lp3thw_25_1.print_first_and_last_sorted(sentence)