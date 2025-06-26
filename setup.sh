#!/bin/bash

# Enhanced Contact Form Setup Script
echo "Setting up Enhanced Contact Form Solution..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    echo "Please install Python 3.11 or later and try again."
    exit 1
fi

# Navigate to backend directory
cd contact-form-backend

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "Setup complete! To run the solution:"
echo ""
echo "1. Start the backend server:"
echo "   cd contact-form-backend"
echo "   source venv/bin/activate"
echo "   python src/main.py"
echo ""
echo "2. Open yubea-website/index.html in your web browser"
echo ""
echo "3. Test the contact form!"
echo ""
echo "Make sure your Make.com scenario is active and configured."
echo "See implementation-guide.md for detailed instructions."

