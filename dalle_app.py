import gradio as gr
import openai
import os
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore")
load_dotenv() # Load variables from .env file

# Ensure your OpenAI API key is set in your environment variables or a .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    warnings.warn("OPENAI_API_KEY is not set. Please set it in your environment or a .env file.")

"""# Create ChatGPT Dalle prompt"""

def chatgpt_api(input_text):
    messages = [
    {"role": "system", "content": "You are a helpful assistant."}]

    if input_text:
        messages.append(
            {"role": "user", "content": 'Summarize this text "{}" into a short and concise Dall-e2 prompt'.format(input_text)},
        )

        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat_completion.choices[0].message.content
    return reply

"""# Dalle 2 Image generation"""

def dall_e_api(dalle_prompt):
    dalle_response = openai.Image.create(
            prompt = dalle_prompt,
            size="512x512"
        )
    image_url = dalle_response['data'][0]['url']
    return image_url

"""# Speech to text transcription Function"""

def whisper_transcribe(audio):
    os.rename(audio, audio + '.wav')
    audio_file = open(audio + '.wav', "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    dalle_prompt = chatgpt_api(transcript["text"])
    image_url = dall_e_api(dalle_prompt)
    return transcript["text"], image_url

"""# Gradio Interface"""

output_1 = gr.Textbox(label="Speech to Text")
output_2 = gr.Image(label="DALL-E Image")

speech_interface = gr.Interface(fn = whisper_transcribe,
                                inputs=gr.Audio(type="filepath"),
                                outputs = [output_1, output_2],
                                title = "Generate Images using Voice")

speech_interface.launch(debug=True)

