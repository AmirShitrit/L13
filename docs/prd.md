# Product Requirements Document: Command-Line AI Agent

## 1. Introduction

This document outlines the requirements for a command-line AI agent. The agent will be able to understand free-text input from a user, and based on that input, execute predefined Python functions as "tools". This allows for the extension of a Large Language Model's (LLM) capabilities by giving it access to local functions.

## 2. Goals

*   To create an AI agent that can be interacted with via a command-line interface.
*   To allow the agent to execute Python functions (tools) based on user input.
*   To ensure that sensitive information, such as API keys, are not exposed in the codebase.

## 3. User Stories

*   As a user, I want to be able to type a command in my terminal and have an AI agent execute a task for me.
*   As a developer, I want to be able to easily define new Python functions that the AI agent can use as tools.
*   As a security-conscious developer, I want to make sure that the agent's API key is kept secret.

## 4. Requirements

### 4.1. Functional Requirements

*   The system shall provide a command-line interface (CLI) for users to interact with the agent.
*   The agent shall accept free-text input from the user.
*   The agent will be composed of an LLM and a set of Python functions (tools).
*   The agent shall be able to determine which tool to use based on the user's input.
*   The agent shall be able to pass arguments to the tools based on the user's input.
*   The system shall execute the selected tool and return the output to the user.
*   There will be at least two distinct Python functions that can be used as tools.

### 4.2. Non-Functional Requirements

*   **Security:** The API key for the LLM must not be hardcoded in the source code. It must be loaded from a secure source, such as an environment variable or a configuration file that is not checked into version control.

### 4.3. Environment Requirements

*   The agent must be executed within a `uv` virtual environment to ensure dependency isolation and reproducibility.