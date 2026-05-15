document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyze-btn');
    const reviewInput = document.getElementById('review-input');
    const loader = document.getElementById('loader');
    const btnText = analyzeBtn.querySelector('.btn-text');
    const resultSection = document.getElementById('result-section');
    const sentimentBadge = document.getElementById('sentiment-badge');
    const sentimentLabelText = document.getElementById('sentiment-label-text');
    const confidenceBar = document.getElementById('confidence-bar');
    const confidenceValue = document.getElementById('confidence-value');

    analyzeBtn.addEventListener('click', async () => {
        const review = reviewInput.value.trim();

        if (!review) {
            alert('Please enter a review first!');
            return;
        }

        // Show loading state
        analyzeBtn.disabled = true;
        loader.style.display = 'inline-block';
        btnText.style.display = 'none';
        resultSection.classList.add('hidden');

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ review }),
            });

            const data = await response.json();

            if (data.error) {
                alert('Error: ' + data.error);
            } else {
                displayResults(data);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Something went wrong. Please check if the Flask server is running.');
        } finally {
            // Restore button state
            analyzeBtn.disabled = false;
            loader.style.display = 'none';
            btnText.style.display = 'inline-block';
        }
    });

    function displayResults(data) {
        const sentiment = data.sentiment;
        const confidence = data.confidence;

        // Set sentiment label and badge
        sentimentLabelText.textContent = sentiment;
        sentimentBadge.textContent = sentiment;
        
        // Remove old classes and add new one
        sentimentBadge.classList.remove('positive', 'negative');
        sentimentBadge.classList.add(sentiment.toLowerCase());

        // Set confidence
        confidenceValue.textContent = `${confidence}%`;
        confidenceBar.style.width = '0%';
        
        setTimeout(() => {
            confidenceBar.style.width = `${confidence}%`;
        }, 100);

        // Show result section
        resultSection.classList.remove('hidden');
    }
});
