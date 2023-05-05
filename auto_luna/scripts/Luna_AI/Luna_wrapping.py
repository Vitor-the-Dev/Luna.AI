import os
#wraps misc LLM, wraps image generator, wraps speak, wraps other wrappers.
#wrapper will need to give the AI access to the nest API, it manages control to tools
#This program connects with the Django backend, both to use it as a bridge to the front and to have access to more delicate wrappers that may need to be separated
def access_api_wrapper(self, *args): #uses Django route to acess wrapper, useful for adding a layer of security
    return 0

def access_local_wrapper(self, *args): #access a local wrappers
    
    return 0
def list_api_wrappers(self, *args):#list avaliable APIs on Django backend

    return 0
def json_api_query(self, *args):
    
    return 0
