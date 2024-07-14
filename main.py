import torch
from TTS.api import TTS
import gradio as gr

device = "cuda" if torch.cuda.is_available() else "cpu"

def generate_audio(text = "I NTRODUCTION A crucial element of multilingual voice recognition systems is language identification, which is the process of automatically identifying the language spoken in an utterance. Choosing the right acoustic and linguistic models for transcription depends on accurate language identifica-tion. However, it is extremely difficult to develop trustworthy language recognition algorithms for low-resource languages like Bengali due to a lack of training data and the possibility of confusion with closely similar languages. An extensive resource on the languages of the globe,Ethnologue[1], estimates that there will be over 228 million Bengali speakers worldwide in 2022."):
    tts = TTS(model_name='tts_models/en/ljspeech/fast_pitch').to(device)
    tts.tts_to_file(text=text, file_path="outputs/output.wav")
    return "outputs/output.wav"

# print(generate_audio())

demo = gr.Interface(
    fn=generate_audio,
    inputs=[gr.Text(label="text"),],
    outputs=[gr.Audio(label="Audio"),],
)
demo.launch(share=True)




















# import torch
# from TTS.api import TTS
# import gradio as gr
# import easyocr
# import fitz  # PyMuPDF

# device = "cuda" if torch.cuda.is_available() else "cpu"

# def read_pdf(file_path):
#     reader = easyocr.Reader(['en'])  # Initialize the OCR reader
#     text = ""
#     pdf_document = fitz.open(file_path)  # Open the PDF document with PyMuPDF
    
#     for page_num in range(len(pdf_document)):
#         page = pdf_document.load_page(page_num)  # Load each page
#         pix = page.get_pixmap()  # Render the page to an image
#         img_path = f"page_{page_num}.png"
#         pix.save(img_path)  # Save the image of the page
#         result = reader.readtext(img_path)  # Perform OCR on the image
#         page_text = " ".join([res[1] for res in result])  # Extract the text
#         text += page_text + "\n"  # Accumulate the text from each page
    
#     return text

# def generate_audio(text):
#     tts = TTS(model_name='tts_models/en/ljspeech/fast_pitch').to(device)
#     tts.tts_to_file(text=text, file_path="outputs/output.wav")
#     return "outputs/output.wav"

# def pdf_to_audio(pdf_file):
#     text = read_pdf(pdf_file.name)
#     return generate_audio(text)

# demo = gr.Interface(
#     fn=pdf_to_audio,
#     inputs=[gr.File(label="Upload PDF")],
#     outputs=[gr.Audio(label="Audio")],
# )

# demo.launch(share=True)
