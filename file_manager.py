from os.path import dirname, abspath
import os
import random
import shutil

class File_Manager:
    dir_to_watch = dirname(dirname(abspath(__file__)))

    def file_manage(self):
        
        obj = os.scandir(self.dir_to_watch)
        for entry in obj:
            if entry.is_file():
                print("file created")
                self.file_types(entry)

    
    def file_types(self, file):
        file_name, file_extension = os.path.splitext(file.name)

        if file_extension == '.txt':
            self.tranfer_file(file, 'text');
            return None;
        
        if file_extension == '.doc' or file_extension == '.docx' or file_extension == '.odt' or file_extension == '.pdf':
            self.tranfer_file(file, 'documnetations')
            return None;

        if file_extension == '.img' or file_extension == '.png' or file_extension == '.JPEG' or file_extension == '.svg' or file_extension == '.jpg':
            self.tranfer_file(file, 'images')
            return None;
        
        if file_extension == '.csv':
            self.tranfer_file(file, 'dataSets')
            return None;
        
        self.tranfer_file(file, 'others');

        
    
    def tranfer_file(self, file, dir_name):
        dir_path = os.path.join(self.dir_to_watch, dir_name)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        
        reallocated_file_path = os.path.join(dir_path, file.name)

        if os.path.exists(reallocated_file_path):
            random_num =random.random();
            random_str = str(random_num)
            file_name, file_extension = os.path.splitext(file.name)
            change_name = file_name+random_str+file_extension;
            reallocated_file_path = os.path.join(dir_path,change_name)


        try:
            shutil.copyfile(file.path, reallocated_file_path)
        except:
            print("error occur when copying file");

        try:
            os.remove(file.path)
        except:
            print("error occur when deleting file");
