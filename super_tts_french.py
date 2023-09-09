import os, shutil, re, sys


#--- Usage
if len(sys.argv) < 2:
    print('Usage: super_tts_french.py source_folder', \
          file=sys.stderr)
    print('Example: ', file=sys.stderr)
    print('py super_tts_french.py poesie_a/', file=sys.stderr)
    sys.exit()


#--- Options
source_folder = sys.argv[1] # source_folder


# Folder's name has to finish with the symbol "/"
if not source_folder.endswith("/"):
    source_folder = source_folder + "/"

print("Source Folder:", source_folder)


# Generation of a list contenaing the text source (of extension ".txt")
text_sources = []
entries = os.listdir(source_folder)
for entry in entries:
        match = re.search("\.txt$", entry)
        if match:
            text_sources.append(entry)


#--- Target folder
target_folder = source_folder.replace("/", "_")
target_folder = target_folder+"_mp3/"

print("Target Folder:", target_folder)

# One erases the folder if it already exists
if os.path.exists(target_folder):
    shutil.rmtree(target_folder)

# Make directory target_folder
os.mkdir(target_folder)

# One places itsef in into directory target_folder        
os.chdir(target_folder)

for entry in text_sources:
    input_file = "../" + source_folder + entry
    os.system(f"py ../tts_french.py -name julie {input_file}")
    output_file = input_file.replace(".txt", ".mp3")
    shutil.move(output_file, ".")

