import os
import hashlib

def filepath(Hashfile):
    if not os.path.exists(Hashfile):
        print("Check file path")
        return "Wrong"
    elif not os.path.isfile(Hashfile):
        print("Check file path")
        return "Does not exist"
    else:
        return "Exists"

def checkalgorithm(hashtype):
    if hashtype.lower() not in hashlib.algorithms_available:
        print("Invalid hash type")
        return "Wrong Algorithm"
    else:
        return "Accepted"

def calchash(Hashfile, hashtype='sha256'):
    validation = filepath(Hashfile)
    if validation != "Wrong":
        try:
            hashfunc = hashlib.new(hashtype.lower())
            with open(Hashfile, 'rb') as file:
                while chunk := file.read(4096):
                    hashfunc.update(chunk)
            return hashfunc.hexdigest()
        except FileNotFoundError as E:
            print(f"File does not exist {E}")
            return None
        except IOError as E:
            print(f"Error reading file {E}")
            return None
    else:
        return None
    
def kepthash(Hashfile, hashedvalue, hashtxt='hashes.txt'):
    try:
        with open(hashtxt, 'a') as file:
            file.write(f"{hashedvalue} {Hashfile}\n")
        print("Hash saved")
    except IOError as E:
        print(f"Try again {E}")

def comparehashes(Hashfile, storedhash, hashtype='sha256'):
    currenthash = calchash(Hashfile, hashtype)
    if currenthash is None:
        return "Wrong hash"
    elif currenthash == storedhash:  
        return "Correct hash"
    else:
        return "Wrong hash"  
    
def main():
    print("File Hashing Tool")
    
    mode = input("Pick mode (Generate or Compare): ").lower()

    if mode == "generate":
        Hashfile = input("Enter the file path: ")
        validate = filepath(Hashfile)
        if validate == "Exists":
            hashtype = input("Enter the hash type (default is sha256): ")
            hashedvalue = calchash(Hashfile, hashtype)
            if hashedvalue:
                kepthash(Hashfile, hashedvalue)
        else:
            if validate == "Wrong":
                print("Invalid file path.")
            else:
                print("Specified path does not point to a file.")

    elif mode == "compare":
        Hashfile = input("Enter file path: ")
        storedhash = input("Enter the stored hash: ")
        hashtype = input("Enter the hash type (default is sha256): ") 
        
        validate = filepath(Hashfile)
        if validate == "Exists":
            result = comparehashes(Hashfile, storedhash, hashtype)
            print(result)
        else:
            print("Invalid file path.")

    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
