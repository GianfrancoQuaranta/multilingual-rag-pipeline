# 🔍 Multilingual RAG Pipeline — SOLID, Cached, and Production-Ready

## 🌍 Overview (English)

### 🎯 Project Objectives

- Build a local API using FastAPI or Flask that accepts user questions and returns consistent LLM responses.
- Automatically detect language (ES, EN, PT), translate if necessary, and generate multilingual responses.
- Store and retrieve chunks from a vector database (ChromaDB).
- Build prompts that are deterministic, emoji-rich, one-sentence, and in third person.
- Follow SOLID principles and best practices.
- Include validation rules and cache system.
- Pass all tests using Pytest.

This project is a fully modular, production-grade **RAG (Retrieval-Augmented Generation)** system, designed with multilingual capabilities in **Spanish**, **English**, and **Portuguese**. It leverages powerful APIs like **Cohere** and **DeepL** and is implemented following **SOLID principles** and best practices for clean, maintainable, and testable code.

### 🚀 Features

- ✅ Multilingual support (ES, EN, PT)
- ✅ Cohere embeddings and language model
- ✅ DeepL-based language detection and translation
- ✅ JSON-based persistent caching system
- ✅ Custom prompt builder with context awareness and validation rules
- ✅ Fully modular design using Protocols, Interfaces, and Adapters
- ✅ FastAPI web interface
- ✅ Async-ready RAG pipeline
- ✅ Modular and integration tests with Pytest

### 🧠 What is RAG?

RAG combines the power of **retrieval systems** (like vector databases) with **generative language models**. Instead of generating responses based on a static knowledge base, this pipeline retrieves relevant information dynamically and uses that context to generate accurate, up-to-date answers.

### 🧱 Technologies Used

- Python 3.11+
- FastAPI
- Cohere API ([Sign up here](https://dashboard.cohere.com/api-keys))
- DeepL API ([Sign up here](https://www.deepl.com/pro))
- ChromaDB for vector storage
- Pytest for testing
- Pydantic for request/response validation

### 💡 SOLID Principles

This project adheres strictly to the **SOLID principles** of software engineering:

- **S**ingle Responsibility
- **O**pen/Closed Principle
- **L**iskov Substitution
- **I**nterface Segregation
- **D**ependency Inversion

All components are modular, extensible, and easily testable.

### 🧰 How to Run the Project

1. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Set up your environment variables**:

    Create a `.env` file from the example provided:

    ```bash
    cp .env.example .env
    ```

    Then, add your API keys:

    - `COHERE_API_KEY`: Get it [here](https://dashboard.cohere.com/api-keys)
    - `DEEPL_API_KEY`: Get it [here](https://www.deepl.com/pro)

3. **Start the server**:

    From the root of the project, run:

    ```bash
    uvicorn app.app:app --reload
    ```

4. **Run the tests**:

    ```bash
    pytest -s tests/test_rag_responses.py
    ```

### 🔄 API Testing with Postman

A Postman Collection file is included:

- `rag_questions_postman_collection.json`

To use it:

1. Open Postman.
2. Click **Import** and upload the file.
3. Use the **Runner** to test all questions in sequence.
4. You’ll get real-time feedback from your local API.

### 🧠 Core Components

- **Cache System**: Uses JSON files to persist translated questions, contexts, and prompts.
- **Translation Pipeline**: Automatically detects and translates input into the embedding language.
- **Validation Rules**: Enforce response structure (e.g., emojis, one sentence, language).
- **Prompt Generation**: Dynamic prompt building with language-aware formatting.
- **Test Suite**: Ensures deterministic responses and verifies language integrity.

---

## 🌍 Descripción General (Español)

### 🎯 Objetivos del Proyecto

- Desarrollar una API local con FastAPI o Flask para responder preguntas de usuario.
- Detectar el idioma automáticamente (ES, EN, PT) y traducir si es necesario.
- Usar ChromaDB para almacenar y recuperar chunks vectorizados.
- Generar prompts que sean deterministas, con emojis, en tercera persona y de una sola oración.
- Seguir principios SOLID y buenas prácticas.
- Incluir validaciones y sistema de cacheo.
- Pasar todos los tests usando Pytest.

Este proyecto es un sistema **RAG (Generación Aumentada por Recuperación)** completamente modular y preparado para producción, con soporte multilingüe en **español**, **inglés** y **portugués**. Está diseñado con principios **SOLID** y buenas prácticas de programación y documentación.

### 🚀 Características

- ✅ Soporte multilingüe (ES, EN, PT)
- ✅ Embeddings y modelo de lenguaje de Cohere
- ✅ Detección de idioma y traducción con DeepL
- ✅ Sistema de cacheo persistente basado en JSON
- ✅ Generador de prompts inteligente y reglas de validación
- ✅ Arquitectura modular con Interfaces y Protocolos
- ✅ API construida con FastAPI
- ✅ Pipeline asincrónico RAG
- ✅ Tests modulares y de integración con Pytest

### 🧠 ¿Qué es RAG?

RAG combina sistemas de **recuperación de información** (vector stores) con modelos de lenguaje generativos. En lugar de responder desde una base fija, recupera contexto relevante en tiempo real y genera respuestas precisas y actualizadas.

### 🧱 Tecnologías utilizadas

- Python 3.11+
- FastAPI
- API de Cohere ([Crear cuenta](https://dashboard.cohere.com/api-keys))
- API de DeepL ([Crear cuenta](https://www.deepl.com/pro))
- ChromaDB como base de vectores
- Pytest para pruebas
- Pydantic para validación

### 💡 Principios SOLID

El diseño respeta los **principios SOLID**:

- **S**ingle Responsibility (Responsabilidad única)
- **O**pen/Closed (Abierto/Cerrado)
- **L**iskov Substitution (Sustitución de Liskov)
- **I**nterface Segregation (Segregación de Interfaces)
- **D**ependency Inversion (Inversión de Dependencias)

Cada componente es extensible, aislado y fácilmente testeable.

### 🧰 Cómo iniciar el proyecto

1. **Instalar dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Configurar variables de entorno**:

    Crear el archivo `.env` desde el ejemplo:

    ```bash
    cp .env.example .env
    ```

    Luego, agregar tus claves:

    - `COHERE_API_KEY`: [Obtener aquí](https://dashboard.cohere.com/api-keys)
    - `DEEPL_API_KEY`: [Obtener aquí](https://www.deepl.com/pro)

3. **Iniciar el servidor**:

    Desde la raíz del proyecto:

    ```bash
    uvicorn app.app:app --reload
    ```

4. **Ejecutar los tests**:

    ```bash
    pytest -s tests/test_rag_responses.py
    ```

### 🔄 Pruebas de API con Postman

Se adjunta el archivo:

- `rag_questions_postman_collection.json`

Pasos para utilizarlo:

1. Abrí Postman.
2. Hacé clic en **Importar** y subí el archivo `.json`.
3. Usá el **Runner** para ejecutar todas las preguntas en secuencia.
4. Vas a obtener las respuestas en tiempo real desde la API local.

### 🧠 Componentes clave

- **Sistema de Caché**: Guarda en JSON traducciones, contextos y prompts generados.
- **Pipeline de Traducción**: Detecta y traduce entradas al idioma base de embeddings.
- **Reglas de Validación**: Verifican formato, uso de emojis, estructura y consistencia de idioma.
- **Generación de Prompts**: Construcción dinámica según idioma y contexto.
- **Suite de Tests**: Asegura consistencia y validez de respuestas.
