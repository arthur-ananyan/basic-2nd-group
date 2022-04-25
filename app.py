class FileManager():
    def __init__(self, filename, mode):
        print("init method")
        self.filename = filename
        self.mode = mode
        self.file = None
          
    def __enter__(self):
        print("enter method")
        self.file = open(self.filename, self.mode)
        return self.file
      
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("close method")
        self.file.close()


for i in range(100):

	with FileManager('t.txt', 'a') as f:
		f.write('Test')
  
print(f.closed)