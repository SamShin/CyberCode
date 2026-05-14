"""
SQLAlchemy session setup.
If DATABASE_URL env var not set, default to SQLite ./vulnlens_dev.db. swap to PostgreSQL in production via env var.
"""
# Imports

def get_db():
    '''Yields DB session.'''
    pass
