import os
import shutil

def copy_pdfs_to_main_folder(main_folder):
    for root, dirs, files in os.walk(main_folder):
        if root != main_folder:
            for file in files:
                if file.endswith('.pdf'):
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(main_folder, file)
                    shutil.copy2(src_file, dst_file)
                    print(f"Copied {src_file} to {dst_file}")

main_folder = f"D:\Vishal"
copy_pdfs_to_main_folder(main_folder)
