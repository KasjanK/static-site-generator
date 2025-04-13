import os
import shutil

def copy_contents(src, dest):
    destination_dir = os.path.abspath(os.path.expanduser(dest))
    source_dir = os.path.abspath(os.path.expanduser(src))
    
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)
        print(f"public wasnt found, created.")
    else:
        if os.listdir(destination_dir):
            for root, dirs, files in os.walk(destination_dir, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))
    
    source_items = os.listdir(source_dir)

    for item in source_items:
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)

        if os.path.isdir(source_item):
            copy_contents(source_item, destination_item)
        else:
            print('Copying: {}'.format(repr(source_item)))
            shutil.copy(source_item, destination_item)
            
def main():
    copy_contents(os.path.abspath(os.path.expanduser("static")), os.path.abspath(os.path.expanduser("public")))

if __name__ =="__main__":
    main()
