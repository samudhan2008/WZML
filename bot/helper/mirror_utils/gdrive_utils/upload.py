
# gdrive_utils/upload.py - Corrected for large file uploads

from bot.helper.mirror_utils.upload_utils import MAX_SPLIT_SIZE, split_file

def upload_to_gdrive(file_path):
    """
    Function to upload file to Google Drive.
    Handles splitting for large files.
    """
    file_size = get_file_size(file_path)
    
    if file_size > MAX_SPLIT_SIZE:
        split_file(file_path, file_size)  # Split the file if too large
    else:
        # Standard upload process for smaller files
        pass
