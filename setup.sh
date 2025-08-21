#!/bin/bash

echo "Setting up NeuroScan Brain Tumor Detection Project..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete! To run the application:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the Streamlit app: streamlit run app.py"
echo ""
echo "Or simply run: ./run.sh" 