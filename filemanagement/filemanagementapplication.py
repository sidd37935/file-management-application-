import os

def create_file(filename):
    try:
        with open(filename,"x") as f:
            print(f"filename {filename}: created sucessfully!")
    except FileExistsError:
        print(f"file name{filename} already exists!")

    except Exception as E:
        print("an eror occured!")

def view_all_files():
    files = os.listdir()
    if not files:
        print("no file found!")
    else:
        print(f"files in directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted sucessfully!")
    except FileNotFoundError:
        print("file not found!")
    except Exception as e:
        print("an eoor occured!")

def read_files(filename):
        try:
            with open("sample.txt","r") as f:
                content = f.read()
                print(f"content of '{filename}' : \n {content}")

        except FileNotFoundError:
            print(f"{filename} doesn't exist!")
        except Exception as e:
            print("an error occured")
def edit_file(filename):
    try:
        with open("sample.txt","a") as f:
            content = input("enter the data to add=")
            f.write(content + "\n")
            print("content added to {filename}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print("an error occured!")

def main():
        while True:
            print("FILE MANAGEMENT APP")
            print("1:create file")
            print("2:view all file")
            print("3:delete file")
            print("4:read file")
            print("5:edit file")
            print("6:exit")
            print("1:")
            choice = input("enter your choice (1-6) =")

            if choice == "1":
                filename = input("enter the filename to create =")
                create_file(filename)
            elif choice == "2":
                view_all_files()
            elif choice == "3":
                filename = input("enter the file you want to delete =")
                delete_file(filename)
            elif choice == "4": 
                filename = input("enter the filename to read = ")
                read_files(filename)
            elif choice == "5":
                filename=input("enter the file to edit=")
                edit_file(filename)
            elif choice == "6":
                print("closing the app..")
                break
            else:
                print("invalid syntax")

if __name__ =="__main__":
    main()
