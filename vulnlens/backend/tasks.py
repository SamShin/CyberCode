"""
Celery app setup.
"""
# Imports

def run_scan_task(scan_id, user_id, target, provider, encrypted_api_key, model_name):
    '''Decrypts key in memory -> runs static scanner -> runs AI engine -> stores full result JSON back to DB -> never persists decrypted key.'''
    pass
