import os
import fnmatch
 
# Get a list of all files in directory
for rootDir, subdirs, filenames in os.walk('..'):
    # Find the files that matches the given patterm
    for filename in fnmatch.filter(filenames, '*.js'):
        try:
            os.remove(os.path.join(rootDir, filename))
        except OSError:
            print("Error while deleting file")