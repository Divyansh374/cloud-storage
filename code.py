import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Bb-wJhVW8lxazCbblY3mHs7_QNneAHAxmRlxdwU2dU1fBph-ZH82GYhtDlPlH13x-LHIdsXeIu9VjZgt9rNqWgJBCilXDFeOXt0LmVz62eiH5YxGoKMq4WtVI5ZV5_1_rwZtlaSEnIKX'
    transferData = TransferData(access_token)

    file_from = 'PRO-C101/test.txt'
    file_to = '/test_folder/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()