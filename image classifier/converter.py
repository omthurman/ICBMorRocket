import os
from PIL import Image
import shutil 

def convert_to_jpg(file_path, output_directory):
    img = Image.open(file_path)
    file_name, _ = os.path.splitext(os.path.basename(file_path))
    jpg_file_path = os.path.join(output_directory, f"{file_name}.jpg")
    img.convert('RGB').save(jpg_file_path)
    return file_name

def convert_images_in_directory(input_directory, output_directory):
    supported_extensions = ('.webp', '.avif', '.png')

    for root, _, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1]
            if file_extension in supported_extensions:
                try:
                    file_name=convert_to_jpg(file_path, output_directory)
                    print(f"Converted {file_path} to {output_directory}/{file_name}.jpg")
                except Exception as e:
                    print(f"Failed to convert {file_path}: {e}")




def move_jpg_files(input_directory, output_directory):

    # Iterate over all files in the input directory
    for file_name in os.listdir(input_directory):
        # Check if the file is a jpg
        if file_name.endswith(".jpg"):
            # Construct the full path of the file
            file_path = os.path.join(input_directory, file_name)

            # Move the file to the output directory
            try:
                shutil.move(file_path, output_directory)
            except:
                print(f"Failed to move {file_path} to {output_directory}")

def main():
    input_directory = r"D:\Alpine Wave\scraper\missile"
    output_directory = r"D:\Alpine Wave\scraper\missile\jpg"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    if os.path.exists(input_directory) and os.path.exists(output_directory):
        convert_images_in_directory(input_directory, output_directory)
        print("\nAll supported images have been converted to .jpg format.")

        move_jpg_files(input_directory, output_directory)
    else:
        print("Invalid directory path(s). Please check the path(s) and try again.")




if __name__ == "__main__":
    main()