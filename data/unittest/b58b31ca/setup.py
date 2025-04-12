import time
import requests
import os
PATIENT_RECORDS = {
    "P1001": {
        "patient_id": "P1001",
        "assigned_staff": ["D101", "N201"],
        "medical_data": "Medical history for patient P1001"
    },
    "P1002": {
        "patient_id": "P1002",
        "assigned_staff": ["D102", "N202"],
        "medical_data": "Medical history for patient P1002"
    }
}