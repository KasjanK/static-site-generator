import os, sys
from generatepage import generate_pages_recursive
from copystatic import copy_contents

basepath = "/"
if len(sys.argv) > 1:
    basepath = sys.argv[1]

def main():
    copy_contents(os.path.abspath(os.path.expanduser("static")), os.path.abspath(os.path.expanduser("docs")))
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

if __name__ =="__main__":
    main()
