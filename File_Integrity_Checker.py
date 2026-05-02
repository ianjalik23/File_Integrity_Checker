from flask import Flask, request, session
import hashlib

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB limit


def generate_hash(file_data):
    return hashlib.sha256(file_data).hexdigest()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("file")

        if not file or file.filename == "":
            return "No file selected"

        file_data = file.read()
        new_hash = generate_hash(file_data)

        # store first upload in session
        if "stored_hash" not in session:
            session["stored_hash"] = new_hash
            return f"""
            <h2>🔐 First file stored</h2>
            <p>Hash: {new_hash}</p>
            <a href="/">Back</a>
            """

        # compare
        if new_hash == session["stored_hash"]:
            status = "UNCHANGED ✅"
        else:
            status = "MODIFIED ❌"

        return f"""
        <h2>🔍 Result</h2>
        <p>Hash: {new_hash}</p>
        <p>Status: {status}</p>
        <a href="/">Back</a>
        """

    return """
    <h1>File Integrity Checker</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
    """
    

if __name__ == "__main__":
    app.run(debug=True)
