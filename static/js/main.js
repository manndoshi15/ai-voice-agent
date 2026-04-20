document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('call-form');
    const phoneInput = document.getElementById('phone');
    const callBtn = document.getElementById('call-btn');
    const btnText = document.querySelector('.btn-text');
    const btnLoader = document.querySelector('.btn-loader');
    const resultMessage = document.getElementById('result-message');

    // Phone number formatting as user types (basic UI enhancement)
    phoneInput.addEventListener('input', (e) => {
        let val = e.target.value;
        if (val && !val.startsWith('+')) {
            e.target.value = '+' + val;
        }
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const phoneNumber = phoneInput.value.trim();
        
        // Basic frontend validation
        if (!/^\+?[1-9]\d{1,14}$/.test(phoneNumber)) {
            showResult('Please enter a valid E.164 phone number (e.g., +1234567890)', 'error');
            return;
        }

        // Setup UI for loading
        setLoading(true);
        hideResult();

        try {
            const response = await fetch('/call', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    phone_number: phoneNumber
                })
            });

            const data = await response.json();

            if (response.ok) {
                showResult(data.message || 'Call initiated successfully!', 'success');
                // Optional: clear input after success
                // phoneInput.value = '';
            } else {
                showResult(data.message || 'Failed to initiate call.', 'error');
            }
        } catch (error) {
            console.error('Error making calling request:', error);
            showResult('Network error. Please try again later.', 'error');
        } finally {
            setLoading(false);
        }
    });

    function setLoading(isLoading) {
        if (isLoading) {
            callBtn.disabled = true;
            btnText.style.display = 'none';
            btnLoader.style.display = 'flex';
        } else {
            callBtn.disabled = false;
            btnText.style.display = 'block';
            btnLoader.style.display = 'none';
        }
    }

    function showResult(message, type) {
        resultMessage.textContent = message;
        resultMessage.className = `result ${type}`; // removes 'hidden' implicitly
    }

    function hideResult() {
        resultMessage.classList.add('hidden');
    }
});
