import dropbox
class TransferData :
    def __init__ (self,access_token) :
        self.access_token = access_token
    def upload_onepiece(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
def main() :
    access_token = "sl.BB4WrqWMcFAdo6fMHDmWS09Hf09cNG5OX-XnH_MeHIG18f-n9TkBo_5eNrwPLZqpe8rOtGTODR8_wuEVsa5kxGZ6cTVJycrby1cSE_uhSXYq_a8a_m5yRi46Dev3voXWydlFM9c"
    transferData = TransferData(access_token)
    file_from = input("Enter The File Name ")
    file_to = input("eneter the full path to upload to dropbox hehehe noob")
    transferData.upload_onepiece(file_from,file_to)
    print("file has been moved")
main()