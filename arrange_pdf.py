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