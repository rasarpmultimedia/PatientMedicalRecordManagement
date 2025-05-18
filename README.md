Project Title: Patient Medical Record Management System
Project Brief:
 Build a CRUD-based REST API for managing patient medical records in a clinic or hospital. The application should be structured using Object-Oriented Programming (OOP) principles and follow proper FastAPI project organization. All data should be stored in separate JSON files for each entity using a dedicated file manager class. The application will include soft delete functionality for each entity with appropriate timestamp management.
Key Entities:
    • Patients

    • Doctors

    • Appointments

    • Medical Records

Features to Implement:
Patients:
    • GET /patients/ — List all patients (excluding deleted records) with pagination and filtering options

    • POST /patients/ — Create a new patient

    • GET /patients/{patient_id} — Retrieve patient details

    • PUT/PATCH /patients/{patient_id} — Update patient information

    • DELETE /patients/{patient_id} — Soft delete a patient (mark as deleted)

Doctors:
    • Implement similar CRUD operations as Patients

Appointments:
    • Assign a patient to a doctor at a specific date/time

    • Status: Scheduled, Completed, Cancelled

    • Ensure a doctor can’t have more than one appointment at the same time

Medical Records:
    • Link to a patient

    • Store diagnosis, prescriptions, treatment date

    • Implement full CRUD operations

Data to Collect:
Patient:
    • ID

    • Full Name

    • Age

    • Gender

    • Contact Information

    • Address

    • Emergency Contact

    • date_created (Timestamp of when the record was created)

    • date_updated (Timestamp of when the record was last updated)

    • date_deleted (Timestamp of when the record was soft-deleted, nullable)

Doctor:
    • ID

    • Full Name

    • Specialty

    • Years of Experience

    • Contact Information

    • date_created (Timestamp of when the record was created)

    • date_updated (Timestamp of when the record was last updated)

    • date_deleted (Timestamp of when the record was soft-deleted, nullable)

Appointment:
    • ID

    • Patient ID

    • Doctor ID

    • Date and Time

    • Status (Scheduled, Completed, Cancelled)

    • date_created (Timestamp of when the record was created)

    • date_updated (Timestamp of when the record was last updated)

    • date_deleted (Timestamp of when the record was soft-deleted, nullable)

Medical Record:
    • ID

    • Patient ID

    • Diagnosis

    • Prescriptions

    • Treatment Date

    • Doctor Notes

    • date_created (Timestamp of when the record was created)

    • date_updated (Timestamp of when the record was last updated)

    • date_deleted (Timestamp of when the record was soft-deleted, nullable)


CopyEdit
    • health_app/
    • ├── main.py
    • ├── routers/
    • │   ├── patients.py
    • │   ├── doctors.py
    • │   ├── appointments.py
    • │   └── medical_records.py
    • ├── models/
    • │   ├── patient.py
    • │   ├── doctor.py
    • │   ├── appointment.py
    • │   └── medical_record.py
    • ├── repositories/
    • │   ├── patient_repository.py
    • │   ├── doctor_repository.py
    • │   ├── appointment_repository.py
    • │   └── medical_record_repository.py
    • ├── services/
    • │   ├── patient_service.py
    • │   ├── doctor_service.py
    • │   ├── appointment_service.py
    • │   └── medical_record_service.py
    • ├── schemas/
    • │   └── ...
    • ├── middleware/
    • │   └── log_request_time.py
    • ├── utils/
    • │   ├── exceptions.py
    • │   └── file_manager.py
    • └── data/
    •     ├── patients.json
    •     ├── doctors.json
    •     ├── appointments.json
    •     └── medical_records.json


