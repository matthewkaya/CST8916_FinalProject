#!/bin/bash

# API Base URL
BASE_URL="http://127.0.0.1:5000"

# Log file
LOG_FILE="script_log.log"

# Clear the log file if it exists
> "$LOG_FILE"

# Function to print a separator
print_separator() {
  echo "--------------------------------------------" | tee -a "$LOG_FILE"
}

# Testing /companies endpoint
echo "Testing /companies endpoint" | tee -a "$LOG_FILE"
print_separator

# POST: Add a new company
echo "POST /companies" | tee -a "$LOG_FILE"
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"company_code": "C001", "name": "Test Company", "address": "123 Test St", "contact": "Test Contact"}' \
  "$BASE_URL/companies" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# GET: Retrieve all companies
echo "GET /companies" | tee -a "$LOG_FILE"
curl -s -X GET "$BASE_URL/companies" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# PUT: Update the company
echo "PUT /companies" | tee -a "$LOG_FILE"
curl -s -X PUT -H "Content-Type: application/json" \
  -d '{"company_code": "C001", "name": "Updated Company", "address": "456 New St", "contact": "Updated Contact"}' \
  "$BASE_URL/companies" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# DELETE: Delete the company
echo "DELETE /companies" | tee -a "$LOG_FILE"
curl -s -X DELETE "$BASE_URL/companies?company_code=C001" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# Testing /vehicles endpoint
echo "Testing /vehicles endpoint" | tee -a "$LOG_FILE"
print_separator

# POST: Add a new vehicle
echo "POST /vehicles" | tee -a "$LOG_FILE"
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"plate": "ONT 456", "fuel_type": "Diesel", "company_code": "C001", "brand": "Test Brand", "model": "Test Model"}' \
  "$BASE_URL/vehicles" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# GET: Retrieve all vehicles
echo "GET /vehicles" | tee -a "$LOG_FILE"
curl -s -X GET "$BASE_URL/vehicles" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# PUT: Update the vehicle
echo "PUT /vehicles" | tee -a "$LOG_FILE"
curl -s -X PUT -H "Content-Type: application/json" \
  -d '{"plate": "ONT 456", "fuel_type": "Gasoline", "company_code": "C001", "brand": "Updated Brand", "model": "Updated Model"}' \
  "$BASE_URL/vehicles" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# DELETE: Delete the vehicle
echo "DELETE /vehicles" | tee -a "$LOG_FILE"
curl -s -X DELETE -G "$BASE_URL/vehicles" --data-urlencode "plate=ONT 456"
echo | tee -a "$LOG_FILE"
print_separator

# Testing /fuel_records endpoint
echo "Testing /fuel_records endpoint" | tee -a "$LOG_FILE"
print_separator

# POST: Add a new fuel record
echo "POST /fuel_records" | tee -a "$LOG_FILE"
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"plate": "ONT 456", "price_per_litre": "1.50", "litres": "50", "total_price": "75.00"}' \
  "$BASE_URL/fuel_records" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# GET: Retrieve all fuel records
echo "GET /fuel_records" | tee -a "$LOG_FILE"
curl -s -X GET "$BASE_URL/fuel_records" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# PUT: Update the fuel record
echo "PUT /fuel_records" | tee -a "$LOG_FILE"
curl -s -X PUT -H "Content-Type: application/json" \
  -d '{"plate": "ONT 456", "price_per_litre": "2.00", "litres": "60", "total_price": "120.00"}' \
  "$BASE_URL/fuel_records" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# DELETE: Delete the fuel record
echo "DELETE /fuel_records" | tee -a "$LOG_FILE"
curl -s -X DELETE -G "$BASE_URL/fuel_records" --data-urlencode "plate=ONT 456"
echo | tee -a "$LOG_FILE"
print_separator

echo "API Tests Completed!" | tee -a "$LOG_FILE"