rem *** Used to create a Python exe 

rem ***** get rid of all the old files in the dist folder
rd /S /Q dist

rem ***** create the exe
rem C:\Python38\Scripts\pyinstaller --onefile --upx-dir C:\Programming\upx-3.96-win64\ -n Farbenfall src/main.py
rem C:\Python38\Scripts\pyinstaller --onefile -w -n Farbenfall src/main.py
C:\Python38\python.exe -OO -m PyInstaller --onefile -w -n Farbenfall --icon icon.ico src/main.py
rem C:\Python38\python.exe -OO -m PyInstaller -w -n Farbenfall --icon icon.ico src/main.py

rem with pyInstaller there is a parameter --upx-dir but that doesn't work with pygame atm
C:\Programming\upx-3.96-win64\upx.exe .\dist\Farbenfall.exe

rem ***** Copy the static files that are needed like images and audio
xcopy /s/y/i .\data .\dist\data
rem xcopy /s/y/i .\data .\dist\Farbenfall\data

rem **** pause so we can see the exit codes
pause "done...hit a key to exit"