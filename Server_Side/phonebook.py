'''
phonebook.py mudole/////
used to search in users data
gets the name which has the given phone number and phone number of given name
'''

import json
import re
number_pattern = re.compile(r'^[+|-]{0,1}\d+([.]\d)*\d*$')

def create_phone_book():
    '''
    crates a phonebook object containing usernames and phone numbers
    '''
    with open("all_users.py",'r') as users_file:
        data = json.loads(users_file.read())
        users_file.close()
    phone_book = {}
    for i in range(len(list(data.keys()))):
        phone_book.update({list(data.keys)[i]:list(data.values())[i][0]})
    return phone_book

def search(string, pattern):
    '''
    base search function for every type of string and pattern
    '''
    pat_list = pattern.split(" ")
    for item in pat_list:
        if item in string:
            return True
    return False  
  
    
def search_phonebook(pattern):
    '''
    searchs through the phonebook for possible expected data
    '''
    is_number = number_pattern.match(pattern) != None
    phone_book = create_phone_book()
    ret_dict = {}
    if not is_number:
        for item in list(phone_book.keys()): 
            if search(item, pattern):
                ret_dict.update({item:phone_book[item]})
    else:
        for item in list(phone_book.values()):
            if pattern == item:
                ret_dict.update({phone_book.keys()[phone_book.values().index(item)]:item})
    return ret_dict


