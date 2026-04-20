import os
import re
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load Vapi Variables
VAPI_API_KEY = os.environ.get('VAPI_API_KEY')
VAPI_ASSISTANT_ID = os.environ.get('VAPI_ASSISTANT_ID')
VAPI_PHONE_NUMBER_ID = os.environ.get('VAPI_PHONE_NUMBER_ID')

def validate_phone_number(phone_number):
    """Basic validation for E.164 phone number format"""
    pattern = re.compile(r"^\+?[1-9]\d{1,14}$")
    return pattern.match(phone_number)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call', methods=['POST'])
def make_call():
    if not VAPI_API_KEY or not VAPI_ASSISTANT_ID or not VAPI_PHONE_NUMBER_ID:
        return jsonify({'success': False, 'message': 'Vapi credentials not configured properly in .env.'}), 500

    data = request.json
    phone_number = data.get('phone_number')
    message_type = data.get('message_type', 'default')

    if not phone_number:
        return jsonify({'success': False, 'message': 'Phone number is required.'}), 400

    if not validate_phone_number(phone_number):
        return jsonify({'success': False, 'message': 'Invalid phone number format. Please use E.164 (e.g., +1234567890).'}), 400

    # Optional: Override the assistant's first message based on message_type
    first_message_map = {
        'sales': "Hi! I'm calling to check if you'd like to renew your AI subscription.",
        'support': "Hello! I'm calling because your support ticket has been resolved. Let me walk you through the details.",
        'default': "Hello! I'm your AI voice assistant. How can I help you today?"
    }
    first_message = first_message_map.get(message_type, first_message_map['default'])

    # ----------------------------------------------------------
    # Call the Vapi API to initiate an outbound phone call
    # ----------------------------------------------------------
    vapi_url = "https://api.vapi.ai/call/phone"

    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "assistantId": VAPI_ASSISTANT_ID,
        "phoneNumberId": VAPI_PHONE_NUMBER_ID,
        "customer": {
            "number": phone_number
        },
        "assistantOverrides": {
            "firstMessage": first_message
        }
    }

    try:
        response = requests.post(vapi_url, headers=headers, json=payload)
        response.raise_for_status()

        call_data = response.json()

        return jsonify({
            'success': True,
            'message': 'AI voice call initiated successfully!',
            'call_sid': call_data.get('id')  # Vapi's call ID
        }), 200

    except requests.exceptions.RequestException as e:
        error_msg = str(e)
        if hasattr(e, 'response') and e.response is not None:
            error_msg = e.response.text

        return jsonify({
            'success': False,
            'message': f'Vapi API Error: {error_msg}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

