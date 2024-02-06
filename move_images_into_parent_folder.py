import os
import shutil

# Function to move images from "images" folder to its parent folder and delete "images" folder
def process_images_folder(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if "images" in dirs:
            images_folder = os.path.join(root, "images")
            parent_folder = os.path.dirname(images_folder)

            # Move image files to parent folder
            for image_file in os.listdir(images_folder):
                image_path = os.path.join(images_folder, image_file)
                destination_path = os.path.join(parent_folder, image_file)
                shutil.move(image_path, destination_path)
                print(f"Moved '{image_file}' from '{images_folder}' to '{parent_folder}'")

            # Remove the now-empty "images" folder
            os.rmdir(images_folder)
            print(f"Deleted empty folder '{images_folder}'")
        else:
            print(f"No 'images' folder found in '{root}'")

# Use the current working directory as the root directory
current_directory = os.getcwd()
process_images_folder(current_directory)

# Print completion message
print("All folders processed. Script completed.")
