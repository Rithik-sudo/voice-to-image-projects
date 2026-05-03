# Voice to Image Projects

This repository contains two approaches for generating images from voice transcripts:

1. **DALL-E Cloud API Approach** (`dalle_app.py`)
2. **Local Open-Source Approach** (`stable_diffusion_local.ipynb`)

---

## 1. DALL-E Cloud API Approach (`dalle_app.py`)

This application uses the OpenAI Cloud APIs to perform speech-to-text transcription (via Whisper), prompt translation (via ChatGPT-3.5), and image generation (via DALL-E 2). It hosts a web interface using **Gradio**.

### Requirements
- An OpenAI API Key (`sk-...`)

### Installation & Execution (via `uv`)
We manage dependencies using `uv`. Make sure you have `uv` installed.

1. **Set up your environment variables:** 
   Copy the provided `.env.example` to `.env` and insert your OpenAI API key.
   ```bash
   cp .env.example .env
   # Edit .env and supply your OPENAI_API_KEY
   ```

2. **Run the application:**
   Using `uv`, everything will be handled locally and extremely fast!
   ```bash
   uv run python dalle_app.py
   ```
   *This automatically creates the virtual environment and starts the Graido web application on `http://127.0.0.1:7860`.*

---

## 2. Local Open-Source Approach (`stable_diffusion_local.ipynb`)

This is a Jupyter Notebook demonstrating an entirely local inference pipeline using **Hugging Face** models.
- **Voice-to-Text**: `openai/whisper-large-v3` (Runs locally via `transformers`)
- **Text-to-Image**: `stabilityai/stable-diffusion-xl-base-1.0` (Runs locally via `diffusers`)

This approach requires no paid APIs, but significantly greater local compute power (a discrete GPU is highly recommended).

### Installation & Execution (via `uv`)
Because we are using `uv`, you can spin up the environment with `jupyter` installed.

1. **Sync dependencies and start Jupyter:**
   ```bash
   uv run jupyter notebook
   ```
2. Open `stable_diffusion_local.ipynb` in your browser.
3. Once running, ensure that `CUDA` is available if you plan to generate text and images swiftly.

---
## Project Dependencies

The list of dependencies are structured inside the newly created `pyproject.toml` file tracked by `uv`. The main commands are standard machine learning and API routing libraries:
- `gradio`, `openai==0.28`, `python-dotenv` (for the API script)
- `diffusers`, `transformers`, `accelerate`, `jupyter`, `torch` (for the localized ML notebook).
