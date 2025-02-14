from file import File
from folder import Folder

try:
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")
    file4 = File("file4.txt")
    file5 = File("file5.txt")
    file6 = File("file6.txt")

    folder1 = Folder("folder1")
    folder2 = Folder("folder2")
    folder3 = Folder("folder3")

    folder1.add(file1)
    folder1.add(file5)
    folder1.add(file6)
    folder2.add(file2)
    folder3.add(file3)

    folder1.add(folder2)
    folder2.add(folder3)

    folder1.showDetails()
    folder2.showDetails()
    folder3.showDetails()
except Exception as e:
    print(e)