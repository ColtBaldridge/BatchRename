import os
from pathlib import Path
from PyPDF2 import PdfFileReader

def reset(src, dst):
    # os.system('')
    pass

def missed_files(file, error):
    pass

# This is the working directory.
# Replace this with the directory where the documents are stored.
directory = 'C:\\Users\\username\\git\\batch-rename\\documents'

# Keep track of files with no title in the metadata.
# Notify the user that they must manually edit these documents.
changed_files = []
missed_files = []

os.mkdir('missed-files')

# Change the working directory to one with the files.
os.chdir(directory)

for article in os.listdir():
    # filepath = os.path.join(directory, article)
    with open(article, 'rb') as f:
        # print(f'Selecting file: {article}')
        try:
            metadata = PdfFileReader(f).getDocumentInfo()
        except:
            print(f'An unknown error occured: {article}')
            missed_files.append(article)
            continue
        # A PDF's metadata may not include a title.
        # Record the incident and continue the loop.
        try:
            title = metadata['/Title']
        except KeyError:
            print(f'Title metadata not found: {article}')
            missed_files.append(article)
            continue
        
        # Check if the title metadata exists.
        # If it does not, add it to the missed files list and move on.
    if title == '' or None:
        print(f'Title metadata is blank: {article}')
        missed_files.append(article)
        continue
    else:
        # Create a file path for the actual PDF title.
        title += '.pdf'
        # Repalce colons with dashes for Windows file compatability
        title = title.replace(':', ' -')
        # new_filepath = os.path.join(directory, metadata['/Title'] + '.pdf')
        os.rename(article, title)
        changed_files.append(title)

# Once the script is complete, show which documetns need manual edits.
print('\n-----------------------------------------------------------------\n')
print('Batch title edit complete.')
print('The script could not edit the follwoing documents:')
for file in missed_files:
    print(file)

for file in missed_files:
    os.system(f'move \"{file}\" {directory}\missed-files')
