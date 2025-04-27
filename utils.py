import os
import time
from google.cloud import documentai_v1 as documentai
from google.cloud import storage


# --------------- CONFIGURATION -------------------
PROJECT_ID = "prj-app-wh-dev"
LOCATION = "us"  # or "eu" depending on your processor location
GCS_BUCKET = "your-gcs-bucket-name"

# Provide paths
LOCAL_DOCUMENTS_DIR = "path_to_documents"
LOCAL_ANNOTATIONS_DIR = "path_to_annotations"  # JSON annotation files

# Schema
SCHEMA_FIELDS = [
    {"name": "Patient Name", "type": "text"},
    {"name": "DOB", "type": "date"},
    {"name": "Medical Record Number", "type": "number"},
    # Add more fields according to your form
]

def create_processor(client, display_name):
    parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"
    processor = documentai.Processor(
        type_="CUSTOM_EXTRACTION_PROCESSOR",  # Very important
        display_name=display_name,
    )
    response = client.create_processor(parent=parent, processor=processor)
    print(f"Processor created: {response.name}")
    return response.name


client = documentai.DocumentProcessorServiceClient()
processor_name = create_processor(client, display_name="automation_test_processor")
processor_id = processor_name.split("/")[-1]