#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value): 
        if isinstance(new_value, str): 
            self._value = new_value
        else: 
            print("The value must be a string.")
            # raise ValueError("The value must be a string.")


    def is_sentence(self):
        return self.value[len(self.value)-1] == "."
        # instead of: 
        # if self.value[-1] == ".": 
        #     return True
        # else:
        #     return False 
        
    def is_question(self):
        return self.value[len(self.value)-1] == "?"
    
    def is_exclamation(self):
        return self.value[len(self.value)-1] == "!"
    
    def count_sentences(self):
        # below is only to count how many punctuation marks
        # return self.value.count(".") + self.value.count("!") + self.value.count("?")
        # instead of: 
        # x = self.value.count(".")
        # y = self.value.count("?")
        # z = self.value.count("!")
        # return x + y + z 
        new_value = self.value.replace("!", ".").replace("?", ".")
        l = new_value.split(".")
        count = 0
        for item in l: 
            if len(item) != 0:
                count += 1
        return count

s = MyString("hello")
print(s.value)
    