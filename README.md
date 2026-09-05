# LIC Management System

A full-stack insurance management platform built with **React, FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and Google Gemini AI**. The system provides customer and policy management, authentication, analytics dashboards, and an AI-powered insurance assistant that generates context-aware responses using customer and policy information.

---

##  Project Overview

The **LIC Management System** is a client-server web application designed to manage insurance customers and their policies through a centralized digital platform.

The project combines a modern React frontend with a Python FastAPI backend and PostgreSQL database. It also integrates **Google Gemini** to provide an AI-powered insurance assistant capable of answering questions using relevant customer and policy information as context.

The project demonstrates practical implementation of **full-stack development, REST APIs, relational databases, authentication, data analytics, and Generative AI integration**.

---

## Key Features

### Customer Management

- Customer registration and login
- Customer profile management
- Search customers by name
- Search customers by mobile number
- View customer information
- View policies associated with a customer

### Policy Management

- Store and manage insurance policy information
- View customer-specific policies
- Search policies by policy type
- View premium information
- Track policy commencement dates
- Track premium-paying periods
- Track policy maturity dates
- Maintain customer-policy relationships

### Authentication & Security

- Customer registration and login
- Password hashing
- JWT-based authentication
- Protected API endpoints
- Environment variables for sensitive credentials
- `.gitignore` protection for API keys and environment files

### Analytics Dashboard

The admin dashboard provides useful insights into the insurance dataset, including:

- Total customers
- Policy statistics
- Policy type distribution
- Gender distribution
- Average customer age
- Highest premium
- Lowest premium

### AI-Powered Insurance Assistant

The system integrates **Google Gemini AI** to provide an intelligent insurance assistant.

Customer and policy information is passed as contextual information to the Gemini model so that the assistant can generate relevant responses to insurance-related questions.

Example questions:

- "What policies do I currently have?"
- "What is my premium amount?"
- "When does my policy mature?"
- "Show me my policy details."

### Current AI Architecture

The current implementation uses:

- Google Gemini API
- Context-aware prompt construction
- Customer and policy information as context
- FastAPI AI endpoint
- Generative AI response generation

> **Note:** The current implementation is context-aware Generative AI. A complete document-based RAG pipeline is planned as a future enhancement.

---

## System Architecture

```text
                         ┌──────────────────────┐
                         │        User          │
                         │   Customer / Admin   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   React Frontend     │
                         │       + Vite         │
                         └──────────┬───────────┘
                                    │
                              HTTP / REST API
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   FastAPI Backend    │
                         │                      │
                         │ Authentication       │
                         │ Customer APIs        │
                         │ Policy APIs           │
                         │ Analytics APIs       │
                         │ AI Endpoint          │
                         └─────────┬────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                    ▼                             ▼
          ┌──────────────────┐          ┌──────────────────┐
          │   PostgreSQL     │          │   Google Gemini  │
          │    Database      │          │   AI Assistant   │
          └──────────────────┘          └──────────────────┘
