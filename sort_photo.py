import os, time, shutil

class Sorting:
    
''' Sort photos by month and years'''

    def path(self):
        self.path = input('Enter the path to sort photos: ')
        self.path_normal = os.path.normpath(self.path)
        self.count = 0

    def processing(self):
        for pathes, names, files in os.walk(self.path_normal):
            print(pathes, names, files)
            for file in files:
                self.count += 1
                full_path = os.path.join(pathes, file)
                secs = os.path.getmtime(full_path)
                file_time = time.gmtime(secs)
                print(full_path, file_time[:2])
                os.makedirs(self.path_normal + '\\' + str(file_time[0]) + '\\' + str(file_time[1]), exist_ok=True)
                path2 = self.path_normal + '\\' + str(file_time[0]) + '\\' + str(file_time[1])
                shutil.copy2(self.path + '\\' + file, path2 + '\\' + file)
        print('Copied files: ', self.count // 2)

sum = Sorting()
sum.path()
sum.processing()
