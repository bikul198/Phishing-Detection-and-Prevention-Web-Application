document.getElementById("urlForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const url = document.getElementById("urlInput").value.trim();
    const resultElement = document.getElementById("result");

    if (!url) {
        resultElement.textContent = "❌ Please enter a URL!";
        resultElement.className = 'invalid';
        return;
    }

    resultElement.textContent = "Checking...";
    resultElement.className = "";

    try {
        const response = await fetch(`/check_phishing?url=${encodeURIComponent(url)}`);
        const result = await response.json();

        resultElement.textContent = result.message;
        resultElement.className = result.status;
    } catch (error) {
        resultElement.textContent = "❌ Server error. Try again.";
        resultElement.className = 'invalid';
    }
});
