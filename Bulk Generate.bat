@echo off
REM Create a TXT file with a list of names (one name per line) and then drag and drop that TXT file onto this BAT file

for /F "usebackq tokens=*" %%A in (%1) do (
python DIMNameGen.py -n "%%A"
)
ren output "%~n1"
pause