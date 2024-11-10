import os
import zipfile
import rarfile
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename='extraction_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Target directory where archives are located
target_directory = 'G:/My Folder'
delete_after_extraction = True  # Delete archive files after extraction is complete

# Function to extract ZIP or RAR files
def extract_archive(archive_path, extract_to):
    try:
        if archive_path.endswith('.zip'):
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
        elif archive_path.endswith('.rar'):
            with rarfile.RarFile(archive_path, 'r') as rar_ref:
                rar_ref.extractall(extract_to)
        logging.info(f'Successfully extracted {archive_path} to {extract_to}')
    except Exception as e:
        logging.error(f'Error extracting {archive_path}: {e}')

# Main function for batch extraction of archives
def batch_extract():
    for archive_name in os.listdir(target_directory):
        archive_path = os.path.join(target_directory, archive_name)
        
        if archive_name.endswith(('.zip', '.rar')) and os.path.isfile(archive_path):
            folder_name = os.path.splitext(archive_name)[0]
            extract_to = os.path.join(target_directory, folder_name)
            os.makedirs(extract_to, exist_ok=True)

            # Extract the archive
            extract_archive(archive_path, extract_to)

            # Delete archive after extraction if set to do so
            if delete_after_extraction:
                try:
                    os.remove(archive_path)
                    logging.info(f'Deleted archive {archive_path} after extraction')
                except Exception as e:
                    logging.error(f'Error deleting {archive_path}: {e}')

if __name__ == "__main__":
    batch_extract()
    print("Batch extraction completed. Check extraction_log.txt for details.")
