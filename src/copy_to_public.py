import os
import shutil

def copy_static():
    if os.path.exists("./public"):
        for item in os.listdir("./public"):
            item_path = os.path.join("./public", item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                    print(f"Removing file: {item_path}")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"Removing directory tree {item_path}")
            except Exception as e:
                print(f"Failed to delete {item_path}. Reason {e}")
    else:
    # Create public folder if it doesn't exist
        os.makedirs("./public")

    #TODO: Copy contents from static to public folder.
    if os.path.exists("./static"):
        for item in os.listdir("./static"):
            source_path = os.path.join("./static", item)
            dest_path = os.path.join("./public", item)

            if os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path)
            else:
                shutil.copy2(source_path, dest_path)
            print("Successfully syncronized public folder")
    else:
        print("Error: Static directory ./static does not exist")



