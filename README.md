# Google Document AI Pipeline 🗎

This repo automates the process of integrating Google Document AI with custom processors, schema creation, document annotation, and model training. It allows users to efficiently create and manage document parsing workflows directly from a user-friendly dashboard.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Setup and Configuration](#setup-and-configuration)

## Overview
Google Document AI enables organizations to automate document parsing and extract structured data from various document formats. However, setting up and managing the custom processors, schema creation, document uploads, annotations, and model training can be time-consuming.

The **Google Document AI Pipeline** project simplifies this by automating the entire workflow:

1. **Schema Creation**: Users can create a custom schema via a dashboard.
2. **Document Upload**: Users upload documents directly to the platform.
3. **Document Annotation**: The platform allows easy annotation of documents for training.
4. **Custom Processor Creation**: A Python script automatically creates a new Google Document AI custom processor.
5. **Model Training**: After all necessary data and annotations are uploaded, the pipeline starts training the model.

This fully automated pipeline reduces the manual work required to implement and train Google Document AI models.

## Features
- **Automated Schema Creation**: Users define and create schemas through a dashboard interface.
- **Easy Document Upload**: Upload medical forms (or any other document type) directly to the dashboard.
- **Annotation Support**: Annotate documents to train the model on specific data.
- **Custom Processor Setup**: Automatically create and configure a new custom processor on Google Document AI.
- **Model Training Automation**: Start training the model with the push of a button, using the provided annotations.
- **User-Friendly Dashboard**: Intuitive dashboard to manage schema creation, document uploads, and annotations.

## Getting Started
To get started with **google-doc-ai-pipeline**, follow these instructions:

### Prerequisites
- Google Cloud account with access to Google Document AI.
- Basic knowledge of Python and Google Cloud API setup.
- Docker (optional for containerization).

### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/google-doc-ai-pipeline.git
   cd google-doc-ai-pipeline

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Google Cloud credentials:
   - Create a Google Cloud project and enable the Document AI API.
   - Download your service account credentials as a JSON file and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable:
     
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path-to-your-service-account-file.json"
   ```
## Usage
Once the repository is set up and the environment is configured, follow these steps to use the pipeline:
1. **Create Schema:** Go to the dashboard and create a schema for the documents you wish to process.
2. **Upload Documents:** Upload the documents you want to annotate and process.
3. **Annotate Documents:** Use the dashboard to annotate documents with the relevant information for training.
4. **Run the Python Script:** Once the documents are uploaded and annotated, execute the Python script to:
   - Create a new custom processor on Google Document AI.
   - Add the schema, documents, and annotations.
   - Start the training process.
```bash
python train_model.py
```

### Setup and Configuration
You can configure the pipeline by editing the following files:
- `config.json`: Contains configurations related to Google Document AI settings (e.g., project ID, custom processor settings).
- `dashboard/config.py`: Contains dashboard-specific settings.


