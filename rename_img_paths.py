#Libraries that you import
import os
import argparse
#
# Classes you build



# Methods you build

def rename_files(folder_name, renaming_class):

    counter = 0

    for file_path in os.listdir(folder_name):

        if not file_path.startswith('.'):
            counter += 1
            # for example dog + 1 + .jpeg
            extension = os.path.splitext(file_path)[-1]
            new_file_path = os.path.join(folder_name, renaming_class + str(counter) + extension)

            source_file_path = os.path.join(folder_name, file_path)
            destination_file_path = new_file_path

            os.rename(source_file_path, destination_file_path)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Rename image paths")
    parser.add_argument("--folder_imgs", dest = "folder_imgs", required = True, help = "please give the name of where you stored the images")
    parser.add_argument("--renaming_class", dest = "renaming_class", required = True, help = "give name of the class")

    args = parser.parse_args()
    folder_name = args.folder_imgs
    renamed_class = args.renaming_class

    rename_files(folder_name = folder_name, renaming_class = renamed_class)
    print("Finished Renaming")
