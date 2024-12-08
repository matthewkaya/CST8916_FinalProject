#!/bin/bash

# Create the directory structure for the application
mkdir -p data utils

# Create necessary data files with default headers
echo "Company Code|Company Name|Address|Contact Information" > data/companies.txt
echo "Plate|Fuel Type|Company Code|Brand|Model" > data/vehicles.txt
echo "Plate|Price Per Litre|Litres|Total Price" > data/fuel_records.txt

# Create a requirements file with additional dependencies
cat <<EOL > requirements.txt
flask
flask-restful
flask-cors
python-dotenv
requests
pytest
black
flake8
EOL

# Create empty Python files
touch app.py
touch utils/file_operations.py

# Install Python requirements
echo "Installing Python requirements..."
pip install -r requirements.txt

# Display a confirmation message
echo "Application setup complete! Directories, files, and dependencies are ready."