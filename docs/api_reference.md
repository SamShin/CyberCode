# VulnLens API Reference

## Base URL

```
http://localhost:8000/api
```

## Authentication

All endpoints require JWT token in `Authorization` header:

```
Authorization: Bearer <token>
```

## Authentication Endpoints

### POST /auth/login
Login and receive JWT token

**Request**:
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response**:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

### POST /auth/register
Create new user account

**Request**:
```json
{
  "email": "user@example.com",
  "password": "password123",
  "password_confirm": "password123"
}
```

**Response**:
```json
{
  "id": 1,
  "email": "user@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### POST /auth/refresh
Refresh access token

**Response**:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

## Scan Endpoints

### POST /scans
Create and start new scan

**Request**:
```json
{
  "scan_name": "My First Scan",
  "target_path": "https://github.com/user/repo"
}
```

**Response**:
```json
{
  "id": 1,
  "scan_name": "My First Scan",
  "target_path": "https://github.com/user/repo",
  "status": "running",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### GET /scans
List user's scans

**Query Parameters**:
- `limit`: Max results (default: 10)
- `offset`: Pagination offset (default: 0)

**Response**:
```json
[
  {
    "id": 1,
    "scan_name": "My First Scan",
    "target_path": "https://github.com/user/repo",
    "status": "completed",
    "created_at": "2024-01-15T10:30:00Z"
  }
]
```

### GET /scans/{scan_id}
Get scan details

**Response**:
```json
{
  "id": 1,
  "scan_name": "My First Scan",
  "target_path": "https://github.com/user/repo",
  "status": "completed",
  "findings": [
    {
      "id": 1,
      "rule_id": "secrets_001",
      "severity": "high",
      "message": "Potential API key found",
      "file_path": "config.py",
      "line_number": 42
    }
  ],
  "created_at": "2024-01-15T10:30:00Z",
  "completed_at": "2024-01-15T10:35:00Z"
}
```

### DELETE /scans/{scan_id}
Delete a scan

**Response**: 204 No Content

### GET /scans/{scan_id}/export
Export scan results

**Query Parameters**:
- `format`: Export format (json, csv, pdf, sarif) (default: json)

**Response**: File download or JSON/CSV data

## User Endpoints

### GET /users/profile
Get current user profile

**Response**:
```json
{
  "id": 1,
  "email": "user@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### PUT /users/profile
Update user profile

**Request**:
```json
{
  "email": "newemail@example.com"
}
```

**Response**:
```json
{
  "id": 1,
  "email": "newemail@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```

## API Key Endpoints

### POST /apikeys
Generate new API key

**Request**:
```json
{
  "name": "CI/CD Key"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "CI/CD Key",
  "key": "vl_1234567890abcdef",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### GET /apikeys
List API keys

**Response**:
```json
[
  {
    "id": 1,
    "name": "CI/CD Key",
    "created_at": "2024-01-15T10:30:00Z",
    "last_used_at": "2024-01-15T10:35:00Z"
  }
]
```

### DELETE /apikeys/{key_id}
Revoke API key

**Response**: 204 No Content

## Error Responses

All errors follow this format:

```json
{
  "detail": "Error message",
  "error_code": "ERROR_CODE"
}
```

### Common Status Codes

- `200 OK`: Successful request
- `201 Created`: Resource created
- `204 No Content`: Successful deletion
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Missing or invalid token
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error
