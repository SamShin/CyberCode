"""
ApiKey SQLAlchemy model definition.
Plaintext key never stored. One user can have multiple keys across providers.
"""
# Imports

class ApiKey:
    '''SQLAlchemy model fields: id, user_id (FK to user), provider (enum: anthropic / openai / google / local), nickname, encrypted_value, model_name, endpoint_url (for local), created_at.'''
    pass
