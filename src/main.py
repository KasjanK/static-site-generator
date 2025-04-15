import os
from generatepage import generate_pages_recursive
from copystatic import copy_contents

def main():
    copy_contents(os.path.abspath(os.path.expanduser("static")), os.path.abspath(os.path.expanduser("public")))
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ =="__main__":
    main()
