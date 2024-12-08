import pytest
from app import app
import os
import logging

# Test file paths
COMPANIES_FILE = "data/companies.txt"
VEHICLES_FILE = "data/vehicles.txt"
FUEL_RECORDS_FILE = "data/fuel_records.txt"
LOG_FILE = "test_logs.log"

# Configure logging
def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # File handler to log to a file
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    
    # Stream handler to log to the terminal
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    
    # Avoid duplicate handlers
    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    
    return logger

logger = setup_logger()

@pytest.fixture
def client():
    """
    Pytest fixture to initialize the Flask test client and reset data files.
    """
    app.config['TESTING'] = True
    client = app.test_client()

    # Clear data files before tests
    for file_path in [COMPANIES_FILE, VEHICLES_FILE, FUEL_RECORDS_FILE]:
        if os.path.exists(file_path):
            open(file_path, 'w').close()

    logger.info("Data files have been cleared before starting tests.")
    yield client

# Test CRUD operations for companies
def test_companies_crud(client):
    logger.info("Testing CRUD operations for /companies")
    
    # POST: Add a new company
    company_data = {"company_code": "C001", "name": "Test Company", "address": "123 Test St", "contact": "Test Contact"}
    logger.info("Adding a new company")
    response = client.post("/companies", json=company_data)
    logger.debug(f"POST /companies response: {response.json}")
    assert response.status_code == 201

    # GET: Retrieve all companies
    logger.info("Retrieving all companies")
    response = client.get("/companies")
    logger.debug(f"GET /companies response: {response.json}")
    assert response.status_code == 200
    assert len(response.json) == 1

    # PUT: Update the company
    updated_company_data = {"company_code": "C001", "name": "Updated Company", "address": "456 New St", "contact": "Updated Contact"}
    logger.info("Updating the company")
    response = client.put("/companies", json=updated_company_data)
    logger.debug(f"PUT /companies response: {response.json}")
    assert response.status_code == 200

    # DELETE: Delete the company
    logger.info("Deleting the company")
    response = client.delete("/companies?company_code=C001")
    logger.debug(f"DELETE /companies response: {response.json}")
    assert response.status_code == 200

# Test CRUD operations for vehicles
def test_vehicles_crud(client):
    logger.info("Testing CRUD operations for /vehicles")
    
    # POST: Add a new vehicle
    vehicle_data = {"plate": "ONT 456", "fuel_type": "Diesel", "company_code": "C001", "brand": "Test Brand", "model": "Test Model"}
    logger.info("Adding a new vehicle")
    response = client.post("/vehicles", json=vehicle_data)
    logger.debug(f"POST /vehicles response: {response.json}")
    assert response.status_code == 201

    # GET: Retrieve all vehicles
    logger.info("Retrieving all vehicles")
    response = client.get("/vehicles")
    logger.debug(f"GET /vehicles response: {response.json}")
    assert response.status_code == 200
    assert len(response.json) == 1

    # PUT: Update the vehicle
    updated_vehicle_data = {"plate": "ONT 456", "fuel_type": "Gasoline", "company_code": "C001", "brand": "Updated Brand", "model": "Updated Model"}
    logger.info("Updating the vehicle")
    response = client.put("/vehicles", json=updated_vehicle_data)
    logger.debug(f"PUT /vehicles response: {response.json}")
    assert response.status_code == 200

    # DELETE: Delete the vehicle
    logger.info("Deleting the vehicle")
    response = client.delete("/vehicles?plate=ONT 456")
    logger.debug(f"DELETE /vehicles response: {response.json}")
    assert response.status_code == 200

# Test CRUD operations for fuel records
def test_fuel_records_crud(client):
    logger.info("Testing CRUD operations for /fuel_records")
    
    # POST: Add a new fuel record
    fuel_record_data = {"plate": "ONT 456", "price_per_litre": "1.50", "litres": "50", "total_price": "75.00"}
    logger.info("Adding a new fuel record")
    response = client.post("/fuel_records", json=fuel_record_data)
    logger.debug(f"POST /fuel_records response: {response.json}")
    assert response.status_code == 201

    # GET: Retrieve all fuel records
    logger.info("Retrieving all fuel records")
    response = client.get("/fuel_records")
    logger.debug(f"GET /fuel_records response: {response.json}")
    assert response.status_code == 200
    assert len(response.json) == 1

    # PUT: Update the fuel record
    updated_fuel_record_data = {"plate": "ONT 456", "price_per_litre": "2.00", "litres": "60", "total_price": "120.00"}
    logger.info("Updating the fuel record")
    response = client.put("/fuel_records", json=updated_fuel_record_data)
    logger.debug(f"PUT /fuel_records response: {response.json}")
    assert response.status_code == 200

    # DELETE: Delete the fuel record
    logger.info("Deleting the fuel record")
    response = client.delete("/fuel_records?plate=ONT 456")
    logger.debug(f"DELETE /fuel_records response: {response.json}")
    assert response.status_code == 200