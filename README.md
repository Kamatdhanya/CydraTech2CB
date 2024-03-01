```markdown
# CydraTech2CB
## Assignment 2: Chatty Document Chatbot

This project implements an AI chatbot that allows users to have a conversation with an uploaded PDF document. The chatbot extracts information from the uploaded PDF and responds to questions asked by the user.

## Tech Stack

- Langchain: Provides the text understanding and generation capabilities.
- FastAPI: Powers the API backend for seamless communication.
- Frontend: Implemented using HTML, CSS, and JavaScript.

## Features

- Upload a PDF: Users can upload a PDF document of their choice.
- Ask Questions: Users can ask questions based on the content of the uploaded PDF.
- Real-time Chat: Engage in real-time conversation with the chatbot.

## How to Run

1. Clone the repository:

```bash
git clone <repository_url>
cd <project_directory>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the API key:

- Open the `backend/main.py` file.
- Locate the `API_KEY` variable and replace `"YOUR_API_KEY"` with your actual API key.

4. Run the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

5. Open your web browser and go to `http://localhost:8000` to access the application.
   - You should see a page prompting you to enter your API key. Enter the API key and click "Submit".
   - After submitting the API key, you can upload a PDF document and ask questions about the document.
   - You can also engage in real-time chat with the chatbot by typing questions in the chatbox.

That's it! You have successfully set up and run the Chatty Document Chatbot project. Enjoy chatting with your uploaded PDF documents!
