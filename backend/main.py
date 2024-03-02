# backend/main.py

from fastapi import FastAPI, File, UploadFile, HTTPException , WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import io
from PyPDF2 import PdfReader
import openai

# Create a FastAPI instance
app = FastAPI()

# Mount the frontend directory as static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Define Jinja2Templates instance
templates = Jinja2Templates(directory="backend/templates")

# Global variable to store API key
api_key = " "

# Function to process PDF content
def process_pdf(content: bytes) -> str:
    try:
        # Open the PDF file using PdfReader
        pdf_reader = PdfReader(io.BytesIO(content))
        
        # Initialize an empty string to store extracted text
        extracted_text = ""

        # Iterate through each page of the PDF and extract text
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()

        # Return the extracted text
        return extracted_text

    except Exception as e:
        # Handle any exceptions that occur during PDF processing
        raise HTTPException(status_code=500, detail=f"Error processing PDF file: {str(e)}")

# Define homepage route
@app.get("/", response_class=HTMLResponse)
async def homepage(request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route to submit API key
@app.post("/api/key/")
async def submit_api_key(key: str):
    global api_key
    api_key = key
    return {"message": "API key submitted successfully"}

# Route to upload PDF file
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if not api_key:
        raise HTTPException(status_code=401, detail="API key is missing")
    try:
        # Read the content of the uploaded file
        content = await file.read()
        
        # Process the PDF content using the process_pdf function
        extracted_text = process_pdf(content)
        
        # Return the extracted text
        return {"text_content": extracted_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing PDF file: {}".format(str(e)))

# Route for chatbot interactions
@app.post("/chat/")
async def chat_with_bot(question: str):
    try:
        # Generate a response from OpenAI
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            temperature=0.7,
            max_tokens=150
        )
        
        # Extract the generated response
        response_text = response.choices[0].text.strip()
        
        # Return the response
        return {"response": response_text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing chat request")


# WebSocket endpoint for real-time communication
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
