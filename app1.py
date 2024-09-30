import pytesseract
from PIL import Image
import gradio as gr

# If necessary, set the path to Tesseract executable (for Windows users)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path, lang='eng+hin'):
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Extract text with multiple languages (e.g., 'eng+hin' for English + Hindi)
        text = pytesseract.image_to_string(img, lang=lang)
        
        return text
    except Exception as e:
        return f"Failed to extract text: {str(e)}"

def highlight_keyword(text, keyword):
    """Highlight the keyword in the text by coloring it using HTML."""
    if not keyword:
        return text  # No keyword, just return the original text
    
    # Use case-insensitive keyword matching and coloring
    highlighted_text = text.replace(keyword, f"<span style='color: red; font-weight: bold;'>{keyword}</span>")  # Color the keyword red
    return highlighted_text

def ocr_and_search(image, keyword):
    extracted_text = ""
    search_result = ""
    
    try:
        # Extract both English and Hindi text
        extracted_text = extract_text(image, lang='eng+hin')
        print(f"Extracted Text: {extracted_text}")  # Debugging output
    except Exception as e:
        return "Error extracting text. Please check the uploaded image.", str(e)

    if not keyword or not keyword.strip():  # Check for empty keyword
        return extracted_text, "Please enter a valid keyword."

    # Check if the keyword exists in the extracted text
    if keyword.lower() in extracted_text.lower():
        search_result = "Keyword found!"
        # Highlight the keyword in the extracted text by coloring it
        highlighted_text = highlight_keyword(extracted_text, keyword)
    else:
        search_result = "Keyword not found."
        highlighted_text = extracted_text  # Return without highlight if not found

    return highlighted_text, search_result

# Gradio Interface
def gradio_app(image, keyword):
    extracted_text, search_result = ocr_and_search(image, keyword)
    return extracted_text, search_result

# Create Gradio interface
interface = gr.Interface(
    fn=gradio_app,
    inputs=[
        gr.Image(type="filepath", label="Upload Image"),
        gr.Textbox(label="Enter Keyword")
    ],
    outputs=[
        gr.HTML(label="Extracted Text"),  # Use HTML output to allow keyword coloring
        gr.Textbox(label="Search Result")
    ],
    title="OCR (English + Hindi) and Keyword Search",
    description="Upload an image with both English and Hindi text, and search for a keyword. The keyword will be highlighted and colored if found."
)

# Launch the interface
interface.launch()
