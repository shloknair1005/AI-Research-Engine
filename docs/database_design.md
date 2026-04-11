# Database Design Document

## Overview

This document defines the database schema used in the AI Agent Platform.

The system uses **PostgreSQL** as the primary database and **SQLAlchemy** as the ORM layer.

The database is designed to support:

* AI task execution tracking
* Multi-agent orchestration
* Guardrail monitoring
* Logging and observability
* System analytics

The database schema follows a **master–transaction architecture**.

Master tables store relatively static reference data, while transaction tables record runtime events and system activity.

---

# Database Architecture

The database contains two categories of tables:

## Master Tables

These tables store reference data that changes infrequently.

* users
* agents

## Transaction Tables

These tables store runtime data generated during system execution.

* tasks
* agent_runs
* results
* logs

Optional monitoring table:

* guardrail_events

---

# Entity Relationship Overview

```
users
   │
   │ 1
   │
   ▼
tasks
   │
   │ 1
   │
   ▼
agent_runs
   │
   │
   ▼
agents

tasks
   │
   ▼
results

tasks
   │
   ▼
logs

tasks
   │
   ▼
guardrail_events
```

---

# Master Tables

## Users Table

Stores information about system users.

### Table: users

| Column     | Type         | Description            |
| ---------- | ------------ | ---------------------- |
| user_id    | Integer (PK) | Unique user identifier |
| name       | String       | User name              |
| email      | String       | User email             |
| role       | String       | User role              |
| created_at | Timestamp    | Account creation time  |

### Purpose

* Identify who submitted tasks
* Support multi-user system usage

---

## Agents Table

Stores metadata about available AI agents.

### Table: agents

| Column      | Type         | Description                     |
| ----------- | ------------ | ------------------------------- |
| agent_id    | Integer (PK) | Unique agent identifier         |
| agent_name  | String       | Name of the AI agent            |
| description | Text         | Agent functionality description |
| version     | String       | Agent version                   |
| is_active   | Boolean      | Agent status                    |
| created_at  | Timestamp    | Registration timestamp          |

### Purpose

* Maintain an agent registry
* Enable agent performance analytics
* Support version tracking

---

# Transaction Tables

## Tasks Table

Represents user requests sent to the AI system.

### Table: tasks

| Column     | Type         | Description              |
| ---------- | ------------ | ------------------------ |
| task_id    | Integer (PK) | Unique task identifier   |
| user_id    | Integer (FK) | Reference to users table |
| query      | Text         | User input query         |
| status     | String       | Task status              |
| created_at | Timestamp    | Task creation time       |

### Purpose

* Track incoming AI tasks
* Link tasks to users

---

## Agent Runs Table

Tracks execution of agents during a task.

### Table: agent_runs

| Column         | Type         | Description               |
| -------------- | ------------ | ------------------------- |
| agent_run_id   | Integer (PK) | Unique execution ID       |
| task_id        | Integer (FK) | Associated task           |
| agent_id       | Integer (FK) | Agent performing the task |
| status         | String       | Execution status          |
| execution_time | Float        | Runtime in seconds        |
| started_at     | Timestamp    | Start time                |
| finished_at    | Timestamp    | End time                  |

### Purpose

* Track agent execution history
* Enable performance analysis
* Monitor failures

---

## Results Table

Stores the final output produced by the system.

### Table: results

| Column           | Type         | Description              |
| ---------------- | ------------ | ------------------------ |
| result_id        | Integer (PK) | Unique result identifier |
| task_id          | Integer (FK) | Associated task          |
| output_text      | Text         | Final generated output   |
| confidence_score | Float        | Confidence metric        |
| created_at       | Timestamp    | Result creation time     |

### Purpose

* Store final AI responses
* Enable result auditing

---

## Logs Table

Stores system logs and execution events.

### Table: logs

| Column    | Type         | Description            |
| --------- | ------------ | ---------------------- |
| log_id    | Integer (PK) | Unique log entry       |
| task_id   | Integer (FK) | Associated task        |
| log_level | String       | INFO / WARNING / ERROR |
| message   | Text         | Log message            |
| timestamp | Timestamp    | Log creation time      |

### Purpose

* System debugging
* Execution traceability
* Observability

---

# Optional Monitoring Table

## Guardrail Events Table

Stores safety and compliance checks performed on AI outputs.

### Table: guardrail_events

| Column         | Type         | Description                 |
| -------------- | ------------ | --------------------------- |
| event_id       | Integer (PK) | Unique event identifier     |
| task_id        | Integer (FK) | Associated task             |
| guardrail_type | String       | Type of guardrail triggered |
| status         | String       | Passed / Failed             |
| message        | Text         | Description of violation    |
| created_at     | Timestamp    | Event timestamp             |

### Purpose

* Track AI safety violations
* Monitor hallucinations
* Detect policy violations

---

# Logging Strategy

The system records logs for all important operations.

Events logged include:

* Task creation
* Agent execution start
* Agent execution completion
* Guardrail checks
* Errors and exceptions
* Fallback activations

Logs are stored in the **logs table**.

---

# Data Flow

The database supports the following workflow:

1. User submits request

```
users → tasks
```

2. System orchestrates agents

```
tasks → agent_runs → agents
```

3. Agents produce result

```
tasks → results
```

4. Execution events recorded

```
tasks → logs
```

5. Guardrail monitoring

```
tasks → guardrail_events
```

---

# Performance Considerations

Indexes should be added for frequently queried fields:

Recommended indexes:

* tasks.user_id
* agent_runs.task_id
* agent_runs.agent_id
* logs.task_id
* results.task_id

This improves query performance for analytics and monitoring.

---

# Scalability Considerations

The schema supports future scaling:

Possible enhancements:

* partition logs table for large datasets
* add model registry table
* add vector database integration
* add analytics tables

---

# Summary

The database architecture provides:

* Clear separation of master and transaction data
* Full traceability of AI agent executions
* Robust logging and observability
* Support for guardrails and safety monitoring

This schema enables the development of a **scalable AI orchestration platform** with full visibility into system behavior.
