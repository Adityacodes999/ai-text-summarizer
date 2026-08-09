# 📝 AI Text Summarizer

A simple AI-powered text summarization web app built with **Python, Streamlit, and OpenAI**.

## Features

- Paste long text into a web interface
- Choose concise, bullet-point, or detailed summaries
- Uses an LLM to generate the summary
- Simple and easy-to-understand codebase

## Tech Stack

- Python
- Streamlit
- OpenAI API

## Run locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API key

PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

Optional model:

```powershell
$env:OPENAI_MODEL="gpt-4o-mini"
```

### 3. Start the app

```bash
streamlit run app.py
```

The app will open in your browser.

## Project structure

```text
ai-text-summarizer/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Future improvements

- PDF upload
- DOCX upload
- Summary history
- Authentication
- Deploy to a cloud platform
