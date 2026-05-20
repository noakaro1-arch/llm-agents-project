# Multi-Agent Translation Chain & Semantic Analysis

A Python-based workflow that demonstrates translation chaining using the Gemini CLI and custom Skills. The system translates an English sentence through a multi-language path (English -> French -> Hebrew -> English) and then performs a semantic comparison to analyze meaning drift and translation quality.

## Project Overview

This project implements a "Level 3" AI agent workflow where a single orchestrator utilizes multiple specialized Skills to perform a complex, multi-step task. By routing a sentence through several languages and back, it tests the robustness of the LLM's translation capabilities and provides a quantitative/qualitative analysis of the final result versus the original input.

## Architecture

The project is structured as follows:

- **Orchestrator (`src/main.py`)**: A Python script that manages the user interaction, progress tracking, and the execution of Gemini CLI commands.
- **Skills (`.gemini/skills/`)**: Modular instruction sets that define the behavior for each translation step and the final comparison.
- **Gemini CLI**: The underlying engine used to execute the prompts and interact with Vertex AI models.
- **Rich Terminal UI**: Used for professional, formatted output in the command line.

## Translation Flow

1.  **English to French**: The original English input is translated into natural French.
2.  **French to Hebrew**: The French text is translated into modern Hebrew.
3.  **Hebrew back to English**: The Hebrew text is translated back into English.
4.  **Semantic Comparison**: The original and final English sentences are compared to measure similarity and identify any meaning drift.

## Skills Used

- **`english_to_french`**: Expert translator specializing in natural French preservation.
- **`french_to_hebrew`**: Expert translator focused on modern Hebrew fluency.
- **`hebrew_to_english`**: Expert translator returning the text to its original language.
- **`comparison`**: Semantic analysis system that scores similarity (0-100) and explains meaning shifts.

## Installation

### Prerequisites

- **Python 3.10+**
- **Gemini CLI**: Installed and authenticated with Vertex AI.
- **Google Cloud Project**: With Vertex AI API enabled.

### Steps

1.  Clone the repository:
    ```bash
    git clone [repository-url]
    cd llm-agents-project
    ```

2.  Install Python dependencies:
    ```bash
    pip install rich
    ```

## Usage

Run the orchestrator from the project root:

```bash
python src/main.py
```

Follow the prompt to enter an English sentence. The system will display progress bars for each translation step and then show a table of results.

## Example Output

**Input:**
`"One for all and all for one"`

**Translation Chain Results:**
| Stage         | Text                                  |
| :------------ | :------------------------------------ |
| Original      | One for all and all for one           |
| French        | Un pour tous et tous pour un          |
| Hebrew        | אחד בשביל כולם וכולם בשביל אחד      |
| Final English | One for all and all for one           |

**Semantic Comparison Analysis:**
- **Similarity Score:** 100/100
- **Meaning Drift:** None. The core idiomatic expression was perfectly preserved through the translation chain.
- **Analysis:**
    - The idiomatic nature of the phrase was recognized and correctly handled in all languages.
    - Factual and intent consistency is perfect.

## Technologies

- **Python**: Scripting and orchestration.
- **Gemini CLI**: LLM interaction and prompt execution.
- **Vertex AI**: Underlying Generative AI models.
- **Rich**: Terminal formatting and progress visualization.
- **Markdown**: Skill definition and documentation.
