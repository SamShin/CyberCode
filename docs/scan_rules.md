# VulnLens Security Rules

## Overview

VulnLens includes 8 major security rule categories for static analysis:

## 1. HTTP Security Headers (headers.py)

Detects missing or misconfigured security headers in HTTP responses:
- Content-Security-Policy (CSP)
- X-Frame-Options
- X-Content-Type-Options
- Strict-Transport-Security (HSTS)
- X-XSS-Protection
- Referrer-Policy

## 2. Secrets Detection (secrets.py)

Identifies hardcoded sensitive information:
- API keys and tokens
- Database passwords
- Private keys and certificates
- OAuth credentials
- AWS secret keys
- JWT tokens

## 3. Injection Vulnerabilities (injection.py)

Detects potential injection attacks:
- SQL Injection patterns
- Command Injection patterns
- Cross-Site Scripting (XSS) patterns
- LDAP Injection
- OS Command Injection

## 4. Authentication & Authorization (auth.py)

Identifies weak authentication implementations:
- Weak password policies
- Missing authorization checks
- Privilege escalation risks
- Weak session management
- Insecure password storage

## 5. Configuration Security (config.py)

Detects insecure configurations:
- Debug mode enabled in production
- Insecure default values
- Exposed environment variables
- .env file commits
- Verbose error messages

## 6. Cookie Security (cookies.py)

Validates cookie security attributes:
- Missing Secure flag
- Missing HttpOnly flag
- Weak SameSite policies
- Missing Path restrictions
- Long expiration times

## 7. Miscellaneous Security (misc.py)

Additional security checks:
- CORS misconfiguration
- Missing CSRF protection
- Outdated dependencies with known CVEs
- Insecure SSL/TLS configuration

## 8. Phase 2 Dynamic Analysis (placeholder.py)

Coming in Phase 2:
- Live application scanning
- HTTP probing and endpoint discovery
- Form fuzzing
- Network traffic analysis
- Runtime behavior monitoring

## Rule Execution

Rules are executed in priority order:
1. High-priority rules execute first (secrets, injection)
2. File prioritization focuses on high-risk files
3. Results are aggregated and deduplicated
4. AI module enhances findings with context
5. Severity is assigned based on CVSS principles

## Integration with AI Module

Each finding can be enhanced by the AI module:
- Provide additional context about the vulnerability
- Suggest remediation steps
- Identify related findings that compound the risk
- Classify severity using LLM analysis
