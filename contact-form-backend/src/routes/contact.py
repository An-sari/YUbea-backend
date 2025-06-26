from flask import Blueprint, request, redirect, url_for, render_template_string, jsonify
import requests
import logging

contact_bp = Blueprint('contact', __name__)

# Make.com webhook URL
MAKE_WEBHOOK_URL = "https://hook.eu2.make.com/yxryuvqyykteafo1fysggvdna82lrba2"

@contact_bp.route('/submit-contact', methods=['POST'])
def submit_contact():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        project = request.form.get('project')
        
        # Validate required fields
        if not name or not email or not project:
            return jsonify({'error': 'All fields are required'}), 400
        
        # Prepare data for Make.com
        webhook_data = {
            'name': name,
            'email': email,
            'project_type': project
        }
        
        # Send data to Make.com webhook
        response = requests.post(MAKE_WEBHOOK_URL, json=webhook_data, timeout=10)
        
        if response.status_code == 200:
            # Redirect to thank you page
            return redirect('/thank-you.html')
        else:
            logging.error(f"Make.com webhook failed: {response.status_code} - {response.text}")
            return jsonify({'error': 'Failed to process submission'}), 500
            
    except requests.exceptions.RequestException as e:
        logging.error(f"Request to Make.com failed: {str(e)}")
        return jsonify({'error': 'Failed to process submission'}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

@contact_bp.route('/test-webhook', methods=['GET'])
def test_webhook():
    """Test endpoint to verify webhook connectivity"""
    try:
        test_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'project_type': 'web-app'
        }
        
        response = requests.post(MAKE_WEBHOOK_URL, json=test_data, timeout=10)
        
        return jsonify({
            'status': 'success' if response.status_code == 200 else 'failed',
            'status_code': response.status_code,
            'response': response.text
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500

