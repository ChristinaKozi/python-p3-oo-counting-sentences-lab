#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        count = 0
        punctuation_marks = ['.', '!', '?']
        sentences = self.value.split()
        for sentence in sentences:
          if sentence.endswith(tuple(punctuation_marks)):
            count+= 1
        return count 