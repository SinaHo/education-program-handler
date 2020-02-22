'''
EDUCATION_PROGRAM HANDLER BY : SINA HONARVAR August 2017
    Users Module /// 
           Accepts new users and saves their data in their specefic folder
           handles users data
           '''


import os
import json



#____________________________________________________GENERAL METHODS:

def create_empty_profile(user_name, user_data_json):
    """Creates empty profile folder and files for new users"""
    user_data = json.loads(user_data_json)
    [grade, field] = list(user_data.values())[3:4]

    os.chdir("users/{}.{}".format(grade, field))
    os.mkdir("{}_PROFILE".format(user_name))
    os.chdir("{}_PROFILE".format(user_name))
    os.mkdir("GENERAL_DATA")
    os.mkdir("programs")
    os.mkdir("education_log")
    with os.chdir("GENERAL_DATA"):
        temp_file = open("base_data.json", 'w')
        json.dump(user_data,temp_file)
        temp_file.close()
        os.chdir("..")
    with os.chdir("education_log"):
        temp_file = open("averages.json", 'w')
        temp_file.close()
        os.chdir("..")
    

    os.chdir("../../..")

def create_new_log(json_log):
    '''
    Creates a json file containing the json formed log
    '''
    if 'users' not in str(os.getcwd()): 
        # checks if the current working directory is the user's profile otherwise changes it to user's profile folder
        os.chdir("users/{}.{}/{}_PROFILE".format(json_log[0][0][2], json_log[0][0][3], json_log[0][0][0]))
        dir_changed = True
    os.chdir("education_log")
    with open("test-{}.json".format(json_log[1][0][0]), 'w') as out_file:
        json.dump(json_log, out_file)
        out_file.close()
    if dir_changed:
        os.chdir("../../..")

def create_new_program(json_program):
    '''
    Creates a json file containing the json formed program
    '''
    if 'users' not in str(os.getcwd()):
        # checks if the current working directory is the user's profile otherwise changes it to user's profile folder
        os.chdir("users/{}.{}/{}_PROFILE".format(json_program[0][2], json_program[0][3], json_program[0][0]))
        dir_changed = True
    os.chdir("programs")
    with open("{}_program.json".format(json_program[0][4]), 'w') as out_file:
        json.dump(json_program, out_file)
        out_file.close()
    if dir_changed:
        os.chdir("../../..")


def find_user_data(name):
    '''
    returns data of the user given which his/her name given
    '''
    with open("users/all_users.json",'r') as all_users:
        [phone_number, school, grade, field] = json.loads(all_users)[name][:]
        all_users.close()
    return [phone_number, school, grade, field]

def load_user(user_name):
    '''
    Loads a user using User Class just with giving name
    Only for old users
    '''
    if 'users' not in str(os.getcwd()):
        cwd = os.getcwd()
        os.chdir('users')
        dir_changed = True
    elif '_PROFILE' in str(os.getcwd()):
        cwd = os.getcwd()
        os.chdir("../..")
        dir_changed = True

    with open("all_users.json",'r') as all_users:
        [grade, field] = json.loads(all_users.read())[user_name][1:2]
        all_users.close()
    os.chdir("{}_{}/{}".format(grade, field, user_name))
    with open("GENERAL_DATA/base_data.json") as base_data:
        user_data_json = json.loads(base_data.read())
        base_data.close()
    user = User(user_name, user_data_json)
    if dir_changed:#changes directory to previous dir
        os.chdir(cwd)
    return user 



#____________________________________________________________________________CLASS USER STARTS:



class User:
    '''
    Creates and loads an object for each user
    '''
    def __init__(self, name, user_data_json, is_new=False):
        '''
        Base __init__ function accepts user's name and json structured data as parameters 
        If the user doesn't have a profile already 'is_new' becames True otherwise False
        '''

        self.name = name   #   "User full name in the format 'first_name last_name' "

        if is_new:
            create_empty_profile(self.name, user_data_json)    #    To create empty folders and log files for new users
        [grade, field]=find_user_data(name)[2:]
        os.chdir("users/{}.{}/{}_PROFILE".format(grade, field, name))
    
    
    def new_edu_log(self, json_log):
        '''
        User's education log that has changed into json form , will be saved in the server here
        '''
        json_data = json.loads(json_log)
        try:
            create_new_log(json_data)
        except Exception:
            os.mkdir(".__ERRORS__")
            os.chdir(".__ERRORS__")
            with open("json_file_creation_error.err", 'w') as er_file:
                er_file.write(str(Exception))
                er_file.close()
                os.chdir("..")

    def new_program(self, json_program):
        '''
        User's defined program will be saved here
        '''
        json_data = json.loads(json_program)
        try:
            create_new_program(json_data)
        except Exception:
            os.mkdir(".__ERRORS__")
            os.chdir(".__ERRORS__")
            with open("json_file_creation_error.err", 'w') as er_file:
                er_file.write(str(Exception))
                er_file.close()
                os.chdir("..")
    





# __ DEBUG FUNCTION __
"""
Debugs the Mudole for inital uses
"""
def __debug():
    print("debug function")

if __name__ == '__main__':
    __debug()
