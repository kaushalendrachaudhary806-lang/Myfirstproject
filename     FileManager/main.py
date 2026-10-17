import os
import shutil

def main():
    while True:
        print("\n1.Create File  2.Create Folder  3.List  4.Delete File  5.Delete Folder  6.Rename  7.Exit")
        ch = input("Enter Choice: ")
        if ch == '1':
            name = input("File name: ")
            open(name, 'w').close()
            print("File Created")
        elif ch == '2':
            name = input("Folder name: ")
            os.mkdir(name)
            print("Folder Created")
        elif ch == '3':
            print(os.listdir())
        elif ch == '4':
            name = input("File to delete: ")
            os.remove(name)
            print("File Deleted")
        elif ch == '5':
            name = input("Folder to delete: ")
            shutil.rmtree(name)
            print("Folder Deleted")
        elif ch == '6':
            old = input("Old Name: ")
            new = input("New Name: ")
            os.rename(old, new)
            print("Renamed")
        elif ch == '7':
            break

main()