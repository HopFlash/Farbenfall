rem *** Used to create a Python exe 

rem ***** get rid of all the old files in the dist folder
rd /S /Q dist

rem ***** create the exe
C:\Python38\python -OO setup.py py2exe

rem ***** we use UPX to compress the exe
C:\Programming\upx-3.96-win64\upx.exe .\dist\Farbenfall.exe

rem **** pause so we can see the exit codes
pause "done...hit a key to exit"