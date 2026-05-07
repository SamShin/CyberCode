# VulnLens AI Prompts

## Overview

VulnLens uses LLM prompts for security analysis. This document describes the prompt templates used.

## Prompt Categories

### 1. Finding Analysis Prompts

**Purpose**: Analyze a security finding in detail

**Template Variables**:
- `finding_type`: Type of security issue
- `code_snippet`: Relevant code excerpt
- `file_path`: Location of the issue
- `context`: Additional context about the application

**Output**: Detailed analysis of the vulnerability, potential impact, and exploitation scenarios

### 2. Remediation Prompts

**Purpose**: Generate fix recommendations

**Template Variables**:
- `vulnerability_type`: Classification of vulnerability
- `code_context`: Code that needs fixing
- `framework`: Web framework being used
- `language`: Programming language

**Output**: Step-by-step remediation instructions with code examples

### 3. Finding Correlation Prompts

**Purpose**: Link related findings that compound risk

**Template Variables**:
- `findings_list`: Array of findings to correlate
- `code_sections`: Relevant code sections
- `application_type`: Type of application

**Output**: Grouped findings with explanation of relationships and compound risk assessment

### 4. Severity Assessment Prompts

**Purpose**: Determine severity level of finding

**Template Variables**:
- `vulnerability_details`: Full finding information
- `application_context`: Purpose and data sensitivity of application
- `environment`: Production/staging/dev context

**Output**: Severity level (critical, high, medium, low, info) with reasoning

## LLM Configuration

### Supported Models
- Claude 3.5 Sonnet (recommended)
- Claude 3 Opus
- OpenAI GPT-4
- Custom models via API

### Token Limits
- Analysis prompts: max 1024 tokens
- Remediation prompts: max 2048 tokens
- Correlation prompts: max 2048 tokens
- Severity assessment: max 512 tokens

### Temperature Settings
- Analysis: 0.3 (deterministic)
- Remediation: 0.5 (balanced)
- Correlation: 0.4 (focused)
- Severity: 0.2 (precise)

## Error Handling

- Timeout: 30 seconds per API call
- Retry logic: 3 attempts with exponential backoff
- Fallback: Use rule-based severity if LLM fails
- Logging: All API calls logged for audit

## Cost Optimization

- Batch similar findings for analysis
- Cache common analysis patterns
- Skip LLM analysis for low-severity findings
- Use structured output format for faster parsing
