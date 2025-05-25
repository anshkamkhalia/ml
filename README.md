# ml-backend-roadmap

my learning journey :)

## **LEVEL 1: Backend Foundations**

### 1. Python Core

- Topics:
    - Syntax & idioms (list comprehensions, unpacking, f‑strings)
    - Data structures (deep dive into dict methods, collections module)
    - OOP: magic methods (**str**, **repr**), class vs instance attributes
    - Exception handling: custom exceptions, try/except/else/finally
    - Virtual environments: venv, pipenv, dependency management
- Project: CLI Study Planner

---

### 2. Git & GitHub

- Topics:
    - Branching strategies (Git Flow vs GitHub Flow)
    - Interactive rebase (git rebase -i) and conflict resolution
    - Stashing, cherry‑picking, bisecting
    - Managing remote repos, forks, upstream syncing
- Project: Python Projects Repo

---

### 3. Testing & Quality

- Topics:
    - pytest fixtures, parametrization
    - Mocking external calls with unittest.mock or pytest-mock
    - Linting: setting up flake8/pylint, pre‑commit hooks
    - Type hints and mypy for static analysis
- Project: Expense Tracker Test Suite

---

## 🎮 **LEVEL 2: APIs & Databases**

### 4. Flask Basics

- Topics:
    - Application factory pattern
    - Blueprints for modular apps
    - WTForms: custom validators, CSRF protection
- Project: Contact Form API

---

### 5. Databases & ORM

- Topics:
    - Advanced SQL (window functions, CTEs)
    - SQLAlchemy relationships: one‑to‑many, many‑to‑many
    - Eager vs lazy loading, query performance
    - Alembic: writing migration scripts, branching histories
- Project: Categorized Note API

---

### 6. FastAPI & Async

- Topics:
    - Python asyncio basics (event loop, tasks)
    - Pydantic models: Field validators, nested models
    - Dependency injection patterns
    - Background tasks vs Celery for long jobs
- Project: Async Sentiment Service

---

### 7. Auth & Security

- Topics:
    - JWT payload design, refresh tokens
    - Secure cookie vs Authorization header
    - OAuth2 flows (authorization code, client credentials)
    - OWASP Top 10 (SQLi, XSS, CSRF) mitigation
- Project: Secure Blog Backend

---

### 8. Deployment & CI/CD

- Topics:
    - Docker multi‑stage builds, caching layers
    - Gunicorn workers, async vs sync workers
    - Nginx reverse proxy, TLS termination
    - Writing GitHub Actions workflows (lint, test, build, deploy)
- Project: Deployed Note API

---

### 🧱 **Django Essentials** *(NEW SECTION)*

- Topics:
    - Django project vs app structure
    - URL routing & views (function-based vs class-based)
    - Django ORM queries and model relationships
    - Built-in auth system, forms, and sessions
    - Middleware & custom admin customization
- Project: Django Blog CMS

---

## 🚀 **LEVEL 3: AI & ML Integration**

### 1. Scikit‑Learn Foundations

- Topics:
    - Data preprocessing (scaling, encoding, imputing)
    - Model pipelines, grid/random search
    - Cross‑validation strategies (k‑fold, stratified)
- Project: House Price Predictor

---

### 2. Neural Network Concepts

- Topics:
    - Activation functions + their gradients
    - Backpropagation step‑by‑step
    - Loss landscapes and vanishing/exploding gradients
- Project: MNIST Classifier from Scratch

---

### 3. Deep Learning with TensorFlow

- Topics:
    - Keras Functional vs Sequential API
    - Callbacks (EarlyStopping, ModelCheckpoint)
    - Data augmentation pipelines
- Project: CNN on CIFAR‑10

---

### 4. TensorFlow Projects

- Topics:
    - Transfer learning best practices
    - Fine‑tuning vs feature extraction
    - TensorBoard for metrics and profiling
- Project: Transfer Learning Classifier

---

### 5. PyTorch Basics

- Topics:
    - Tensor operations vs NumPy
    - Custom Dataset/DataLoader classes
    - Autograd internals
- Project: PyTorch Feedforward Net

---

### 6. PyTorch Projects

- Topics:
    - Using torchvision models and transforms
    - Freezing layers and adjusting learning rates
    - Saving/loading checkpoints
- Project: Neural Style Transfer

---

### 7. Advanced Capstones

- Topics:
    - GAN training stability (WGAN, gradient penalty)
    - Policy gradients vs Q‑learning basics
    - Text tokenization (BPE, WordPiece)
- Project: GAN‑Based Image Generator

---

### 9. OpenAI / Gemini API

- Topics:
    - Rate limit handling, retry/backoff
    - Secure key rotation
    - Parsing streaming JSON chunks
- Project: Ask‑AI Service

---

### 10. Prompt Engineering

- Topics:
    - Prompt templates as code (Jinja2 or f‑strings)
    - Auto‑prompt generation from examples
    - Evaluating prompt robustness
- Project: AI Quiz Maker

---

### 11. LangChain Essentials

- Topics:
    - Custom tool wrappers
    - Memory serialization and expiry
    - Agent orchestration flows
- Project: Chat with PDF API

---

### 12. Vector Databases

- Topics:
    - Embedding normalization, indexing strategies
    - ANN algorithms (HNSW, IVF)
    - Scaling vector stores
- Project: Semantic Search API

---

### 13. Streaming Responses

- Topics:
    - Chunked transfer encoding
    - Frontend SSE/Fetch handlers
    - Reconnecting and backpressure
- Project: Live AI Typing Service

---

## 🛡️ **LEVEL 4: Production‑Grade AI**

### 14. Model Serving & Custom ML

- Topics:
    - Flask vs FastAPI for model serving
    - Batch prediction pipelines
    - A/B testing models in production
- Project: Expense Categorizer API

---

### 15. DevOps for AI

- Topics:
    - Kubernetes Deployments & Services
    - Model monitoring (latency, accuracy drift)
    - Canary rollouts
- Project: Monitored Deploy of Categorizer

---

## 🎮 **LEVEL 5: AI Agent Architectures & Capstones**

### 16. Agent Design & Plugins

- Topics:
    - Tool schema definitions
    - Agent self‑evaluation loops
    - Long‑term memory strategies
- Project: Personal AI Butler

---

### 17. Multi‑Modal Models

- Topics:
    - Vision + text joint embeddings
    - OCR preprocessing pipelines
    - VQA chain setup
- Project: Vision‑Enabled Tutor

---

### 18. Final Capstone

- Steps: define → select → train → eval → deploy
- Topics:
    - End‑to‑end ML pipeline architecture
    - Feature stores & data versioning
    - Scalable inference (serverless, GPU autoscaling)
- Project: Build & Deploy Your Own AI Model
