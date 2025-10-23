# Command-Line AI Agent for Tool Testing

## Overview

This project is a command-line AI agent designed to help developers test and validate Python functions (referred to as "tools"). The agent uses a Large Language Model (LLM) to understand user input, execute the corresponding tool, and then gather feedback on the tool's performance. All feedback is saved to `feedback.md` for later review.

## Getting Started

### Prerequisites

Make sure you have `uv` installed. You can find installation instructions [here](https://github.com/astral-sh/uv).

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Initialize the submodule:**
    ```bash
    git submodule update --init --recursive
    ```

3.  **Create and activate the virtual environment:**
    ```bash
    uv venv
    source .venv/bin/activate
    ```

4.  **Install dependencies:**
    ```bash
    uv pip install -e .
    ```

5.  **Set up your API Key:**
    The agent requires an API key for the LLM. Export it as an environment variable:
    ```bash
    export LLM_API_KEY='your-api-key-here'
    ```

## Usage

Run the agent by executing the `tests.py` script with `uv run`. Provide a free-text prompt describing the tool you want to test.

```bash
uv run tests.py "test the convolution tool with start point 1 and end point 2"
```

After the tool executes, you will be prompted to provide feedback on its performance.

### Example Run

```
$ uv run tests.py "test the convolution tool with start point 1 and end point 2"
Running tool: Convolution Tool
Tool output:
  - signal_and_matches.png (76KB)
  - convolution_result.png (70KB)
  - Convolution Result: Array of correlation values ranging from ~2.35 to ~26.12

Please provide your feedback on this tool execution (type 'exit' to finish):
> Overall Quality Rating: Excellent - Works perfectly as expected
> The tool executed correctly, generated accurate visualizations, and the pattern matching worked well. The convolution algorithm successfully identified all matching patterns in the sine wave signal.
> Areas for Improvement: Documentation clarity: README or usage instructions could be clearer or more detailed
> Observations: The tool successfully generated a sine wave signal over 10 cycles (200 samples per cycle). Pattern extraction from radians 1 to 2 worked correctly. Normalized cross-correlation identified 10 matching peaks (one per cycle) with high accuracy. Visualization clearly shows the original signal (blue), the selected pattern (orange), and matched patterns (red dashed). The convolution result plot shows periodic peaks corresponding to pattern matches. All dependencies (numpy, matplotlib, scipy) were installed successfully via uv.
> Technical Details: Environment: uv virtual environment, Python Version: 3.10.12, Key Dependencies: numpy 2.2.6, matplotlib 3.10.7, scipy 1.15.3, Execution Time: < 10 seconds (including dependency resolution).
> exit
Feedback saved to feedback.md
```

## Feedback

All feedback is collected and appended to the `feedback.md` file in the root of the project. This file contains a log of all tool executions and the feedback provided for each one. An example of the `feedback.md` content is shown below:

```markdown
# Tool Testing Feedback

## Convolution Tool

**Timestamp:** 2025-10-23 19:51:41

**Test Parameters:**
- Tool: Convolution (1D Signal Simulation and Convolution Analysis)
- Command: `python main.py --start_point 1 --end_point 2`
- Test Range: 1 to 2 radians

**Execution Results:**
- Status: Success
- Output Files Generated:
  - signal_and_matches.png (76KB)
  - convolution_result.png (70KB)
- Convolution Result: Array of correlation values ranging from ~2.35 to ~26.12

**User Feedback:**

**Overall Quality Rating:** Excellent - Works perfectly as expected

The tool executed correctly, generated accurate visualizations, and the pattern matching worked well. The convolution algorithm successfully identified all matching patterns in the sine wave signal.

**Areas for Improvement:**
- Documentation clarity: README or usage instructions could be clearer or more detailed

**Observations:**
1. The tool successfully generated a sine wave signal over 10 cycles (200 samples per cycle)
2. Pattern extraction from radians 1 to 2 worked correctly
3. Normalized cross-correlation identified 10 matching peaks (one per cycle) with high accuracy
4. Visualization clearly shows the original signal (blue), the selected pattern (orange), and matched patterns (red dashed)
5. The convolution result plot shows periodic peaks corresponding to pattern matches
6. All dependencies (numpy, matplotlib, scipy) were installed successfully via uv

**Technical Details:**
- Environment: uv virtual environment
- Python Version: 3.10.12
- Key Dependencies: numpy 2.2.6, matplotlib 3.10.7, scipy 1.15.3
- Execution Time: < 10 seconds (including dependency resolution)

---
```
