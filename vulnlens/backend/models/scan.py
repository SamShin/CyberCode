"""
Scan SQLAlchemy model definition.
"""
# Imports

class Scan:
    '''SQLAlchemy model fields: id, user_id (FK), target (GitHub URL or local path string), status (enum: queued / running / complete / failed), result_json (full raw JSON report stored as Text/JSON column), overall_score (float), severity_counts (JSON: {low, medium, high}), created_at, completed_at.'''
    pass
