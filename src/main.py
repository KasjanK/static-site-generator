import os
from generatepage import generate_page
from copystatic import copy_contents

def main():
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    copy_contents(os.path.abspath(os.path.expanduser("static")), os.path.abspath(os.path.expanduser("public")))


if __name__ =="__main__":
    main()
