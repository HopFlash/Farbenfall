from distutils.core import setup
import py2exe

import os

# TODO: feature for file patterns
def collectDataFiles(dataPath='img', dir='./img', recursive=True):
    allDataFiles = []

    absPath = os.path.abspath(dir)
    for filename in os.listdir(dir):
        absFilename = os.path.join(absPath, filename)
        if os.path.isfile(absFilename):
            newFileTuple = dataPath, [absFilename]
            allDataFiles.append(newFileTuple)
        else:
            if recursive:
                subdir = absFilename
                newDataPath = os.path.join(dataPath, filename)
                allDataFiles = allDataFiles + collectDataFiles(newDataPath, subdir, True)
    return allDataFiles

# collection all files from "img" into the dist
datafiles = collectDataFiles('data', './data', True)

# print(datafiles)

setup(
    windows=[
        {
            'script': './src/main.py',
            "icon_resources": [(0, "icon.ico")],
            "dest_base" : 'Farbenfall'
        }
    ],
    # including this line we get one big exe and no library.zip
    # zipfile=None,
    data_files=datafiles,
    options={
        'py2exe': {
            #'includes': ['OpenGL', 'Queue', 'numpy'],
            #  excluding tkinter is necessary for bundle_files = 1
#            'excludes': ['tkinter'],
            # excluding doctest, pdb, unittest, difflib and inspect is a tip from "http://www.py2exe.org/index.cgi/OptimizingSize" because they are big not necessary modules
#            'excludes': ['tkinter', 'doctest', 'pdb', 'unittest', 'difflib', 'inspect'],
            'excludes': ['tkinter', 'doctest', 'pdb', 'unittest', 'difflib', 'inspect', 'OpenGL', 'Queue', 'numpy'],
            'optimize': 2,
            'compressed': True,
            'bundle_files': 3
        }
    }
    )
