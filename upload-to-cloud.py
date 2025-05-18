import os
from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_path, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)
    print(f"File uploaded to gs://{bucket_name}/{destination_blob_name}.")

def main():
    bucket_name = "ani_test_bucket"  
    source_file_path = "/Users/aniprodanova/Desktop/First-DE-GCS-project/Customers_TEST1.csv"  
    destination_blob_name = "raw/Customers_TEST1.csv"  

    if not os.path.exists(source_file_path):
        print(f"Error: File not found at {source_file_path}")
        return

    upload_to_gcs(bucket_name, source_file_path, destination_blob_name)

if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/aniprodanova/Desktop/First-DE-GCS-project/de-1st-project-key.json"  
    main()




       