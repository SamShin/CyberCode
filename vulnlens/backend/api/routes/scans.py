"""
Scans routes.
"""
# Imports

def create_scan():
    '''POST /scans/ (validates user has at least one API key, enqueues Celery task, returns scan ID immediately)'''
    pass

def list_scans():
    '''GET /scans/ (list history)'''
    pass

def get_scan(id: int):
    '''GET /scans/{id} (full report including raw result JSON)'''
    pass

def get_scan_status(id: int):
    '''GET /scans/{id}/status (poll for task status)'''
    pass

def delete_scan(id: int):
    '''DELETE /scans/{id}'''
    pass
