import sys
import os
import pypandoc

def callPandoc(fileName):
    try:
        options = ['--template=humanist']
        options += ['-N']
        options += ['--pdf-engine=xelatex']
        pypandoc.convert_file(fileName, to='pdf', extra_args=options, outputfile=fileName[:-3] + ".pdf")
        # os.startfile(fileName + ".pdf")
    except(RuntimeError):
        print("ERROR: pandoc runtime error")

if __name__ == "__main__":
    try:
        fileNameArray = os.path.splitext(sys.argv[1])
        fileName = fileNameArray[0]
        fileExtension = fileNameArray[1]
        callPandoc(fileName, fileExtension)
    except IndexError:
        print("ERROR: no input given")
