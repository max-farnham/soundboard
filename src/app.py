from flask import Flask, request, jsonify, render_template
from azure.storage.blob import BlobServiceClient, ContentSettings
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from datetime import datetime
import os

# Load environment variables from .env
load_dotenv()

# Allowed audio types
ALLOWED_AUDIO_TYPES = {
    "audio/wav",
    "audio/mpeg",
    "audio/mp4",
    "audio/x-wav",
    "audio/x-m4a",
    "audio/ogg",
    "audio/flac",
}

# Environment variables
STORAGE_URL = os.environ.get("STORAGE_ACCOUNT_URL", "")
CONTAINER = os.environ.get("AUDIO_CONTAINER", "")
AZURE_KEY = os.environ.get("AZURE_KEY", "")


if not STORAGE_URL or not STORAGE_URL.startswith("https://"):
    raise RuntimeError(f"Invalid STORAGE_ACCOUNT_URL: '{STORAGE_URL}'")

if not CONTAINER:
    raise RuntimeError("AUDIO_CONTAINER environment variable is missing.")

if not AZURE_KEY:
    raise RuntimeError("AZURE_KEY environment variable is missing.")


# Create blob client
bsc = BlobServiceClient(account_url=STORAGE_URL, credential=AZURE_KEY)
cc = bsc.get_container_client(CONTAINER)

# Create Flask app
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "../templates"))

# Helper function
def is_allowed_audio(content_type):
    return content_type in ALLOWED_AUDIO_TYPES

# Upload route
@app.post("/api/v1/upload")
def upload_audio():
    if "file" not in request.files:
        return jsonify(ok=False, error="No file provided"), 400

    f = request.files["file"]

    if not is_allowed_audio(f.content_type):
        return jsonify(ok=False, error="Invalid audio type"), 400

    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    sanitized = secure_filename(f.filename)
    blob_name = f"{timestamp}-{sanitized}"

    try:
        cc.upload_blob(
            blob_name,
            f,
            overwrite=True,
            content_settings=ContentSettings(content_type=f.content_type)
        )
        url = f"{cc.url}/{blob_name}"
        return jsonify(ok=True, url=url)

    except Exception as e:
        return jsonify(ok=False, error=str(e)), 500

# Gallery route (JSON)
@app.get("/api/v1/gallery")
def gallery():
    try:
        urls = [f"{cc.url}/{b.name}" for b in cc.list_blobs()]
        return jsonify(ok=True, gallery=urls)
    except Exception as e:
        return jsonify(ok=False, error=str(e)), 500

# Health route
@app.get("/health")
def health():
    return jsonify(ok=True)

# Index route (renders HTML)
@app.get("/")
def index():
    files = [f"{cc.url}/{b.name}" for b in cc.list_blobs()]
    return render_template("index.html", files=files)

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

