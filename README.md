# DIM Name Gen
A utility to generate Bandai Vital Bracelet compatible name sprites

Usage: DIMNameGen.exe [-h] [-n NAME]

Running the utility by itself will bring up a prompt to type a name. The name will be saved into an output folder.
Passing the argument -n followed by a name in quotations will generate that name without the interactive prompt.

Included in the repo is an example batch file for bulk creating sprites. Create a TXT file with the names you want, one per line, then drag and drop the TXT file onto the BAT file. It will generate all the names in the TXT and name the folder the same as the TXT filename. 

This utility was written in python and converted to stand-alone executable with Nuitka.
