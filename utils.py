import os
import time
from google.cloud import documentai_v1beta3 as documentai
from google.cloud import storage
from google.api_core.client_options import ClientOptions


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


def create_dataset(PROJECT_ID, LOCATION, PROCESS_ID, gcs_uri_prefix):

    # Setup the endpoint correctly
    client_options = ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")

    # Initialize the Document AI client
    client = documentai.DocumentServiceAsyncClient(client_options=client_options)

    # Build the full dataset resource name
    dataset_name = f"projects/{PROJECT_ID}/locations/{LOCATION}/processors/{PROCESS_ID}/dataset"

    # Prepare the dataset configuration
    dataset = documentai.Dataset(
        name=dataset_name,
        gcs_managed_config=documentai.Dataset.GCSManagedConfig(
            gcs_prefix=documentai.GcsPrefix(
                gcs_uri_prefix=gcs_uri_prefix
            )
        ),
        spanner_indexing_config=documentai.Dataset.SpannerIndexingConfig()
    )

    # Prepare the update request
    update_request = documentai.UpdateDatasetRequest(
        dataset=dataset
    )

    # Call the update_dataset API
    operation = client.update_dataset(request=update_request)

    response = (await operation).result()
    return response