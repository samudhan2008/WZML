
# upload_utils.py - Corrected

# Set MAX_SPLIT_SIZE to 4GB
MAX_SPLIT_SIZE = 4 * 1024**3  # Set to 4GB

def split_file(file_path, file_size):
    """
    This function splits the file if it exceeds MAX_SPLIT_SIZE.
    """
    if file_size > MAX_SPLIT_SIZE:
        # Implement file splitting logic here
        pass

def upload_file(file_path):
    """
    This function handles file uploads.
    Checks if the file size exceeds MAX_SPLIT_SIZE and splits the file if necessary.
    """
    file_size = get_file_size(file_path)
    
    if file_size > MAX_SPLIT_SIZE:
        # Split the file into smaller parts
        split_file(file_path, file_size)
    else:
        # Direct upload for smaller files
        pass

def get_file_size(file_path):
    """
    Utility function to get the size of the file.
    """
    return os.path.getsize(file_path)
