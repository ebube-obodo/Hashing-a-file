import os
#This allows the code to interact with the operating system.

import hashlib
#This imports various hashing algorithms.

def filepath(Hashfile):
    if not os.path.exists(Hashfile):
        print("Check file path")
        return "Wrong"
    elif not os.path.isfile(Hashfile):
        print("Check file path")
        return "Does not exist"
    else:
        return "Exists"
#This function checks for the file path validity.

def checkalgorithm(hashtype):
    if hashtype.lower() not in hashlib.algorithms_available:
        print("Invalid hash type")
        return "Wrong Algorithm"
    else:
        return "Accepted"
#This function verifies if the provided hash type is available among the various hashing versions.

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
#The hash value is stored by default as sha256 and generates a hash value for the file.

def kepthash(Hashfile, hashedvalue, hashtxt='hashes.txt'):
    try:
        with open(hashtxt, 'a') as file:
            file.write(f"{hashedvalue} {Hashfile}\n")
        print("Hash saved")
    except IOError as E:
        print(f"Try again {E}")
#Writes the hashed value and saves it to a file called hashes.txt.

def comparehashes(Hashfile, storedhash, hashtype='sha256'):
    currenthash = calchash(Hashfile, hashtype)
    if currenthash is None:
        return "Wrong hash"
    elif currenthash == storedhash:  
        return "Correct hash"
    else:
        return "Wrong hash"
#Compares the hash value with the hashed file and compares them.

def main():
    print("File Hashing Tool")
    
    mode = input("Pick mode (Generate or Compare): ").lower()

    if mode == "generate":
        Hashfile = input("Enter the file path: ")
        validate = filepath(Hashfile)...
#The main function receives input from the user.



