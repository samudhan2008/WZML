
# telegram_uploader.py - Corrected for large file uploads

from bot.helper.mirror_utils.upload_utils import MAX_SPLIT_SIZE, split_file

class TelegramUploader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_size = get_file_size(file_path)

    def upload(self):
        if self.file_size > MAX_SPLIT_SIZE:
            split_file(self.file_path, self.file_size)  # Split the file if too large
        else:
            # Standard Telegram upload process for smaller files
            pass

    def get_file_size(self, file_path):
        """
        Utility function to get the size of the file.
        """
        return os.path.getsize(file_path)
