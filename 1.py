import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dst_dir):
    try:
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
            print(f"Created directory: {dst_dir}")
        
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            if os.path.isdir(src_path):
                print(f"Entering directory: {src_path}")
                copy_and_sort_files(src_path, dst_dir)
            else:
                file_ext = os.path.splitext(item)[1][1:] or 'no_extension'
                ext_dir = os.path.join(dst_dir, file_ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                    print(f"Created directory for extension {file_ext}: {ext_dir}")
                shutil.copy2(src_path, ext_dir)
                print(f"Copied {src_path} to {ext_dir}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursively copy files and sort them into subdirectories based on file extensions.")
    parser.add_argument("source", help="Path to the source directory")
    parser.add_argument("destination", nargs='?', default="dist", help="Path to the destination directory (default: 'dist')")
    args = parser.parse_args()
    
    src_dir = args.source
    dst_dir = args.destination

    if not os.path.isdir(src_dir):
        print(f"Source directory {src_dir} does not exist.")
        return
    
    copy_and_sort_files(src_dir, dst_dir)
    print(f"Files from {src_dir} have been copied to {dst_dir} and sorted by file extension.")

if __name__ == "__main__":
    main()
