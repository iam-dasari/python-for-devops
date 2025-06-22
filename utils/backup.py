import shutil
import datetime
import os

def backup_files(source,destination):
    today=datetime.date.today()
    backup_file_name=os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar',source)
    
    
source="E:/dasari-devops-practice/python/python-for-devops/utils"
destination="E:/dasari-devops-practice/python/python-for-devops/utils/backups"
backup_files(source,destination)
