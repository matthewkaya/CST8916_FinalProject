import os

def read_records(file_path):
    """
    Reads all records from the specified text file.
    Returns a list of records as strings.
    """
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def write_record(file_path, record):
    """
    Appends a new record to the specified text file.
    """
    with open(file_path, 'a') as file:
        file.write(record + '\n')

def update_record(file_path, key, new_record):
    """
    Updates a record in the specified text file.
    The record to be updated is identified by the `key`.
    """
    records = read_records(file_path)
    updated = False
    with open(file_path, 'w') as file:
        for record in records:
            if record.startswith(key):
                file.write(new_record + '\n')
                updated = True
            else:
                file.write(record + '\n')
    return updated

def delete_record(file_path, key):
    """
    Deletes a record from the specified text file.
    The record to be deleted is identified by the `key`.
    """
    records = read_records(file_path)
    deleted = False
    with open(file_path, 'w') as file:
        for record in records:
            if not record.startswith(key):
                file.write(record + '\n')
            else:
                deleted = True
    return deleted

def record_exists(file_path, key):
    """
    Checks if a record with the given `key` exists in the specified text file.
    """
    records = read_records(file_path)
    return any(record.startswith(key) for record in records)