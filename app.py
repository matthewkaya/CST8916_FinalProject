from flask import Flask, request, jsonify
from utils.file_operations import read_records, write_record, update_record, delete_record, record_exists
import os

# Initialize Flask app
app = Flask(__name__)

# File paths
COMPANIES_FILE = "data/companies.txt"
VEHICLES_FILE = "data/vehicles.txt"
FUEL_RECORDS_FILE = "data/fuel_records.txt"

# CRUD routes for companies
@app.route('/companies', methods=['GET', 'POST', 'PUT', 'DELETE'])
def companies():
    if request.method == 'GET':
        records = read_records(COMPANIES_FILE)
        companies = [dict(zip(["company_code", "name", "address", "contact"], record.split('|'))) for record in records]
        return jsonify(companies), 200

    elif request.method == 'POST':
        data = request.json
        company_code = data.get("company_code")
        name = data.get("name")
        address = data.get("address")
        contact = data.get("contact")

        if not all([company_code, name, address, contact]):
            return jsonify({"error": "All fields are required"}), 400

        if record_exists(COMPANIES_FILE, company_code):
            return jsonify({"error": "Company code already exists"}), 400

        write_record(COMPANIES_FILE, f"{company_code}|{name}|{address}|{contact}")
        return jsonify({"message": "Company added successfully"}), 201

    elif request.method == 'PUT':
        data = request.json
        company_code = data.get("company_code")
        name = data.get("name")
        address = data.get("address")
        contact = data.get("contact")

        if not company_code:
            return jsonify({"error": "Company code is required"}), 400

        new_record = f"{company_code}|{name}|{address}|{contact}"
        if update_record(COMPANIES_FILE, company_code, new_record):
            return jsonify({"message": "Company updated successfully"}), 200
        else:
            return jsonify({"error": "Company not found"}), 404

    elif request.method == 'DELETE':
        company_code = request.args.get("company_code")
        if not company_code:
            return jsonify({"error": "Company code is required"}), 400

        if delete_record(COMPANIES_FILE, company_code):
            return jsonify({"message": "Company deleted successfully"}), 200
        else:
            return jsonify({"error": "Company not found"}), 404

# CRUD routes for vehicles
@app.route('/vehicles', methods=['GET', 'POST', 'PUT', 'DELETE'])
def vehicles():
    if request.method == 'GET':
        records = read_records(VEHICLES_FILE)
        vehicles = [dict(zip(["plate", "fuel_type", "company_code", "brand", "model"], record.split('|'))) for record in records]
        return jsonify(vehicles), 200

    elif request.method == 'POST':
        data = request.json
        plate = data.get("plate")
        fuel_type = data.get("fuel_type")
        company_code = data.get("company_code")
        brand = data.get("brand")
        model = data.get("model")

        if not all([plate, fuel_type, company_code, brand, model]):
            return jsonify({"error": "All fields are required"}), 400

        if record_exists(VEHICLES_FILE, plate):
            return jsonify({"error": "Vehicle plate already exists"}), 400

        write_record(VEHICLES_FILE, f"{plate}|{fuel_type}|{company_code}|{brand}|{model}")
        return jsonify({"message": "Vehicle added successfully"}), 201

    elif request.method == 'PUT':
        data = request.json
        plate = data.get("plate")
        fuel_type = data.get("fuel_type")
        company_code = data.get("company_code")
        brand = data.get("brand")
        model = data.get("model")

        if not plate:
            return jsonify({"error": "Vehicle plate is required"}), 400

        new_record = f"{plate}|{fuel_type}|{company_code}|{brand}|{model}"
        if update_record(VEHICLES_FILE, plate, new_record):
            return jsonify({"message": "Vehicle updated successfully"}), 200
        else:
            return jsonify({"error": "Vehicle not found"}), 404

    elif request.method == 'DELETE':
        plate = request.args.get("plate")
        if not plate:
            return jsonify({"error": "Vehicle plate is required"}), 400

        if delete_record(VEHICLES_FILE, plate):
            return jsonify({"message": "Vehicle deleted successfully"}), 200
        else:
            return jsonify({"error": "Vehicle not found"}), 404

# CRUD routes for fuel records
@app.route('/fuel_records', methods=['GET', 'POST', 'PUT', 'DELETE'])
def fuel_records():
    if request.method == 'GET':
        records = read_records(FUEL_RECORDS_FILE)
        fuel_records = [dict(zip(["plate", "price_per_litre", "litres", "total_price"], record.split('|'))) for record in records]
        return jsonify(fuel_records), 200

    elif request.method == 'POST':
        data = request.json
        plate = data.get("plate")
        price_per_litre = data.get("price_per_litre")
        litres = data.get("litres")
        total_price = data.get("total_price")

        if not all([plate, price_per_litre, litres, total_price]):
            return jsonify({"error": "All fields are required"}), 400

        write_record(FUEL_RECORDS_FILE, f"{plate}|{price_per_litre}|{litres}|{total_price}")
        return jsonify({"message": "Fuel record added successfully"}), 201

    elif request.method == 'PUT':
        data = request.json
        plate = data.get("plate")
        price_per_litre = data.get("price_per_litre")
        litres = data.get("litres")
        total_price = data.get("total_price")

        if not plate:
            return jsonify({"error": "Vehicle plate is required"}), 400

        new_record = f"{plate}|{price_per_litre}|{litres}|{total_price}"
        if update_record(FUEL_RECORDS_FILE, plate, new_record):
            return jsonify({"message": "Fuel record updated successfully"}), 200
        else:
            return jsonify({"error": "Fuel record not found"}), 404

    elif request.method == 'DELETE':
        plate = request.args.get("plate")
        if not plate:
            return jsonify({"error": "Vehicle plate is required"}), 400

        if delete_record(FUEL_RECORDS_FILE, plate):
            return jsonify({"message": "Fuel record deleted successfully"}), 200
        else:
            return jsonify({"error": "Fuel record not found"}), 404

# Start the Flask application
if __name__ == '__main__':
    os.makedirs(os.path.dirname(COMPANIES_FILE), exist_ok=True)
    app.run(debug=True)