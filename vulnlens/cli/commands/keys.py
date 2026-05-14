"""
CLI Keys management.
"""
# Imports

def keys_list():
    '''vulnlens keys list — lists user's saved AI provider keys (no values shown)'''
    pass

def keys_add():
    '''vulnlens keys add — prompts for provider, nickname, api key, model name, optional endpoint (local only), POSTs to /apikeys/'''
    pass

def keys_remove(id: int):
    '''vulnlens keys remove <id> — DELETEs key by ID'''
    pass

def keys_edit(id: int):
    '''vulnlens keys edit <id> — updates nickname or model name'''
    pass
