from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from extract_text import extract_text_from_pdf
from resume_parser.resumeparse import resumeparse

app = Flask(__name__)
CORS(app)


@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    # Extract text from the uploaded PDF
    extracted_text = extract_text_from_pdf(file)
    data = resumeparse.read_file(file)
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(port=8000,debug=True)
