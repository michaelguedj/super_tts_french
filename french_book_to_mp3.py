# -*- coding: utf8 -*
import sys, os, shutil
from odt2txt_modif import OpenDocumentTextFile

# Book Conversion into a string list
book = sys.argv[1]
odt = OpenDocumentTextFile(book)
unicode = odt.toString()

# renaming of the book (without ".odt")
book = book.replace(".odt", "")

txt_folder = f"{book}_txt"

# One erases the folder if it already exists
if os.path.exists(txt_folder):
    shutil.rmtree(txt_folder)

os.mkdir(txt_folder)

# Tempory Files of Each Parts
lst = unicode.split("###")
n = len(lst)
for i in range(1, n): # on passe la premiere partie (titre)
    #print(lst[i])  
    #print("#"*50)
    output = f"{txt_folder}/{book}_{i}_tmp.txt"
    f = open(output, "w", encoding='utf-8')
    f.write(lst[i])
    f.close()

a =  os.listdir()
print(a)
current_working_directory = os.getcwd()
print(current_working_directory)

input()
print(f"py super_tts_french.py {txt_folder}")
input()
os.system(f"py super_tts_french.py {txt_folder}")
