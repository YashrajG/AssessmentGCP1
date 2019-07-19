import sys

from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))
    
def copy_blob(bucket_name, blob_name, new_bucket_name, new_blob_name):
    """Copies a blob from one bucket to another with a new name."""
    source_bucket = storage_client.get_bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.get_bucket(new_bucket_name)

    new_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, new_blob_name)

    print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(
        source_blob.name, source_bucket.name, new_blob.name,
        destination_bucket.name))

def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()

    print('Blob {} deleted.'.format(blob_name))

def move_blob(bucket_name, blob_name, new_bucket_name, new_blob_name):
    copy_blob(bucket_name, blob_name, new_bucket_name, new_blob_name)
    delete_blob(bucket_name, blob_name)



if __name__ == "__main__":
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(sys.argv[1])
    
    # Sample File for Upload, Copy, DOwnload
    file1Name = 'UCDoSample.txt'

    # Sample file for Upload, Move, DElete
    file2Name = 'UMDeSample.txt'

    print("initialisation done")
    
    upload_blob(sys.argv[1], file1Name, file1Name)
    upload_blob(sys.argv[1], file2Name, file2Name)

    copy_blob(sys.argv[1], file1Name, sys.argv[2], file1Name)

    # GCP Documentation mentions moving strategy as copy + delete original
    move_blob(sys.argv[1], file2Name, sys.argv[2], file2Name) 

    delete_blob(sys.argv[2], file2Name)

    download_blob(sys.argv[2], file1Name, file1Nam)