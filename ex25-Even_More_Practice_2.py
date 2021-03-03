# Imports the items defined in ex25_Even_More_Practice_1.py as a moduleso that we can use it's defined functions.
# Could also use: from ex25_Even_More_Practice_1 import *
import ex25_Even_More_Practice_1  

sentence = "All good things come to those who wait."

words = ex25_Even_More_Practice_1.break_words(sentence)
sorted_words = ex25_Even_More_Practice_1.sort_words(words)
sorted_words
ex25_Even_More_Practice_1.print_first_word(words)
ex25_Even_More_Practice_1.print_last_word(words)
words
ex25_Even_More_Practice_1.print_first_word(sorted_words)
ex25_Even_More_Practice_1.print_last_word(sorted_words)
sorted_words
sorted_words = ex25_Even_More_Practice_1.sort_sentence(sentence)
sorted_words
ex25_Even_More_Practice_1.print_first_and_last(sentence)
ex25_Even_More_Practice_1.print_first_and_last_sorted(sentence)