const BACKEND_URL = process.env.BACKEND_URL || "https://backend.onrender.com";

document.getElementById('uploadForm').onsubmit = async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('imageInput');
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    const response = await fetch(`${BACKEND_URL}/upload`, {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('results').textContent = JSON.stringify(result, null, 2);
};
