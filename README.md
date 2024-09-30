Here's the README with GitHub-style headings using `#`:

---

# OCR and Document Search Web Application

## Objective
This project is a web-based prototype that demonstrates the ability to perform **Optical Character Recognition (OCR)** on an uploaded image containing text in both **Hindi and English**. The application also provides a basic **keyword search** functionality on the extracted text.

## Features
- Extracts text from images (JPEG, PNG, etc.) containing both Hindi and English.
- Simple, user-friendly web interface for image uploads using **Gradio**.
- Provides keyword search functionality within the extracted text.
- Highlights the searched keywords in the extracted text.
- Deployed on **Hugging Face Spaces** with a live URL.

## Installation
1. Clone the repository:
    ```bash
    git clone https://huggingface.co/spaces/your-username/ocr-document-search-app
    ```

2. Navigate to the project directory:
    ```bash
    cd ocr-document-search-app
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application locally:
    ```bash
    python app.py
    ```

2. Open the app in your browser and upload an image containing Hindi and English text.

3. Perform a search by entering keywords and see them highlighted in the extracted text.

## Deployment
The app is deployed on **Hugging Face Spaces**. You can view and use it via the live URL:
[https://huggingface.co/spaces/your-username/ocr-document-search-app](https://huggingface.co/spaces/your-username/ocr-document-search-app)

## Dependencies
Add any necessary dependencies in:
- `requirements.txt` for Python libraries.
- `packages.txt` for Debian packages if required.

## Thought Process Behind the Implementation
1. **OCR Implementation**: I chose the `pytesseract` OCR engine for its ability to extract mixed-language text (Hindi and English). It allows for easy integration and works well for most image formats.
  
2. **Web Interface**: The application uses **Gradio** for a simple interface that supports image uploads, displays extracted text, and facilitates keyword searches.

3. **Deployment**: The application is deployed on **Hugging Face Spaces**, which offers seamless integration for running Gradio applications.
