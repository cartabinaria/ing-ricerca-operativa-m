import os

def rename_files():
    # Get all files in current directory
    files = os.listdir(".")

    for filename in files:
        # Skip directories
        if not os.path.isfile(filename):
            continue

        # Check if 'svolto' is in filename
        if "svolto" in filename:
            new_name = filename.replace("svolto", "soluzione-svolto")

            # Rename file
            os.rename(filename, new_name)
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    rename_files()