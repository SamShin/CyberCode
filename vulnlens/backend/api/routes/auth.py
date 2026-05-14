"""
Auth routes.
"""
# Imports

def register():
    '''POST /auth/register'''
    pass

def login():
    '''POST /auth/login (returns JWT, sets HTTP-only cookie)'''
    pass

def logout():
    '''POST /auth/logout'''
    pass

def cli_login():
    '''POST /auth/cli-login (accepts email + password, returns a long-lived CLI session token stored in DB)'''
    pass
