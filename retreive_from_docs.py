from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account JSON key file
SERVICE_ACCOUNT_FILE = "path/to/your/service_account_key.json"
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# Document ID of the Google Doc you want to retrieve
DOCUMENT_ID = "your_document_id_here"

def list_google_doc_content():
    # Authenticate using the service account
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    # Build the Google Docs service
    service = build('docs', 'v1', credentials=credentials)
    
    # Retrieve the document
    document = service.documents().get(documentId=DOCUMENT_ID).execute()
    
    # Process and print the document content
    content = document.get('body', {}).get('content', [])
    for element in content:
        if 'paragraph' in element:
            text_runs = element['paragraph'].get('elements', [])
            for run in text_runs:
                text = run.get('textRun', {}).get('content')
                if text:
                    print(text, end="")  # Print text without extra newlines

if __name__ == "__main__":
    list_google_doc_content()
