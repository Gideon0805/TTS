# XTTS Gradio Demo

This demo showcases voice cloning with the XTTS v2 model using Gradio.
It runs as a standalone script – no packaging is required. Execute
`app.py` directly after installing dependencies.

## Setup

1. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**:
   From the repository root, install the library and demo requirements:
   ```bash
   pip install -e .
   pip install -r TTS/demos/xtts_gradio_demo/requirements.txt
   ```

3. **Run the demo**:
   ```bash
   python TTS/demos/xtts_gradio_demo/app.py
   ```
   The interface will open in your default browser at `http://localhost:7860`.
   Set `DEMO_HOST` or `DEMO_PORT` to change the host or port.

The project now supports Python 3.13 in addition to earlier versions
(`>=3.9, <3.14`). Ensure your virtual environment uses a compatible
version before running the demo.

The first run will download the XTTS model weights and may take a few minutes.
The demo runs on CPU by default and accepts Coqui's terms of service via
`COQUI_TOS_AGREED`.
