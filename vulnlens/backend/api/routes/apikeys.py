"""
API Keys routes.
"""
# Imports

def list_keys():
    '''GET /apikeys/ (list user's keys - never return decrypted value)'''
    pass

def add_key():
    '''POST /apikeys/ (add new key - encrypt before save)'''
    pass

def update_key(id: int):
    '''PATCH /apikeys/{id} (update nickname or model name)'''
    pass

def delete_key(id: int):
    '''DELETE /apikeys/{id}'''
    pass
