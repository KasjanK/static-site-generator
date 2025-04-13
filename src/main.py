import os
from copystatic import copy_contents

def main():
    copy_contents(os.path.abspath(os.path.expanduser("static")), os.path.abspath(os.path.expanduser("public")))

if __name__ =="__main__":
    main()
