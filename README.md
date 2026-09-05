# AI Research Assistant 🔎🤖

A practical Python application that answers research questions using **externally retrieved information** and the **OpenAI Python SDK**.

This project was built as a hands-on AI engineering exercise to understand the fundamentals of building an LLM application that can retrieve information from an external source, build context, orchestrate multiple components, and generate an answer using an LLM.

The project intentionally keeps the architecture small and focused, avoiding unnecessary abstractions while providing a clean foundation for future AI engineering projects.

## 🏗️ Architecture

```text
User
 │
 ▼
main.py
 │
 ▼
research.py
 │
 ├──────────────► retriever.py
 │                     │
 │                     ▼
 │              Wikipedia API
 │                     │
 │                     ▼
 │               Information
 │
 ▼
Context + Prompts
 │
 ▼
LLMClient
 │
 ▼
OpenAI API
 │
 ▼
LLM Response
```

### Components

* **`main.py`** — Application entry point. Handles user interaction, input validation, dependency creation, error handling, and displaying the final result.

* **`research.py`** — Research workflow and orchestrator. Coordinates information retrieval, context construction, prompts, and the LLM request.

* **`retriever.py`** — Retrieves external information from the Wikipedia API.

* **`llm_client.py`** — Encapsulates communication with the OpenAI API using the OpenAI Python SDK.

* **`config.py`** — Loads and validates the OpenAI API key from environment variables.

* **`tests/`** — Contains automated tests using `pytest` and mocks.

The project deliberately keeps the architecture small. No service layer, vector database, embedding system, agent framework, or complex RAG architecture is included because the current application does not require those abstractions.

## ✨ Features

* External information retrieval using the Wikipedia API
* OpenAI Responses API
* Research workflow orchestration
* Context construction from retrieved information
* System and user prompt construction
* Configurable model selection
* Input validation
* Retrieval failure handling
* OpenAI API error handling
* Connection error handling
* Environment-based API key configuration
* Unit testing with `pytest`
* Mocked external dependencies for testing
* Separation of application responsibilities

## 🛠️ Tech Stack

* **Python**
* **OpenAI Python SDK**
* **Wikipedia API**
* **Requests**
* **python-dotenv**
* **pytest**
* **unittest.mock**

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your system.

Then create a virtual environment if desired:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-Research-Assistant
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

The application reads the API key from `OPENAI_API_KEY`.

**Never commit your real `.env` file or API key to GitHub.**

## ▶️ Running the Application

Run the application from the project root:

```bash
python -m src.research_assistant.main
```

The application prompts you for:

1. Research question
2. Model

Example:

```text
Enter your research question: What is artificial intelligence?
Enter model: gpt-5
```

The application then:

1. Receives the research question.
2. Searches Wikipedia for relevant information.
3. Extracts retrieved information.
4. Builds context containing the question and retrieved information.
5. Sends the context to the OpenAI API.
6. Generates and displays the research answer.

## 🔄 Research Workflow

The core workflow is:

```text
User Question
      ↓
Retriever
      ↓
External Information
      ↓
Context Building
      ↓
LLM Client
      ↓
OpenAI API
      ↓
Research Answer
```

The `research.py` module acts as the **orchestrator**.

Its responsibility is to coordinate the different components rather than implement every operation itself.

## 🧩 Context Building

The application provides the retrieved information to the LLM together with the original question.

The model receives context similar to:

```text
Question:
What is artificial intelligence?

Retrieved information:
Artificial intelligence is ...
```

The system prompt instructs the model to use the retrieved information as evidence.

If the retrieved information is insufficient, the model is instructed to say so rather than inventing an answer.

This demonstrates an important principle of LLM applications:

> **The quality of the answer depends heavily on the quality and relevance of the context provided to the model.**

## 🔎 External Information Retrieval

The retriever uses the Wikipedia API to search for information:

```python
search_information(question)
```

The retriever is responsible only for retrieving information.

