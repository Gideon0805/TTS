import os
import gradio as gr
from TTS.api import TTS

# Accept Coqui terms for demo usage
os.environ["COQUI_TOS_AGREED"] = "1"

MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"

# Optional host/port configuration for the local web UI
HOST = os.environ.get("DEMO_HOST", "127.0.0.1")
PORT = int(os.environ.get("DEMO_PORT", "7860"))

# Initialize TTS model on CPU
tts = TTS(MODEL_NAME, gpu=False)

def predict(prompt: str, language: str, reference_audio: str):
    """Generate audio using a reference voice sample."""
    if not prompt.strip():
        return None, None

    tts.tts_to_file(
        text=prompt,
        file_path="output.wav",
        speaker_wav=reference_audio,
        language=language,
    )

    return gr.make_waveform("output.wav"), "output.wav"


def main():
    demo = gr.Interface(
        fn=predict,
        inputs=[
            gr.Textbox(label="Text Prompt"),
            gr.Dropdown(
                label="Language",
                choices=["en", "es", "fr", "de", "it", "pt", "pl", "tr", "ru", "nl", "cs", "zh-cn"],
                value="en",
            ),
            gr.Audio(label="Reference Audio", type="filepath"),
        ],
        outputs=[
            gr.Video(label="Waveform Visual"),
            gr.Audio(label="Synthesised Audio"),
        ],
        title="XTTS Voice Cloning",
        description="Minimal XTTS voice cloning demo using Gradio.",
    )
    demo.queue().launch(
        server_name=HOST,
        server_port=PORT,
        share=False,
        inbrowser=True,
    )


if __name__ == "__main__":
    main()
