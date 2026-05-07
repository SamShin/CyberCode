# VulnLens Architecture

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend (React/Vite)               │
│                                                               │
│  ┌────────────────┐  ┌──────────────┐  ┌──────────────────┐ │
│  │     Pages      │  │  Components  │  │   API Clients    │ │
│  └────────────────┘  └──────────────┘  └──────────────────┘ │
└────────────────────────┬──────────────────────────────────────┘
                         │ HTTP/REST
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  Nginx Reverse Proxy                         │
│                                                               │
│  Routes /api/* → Backend:8000                                │
│  Routes / → Frontend:80                                      │
└────────────────────────┬──────────────────────────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │                                 │
        ▼                                 ▼
┌──────────────────┐        ┌────────────────────────────────┐
│   FastAPI        │        │  Scanner Engine                │
│   Backend        │        │  (Python)                      │
│                  │        │                                │
│ - REST Routes    │        │ ┌──────────────────────────┐  │
│ - Auth (JWT)     │        │ │ Static Analysis Module   │  │
│ - User Management│        │ │ - Rules Engine           │  │
│ - Scan Service   │        │ │ - File Prioritizer       │  │
│ - Report Export  │◄──────►│ │ - 8 Security Rules       │  │
│                  │        │ └──────────────────────────┘  │
│                  │        │                                │
│                  │        │ ┌──────────────────────────┐  │
│                  │        │ │ AI Analysis Module       │  │
│                  │        │ │ - LLM Client             │  │
│                  │        │ │ - Prompt Engine          │  │
│                  │        │ │ - Severity Classification│  │
│                  │        │ └──────────────────────────┘  │
│                  │        │                                │
│                  │        │ ┌──────────────────────────┐  │
│                  │        │ │ Report Generation        │  │
│                  │        │ │ - Builder                │  │
│                  │        │ │ - CLI Formatter          │  │
│                  │        │ │ - Export Formatter       │  │
│                  │        │ └──────────────────────────┘  │
│                  │        │                                │
│                  │        │ ┌──────────────────────────┐  │
│                  │        │ │ Code Ingestion Module    │  │
│                  │        │ │ - Local FS Ingestion     │  │
│                  │        │ │ - GitHub Ingestion       │  │
│                  │        │ └──────────────────────────┘  │
└──────────┬───────┘        │                                │
           │                │ ┌──────────────────────────┐  │
           │                │ │ Phase 2: Dynamic Analysis│  │
           │                │ │ (Placeholder)            │  │
           │                │ └──────────────────────────┘  │
           │                │                                │
           │                └────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────────────┐
│              PostgreSQL Database                             │
│                                                               │
│ Tables:                                                       │
│ - users (authentication & profiles)                           │
│ - scans (scan history & metadata)                             │
│ - findings (scan results)                                     │
│ - apikeys (API key management)                                │
└──────────────────────────────────────────────────────────────┘
```

## Module Breakdown

### Frontend (React/Vite)
- Single-page application for scan management
- Real-time dashboard with scan status
- Report viewing and comparison tools
- User authentication and API key management

### Backend (FastAPI)
- REST API for all operations
- JWT-based authentication
- Database ORM with SQLAlchemy
- Service layer for business logic

### Scanner (Python)
- Static analysis engine with 8 rule categories
- AI-powered enhancement of findings
- Support for local and GitHub code ingestion
- Multiple export formats (JSON, CSV, PDF, SARIF)
- Phase 2: Docker-sandboxed dynamic analysis

### Database
- PostgreSQL for persistence
- Alembic for schema migrations
- User management, scan tracking, finding storage

## Data Flow

1. User initiates scan via CLI or web UI
2. Scanner ingests code (local or GitHub)
3. Static analysis rules run against code
4. AI module enhances findings with context
5. Report builder aggregates results
6. Results stored in database
7. Frontend displays findings with visualizations
8. User can export in multiple formats

## Security Considerations

- JWT-based API authentication
- API keys for programmatic access
- Password hashing with bcrypt
- Environment-based configuration
- CORS policy for frontend
- SQL injection prevention via SQLAlchemy ORM
