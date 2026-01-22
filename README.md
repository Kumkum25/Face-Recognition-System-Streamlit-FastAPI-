<!DOCTYPE html>
<html>
<head>

</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">

<h1>Face Recognition System</h1>
<h3>Real-Time Face Detection & Recognition using Streamlit and FastAPI</h3>

<hr>

<h2>1. Overview</h2>
<p>
This project is an end-to-end Face Recognition System designed to perform real-time face detection and identity recognition using a webcam.
It provides both a user-friendly web interface and a RESTful API for seamless integration into real-world applications.
</p>

<h2>2. Key Highlights</h2>
<ul>
  <li>Real-time face detection from live camera feed</li>
  <li>Face recognition with identity matching</li>
  <li>Image preprocessing and feature extraction</li>
  <li>Dual deployment architecture:
    <ul>
      <li>Web UI using Streamlit</li>
      <li>Backend services using FastAPI</li>
    </ul>
  </li>
  <li>Scalable design for multiple users</li>
</ul>

<h2>3. System Architecture</h2>
<pre>
User → Streamlit UI → Face Recognition Engine → Results
             ↓
         FastAPI (REST API)
</pre>

<h2>4. Tech Stack</h2>
<table border="1" cellpadding="6">
<tr><th>Category</th><th>Tools</th></tr>
<tr><td>Language</td><td>Python</td></tr>
<tr><td>Computer Vision</td><td>OpenCV</td></tr>
<tr><td>Deep Learning</td><td>CNN-based embeddings</td></tr>
<tr><td>Frontend</td><td>Streamlit</td></tr>
<tr><td>Backend</td><td>FastAPI</td></tr>
<tr><td>Server</td><td>Uvicorn</td></tr>
</table>

<h2>5. Project Structure</h2>
<pre>
Face Recognition System/
 ├── app/
 │    ├── api/              # API routes
 │    ├── frs/              # Face recognition logic
 │    ├── data/             # Images / embeddings
 │    ├── config.py         # Configuration
 │    └── main.py           # FastAPI entry point
 │
 ├── streamlit_app.py       # Streamlit UI
 ├── requirements.txt
 └── README.md

</pre>

<h2>6. Installation & Setup</h2>
<pre>
# Create and activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
</pre>

<h2>7. Running the Application</h2>

<h3>A. Web Interface (Streamlit)</h3>
<pre>
streamlit run streamlit_app.py
</pre>

<h3>B. API Backend (FastAPI)</h3>
<pre>
uvicorn app.main:app --reload
</pre>

<h2>8. Execution Modes</h2>
<table border="1" cellpadding="6">
<tr><th>Mode</th><th>Description</th></tr>
<tr><td>Streamlit UI</td><td>Interactive web-based face recognition</td></tr>
<tr><td>FastAPI</td><td>REST API for external system integration</td></tr>
</table>

<h2>9. Results & Output</h2>
<ul>
  <li>Face detection bounding box</li>
  <li>Recognized identity label</li>
  <li>Live camera feed</li>
</ul>

<h2>10. Demo Video</h2>
<p>(https://drive.google.com/file/d/1FlUY8FreHt_hMIWUemZ6nVdH6vfCwj4D/view?usp=sharing)</p>

<h2>11. Real-World Use Cases</h2>
<ul>
  <li>Biometric login systems</li>
  <li>Smart attendance solutions</li>
  <li>Surveillance and security</li>
  <li>Identity verification platforms</li>
</ul>

<h2>12. Future Enhancements</h2>
<ul>
  <li>Face recognition under low-light conditions</li>
  <li>Database integration (MongoDB / PostgreSQL)</li>
  <li>Cloud deployment (AWS / GCP)</li>
  <li>Mobile application interface</li>
</ul>

<h2>13. Conclusion</h2>
<p>
This project demonstrates a complete real-time computer vision system with both frontend and backend integration, following industry-level architecture and deployment practices.
</p>

</body>
</html>
