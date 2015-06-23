"""
      Usually I will have more PDF files in my Downloads path like 300 and 400 pdf files. Sometimes it will be tough to search something I need. So this program move them to appropriate folder in minute of time.
"""
from os import listdir
from os.path import isfile,join
import fnmatch
import shutil


path="/home/ak/Downloads"
for file in listdir(path):
    if fnmatch.fnmatch(file,"*.pdf"):
        if fnmatch.fnmatch(file,"*report*") or fnmatch.fnmatch(file,'*sale*') or fnmatch.fnmatch(file,'*purchase*'):
            src=path+"/"+file
            dst=path+"/reports"
            shutil.move(src, dst)
        if fnmatch.fnmatch(file,'*odoo*') or fnmatch.fnmatch(file,'*openerp*'):
            src=path+"/"+file
            dst=path+"/odoo"
            shutil.move(src, dst)
        if fnmatch.fnmatch(file,"*python*"):
            src=path+"/"+file
            dst=path+"/python"
            shutil.move(src,dst)
