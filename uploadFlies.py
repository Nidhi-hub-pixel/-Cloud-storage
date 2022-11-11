import os
from pip import dropbox 
from dropbox.files import WriteMode
#
class TransferData:
    def _init_(self,access_token):
        self.excess_token=access_token
#
    def upload_file(self,file_from,file_to) :
         dbx=dropbox.Dropbox(self.access_token)

         for route,dirs,files in os.walk(file_from):

             for filename in files:
                 local_path=os.path.join(route_filename) 

                 relative_path=os.path.relpath(local_path,file_from) 
                 dropbox_path=os.path.join(file_to,relative_path)

                 with open(local_path,'rb') as f:
                       dbx.files_upload(f.read(), dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token=''
    transferData=TransferData(access_token)

    file_from=str(input("enter the folder path to transfer"))
    file_to=input("enter the full path to upload to the dropbox")

    TransferData.upload_file(file_from,file_to)
    print("file has been moved")

main()
