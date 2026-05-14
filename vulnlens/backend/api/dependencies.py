"""
API dependencies.
"""
# Imports

def get_current_user():
    '''Validates JWT from HTTP-only cookie (website) or Authorization: Bearer <token> header (CLI). Returns current user or raises 401.'''
    pass

def rate_limit():
    '''slowapi limiter stub. Apply to scan submission endpoint.'''
    pass
