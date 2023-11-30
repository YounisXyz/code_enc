import os, sys
os.system("git pull")
try:
    __import__("Enc").code_enc()
except Exception as e:
    exit(str(e))
 
