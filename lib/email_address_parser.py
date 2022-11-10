# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, string):
        self.string = string
        pass

    def parse(self):
        regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
        email_list =  regex.findall(self.string)
        email_list.reverse()
        return email_list
        pass
    pass
