import nbformat as nbf
from glob import glob

files = glob('./*.ipynb')
for ifile in files:
    ntbk = nbf.read(ifile, nbf.NO_CONVERT)
