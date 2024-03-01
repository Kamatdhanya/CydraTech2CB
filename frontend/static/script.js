// Function to handle PDF upload
document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    try {
        const response = await fetch('/upload/', {
            method: 'POST',
            body: formData
        });
        if (response.ok) {
            const data = await response.json();
            console.log('Upload successful:', data);
            // Display response from backend or inform user
        } else {
            console.error('Error uploading PDF');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

// Function to handle question submission
document.getElementById('questionForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const question = document.getElementById('question').value;
    try {
        const response = await fetch('/chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question })
        });
        if (response.ok) {
            const data = await response.json();
            console.log('Response:', data);
            // Display response in chatbox
        } else {
            console.error('Error submitting question');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
