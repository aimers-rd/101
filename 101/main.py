import dropbox as db
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=db.Dropbox(self.access_token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)
def main():
    # change access_token to your own access token
    access_token = 'sl.BGqXA9-K69eiYZInqhVRDDkcweMZPcHgCpzGpwSgDBZfpiLjrStx2kGsySKEwluRoeFjxwLbKyy-H0-1fMWlvBbIQ-8IXUKQ1piP76lsHpZeBtCEu2-gv_n1pISU6X2t-12nbaEFPAWp'
    transferData= TransferData(access_token)
   # change file path to your own file path. Can also use input() to get user input for file path
    file_from='test.txt'
    # change file path to your liking . Can also use input() to get user input for file path
    file_to='/test3.txt'
    print(transferData.upload_file(file_from,file_to))

if __name__=='__main__':
     main()