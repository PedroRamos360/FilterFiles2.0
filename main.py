import os


def get_file_type(file):
   filename = file.split(".")
   return filename[-1]


def move_file(filename, original_path, new_path):
   file_moved = False

   src = original_path + '/' + filename
   new_destination = new_path + '/' + filename
   while not file_moved:
      try:
         os.rename(src, new_destination)
         file_moved = True
      except FileExistsError:
         filename = '(new)' + filename
         new_destination = new_path + '/' + filename


def filter_all_files(folder_path):
   for filename in os.listdir(folder_path):
      path_to_file = "{}/{}".format(folder_path, filename)

      if not os.path.isdir(path_to_file):
         try:
            os.mkdir('{}/.{}'.format(folder_path, get_file_type(filename)))
         except FileExistsError:
            pass
         move_file(filename, folder_path, '{}/.{}'.format(folder_path, get_file_type(filename)))

   print("Files moved sucessfully!")


folder_path = input("Type the folder location: ")
try:
   filter_all_files(folder_path)
   input("All files moved successfully!")
except Exception as err:
   input("An error occurred while trying to move your files: {}".format(err))