It does not:

* Generate answers
* Call the LLM
* Build the research workflow
* Handle application-level orchestration

This separation keeps the component simple and focused.

## 🧪 Testing

The project uses `pytest` for automated testing.

Run the complete test suite:

```bash
python -m pytest
```

Run tests with verbose output:

```bash
python -m pytest -v
```

External dependencies are mocked during unit testing so tests do not require real API requests.

Current tests cover:

* Wikipedia retrieval
* Retriever response handling
* LLM client creation
* LLM response handling
* Request construction
* Research workflow
* Retriever interaction
* LLM client interaction
* Failure conditions

Mocking allows the application's logic to be tested without depending on external services.

## 🛡️ Error Handling

The application validates user input before starting the research workflow.

It handles common failures including:

* Missing API key
* Empty research question
* Empty model name
* No information retrieved
* Authentication errors
* Bad API requests
* OpenAI connection failures
* Other OpenAI API status errors
* External retrieval failures

During development, real external failures were also used as debugging and learning opportunities.

The project follows a simple debugging principle:

```text
Read the error
      ↓
Understand the status code
      ↓
Identify which component failed
      ↓
Find the root cause
      ↓
Fix the problem
      ↓
Test again
```

## 🧠 Failure Analysis

The project intentionally explored failures across different parts of the system.

Examples included:

* Retrieval not performing a real search
* No information being returned
* Poor or insufficient context
* OpenAI authentication failures
* Invalid model identifiers
* External API connection failures
* Wikipedia returning HTTP 403

These failures demonstrated that an AI application is not simply an LLM call.

It is a system containing multiple components and external dependencies, each of which can fail independently.

## 🎯 Engineering Approach

This project follows a practical engineering workflow:

```text
BUILD
  ↓
ENCOUNTER
  ↓
LEARN
  ↓
APPLY
  ↓
BREAK
  ↓
DEBUG
  ↓
TEST
  ↓
REFACTOR
  ↓
REVIEW
```

The objective is not simply to make an LLM produce an answer.

The objective is to understand how multiple components work together and how to build, test, debug, and improve an AI application.

## 🧠 Key Engineering Concepts Practiced

This project provided hands-on practice with:

* External information retrieval
* HTTP APIs
* Context building
* LLM orchestration
* Separation of responsibilities
* Dependency injection
* Classes and objects
* Type annotations
* OpenAI Responses API
* Environment variables
* Configuration validation
* Prompt construction
* Model selection
* Input validation
* Exception handling
* Multiple external dependencies
* Failure isolation
* Unit testing
* Mocking external dependencies
* Debugging API failures
* Root-cause analysis
* Refactoring
* Avoiding premature abstraction

## 📁 Project Structure

```text
AI-Research-Assistant/
│
├── src/
│   └── research_assistant/
│       ├── __init__.py
│       ├── config.py
│       ├── llm_client.py
│       ├── retriever.py
│       ├── research.py
│       └── main.py
│
├── tests/
│   ├── __init__.py
│   ├── test_llm_client.py
│   ├── test_research.py
│   └── test_retriever.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

`.env` is intentionally excluded from the repository because it contains the API key.

## 🔐 Security

API credentials should never be hardcoded in source code or committed to version control.

Use environment variables:

```text
OPENAI_API_KEY=your_api_key_here
```

Make sure `.env` is included in `.gitignore`.

If an API key is accidentally exposed, revoke it and generate a new one immediately.

## 📌 Project Status

**Status: Completed — Phase 1, Project 2**

The project has completed its initial implementation, retrieval workflow, context construction, orchestration, failure analysis, testing, debugging, and final engineering review.

The project successfully demonstrates the fundamentals of building a small AI research application with external information retrieval and LLM orchestration.

## 👨‍💻 Author

**Mohamed Remalli**

Full-Stack Developer & AI Enginner

* GitHub: https://github.com/neelkRemalli



