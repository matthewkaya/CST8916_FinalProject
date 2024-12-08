#!/bin/bash

# API Base URL
BASE_URL="http://127.0.0.1:5000"

# Log file
LOG_FILE="add_data_log.log"

# Clear the log file if it exists
> "$LOG_FILE"

# Function to print a separator
print_separator() {
  echo "--------------------------------------------" | tee -a "$LOG_FILE"
}

# Adding a company
echo "Adding a company" | tee -a "$LOG_FILE"
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"company_code": "C001", "name": "Test Company", "address": "123 Test St", "contact": "Test Contact"}' \
  "$BASE_URL/companies" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# Adding a vehicle
echo "Adding a vehicle" | tee -a "$LOG_FILE"
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"plate": "ONT 456", "fuel_type": "Diesel", "company_code": "C001", "brand": "Test Brand", "model": "Test Model"}' \
  "$BASE_URL/vehicles" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

# Adding a fuel record
echo "Adding a fuel record" | tee -a "$LOG_FILE"
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"plate": "ONT 456", "price_per_litre": "1.50", "litres": "50", "total_price": "75.00"}' \
  "$BASE_URL/fuel_records" | tee -a "$LOG_FILE"
echo | tee -a "$LOG_FILE"
print_separator

echo "Data addition completed!" | tee -a "$LOG_FILE"