Heelo there here is a break down of what of code does, 

import os
#This makes a way for the code to interract with the operating system

import hashlib
#This imports the hashing algorithms 

def filepath(Hashfile):
    if not os.path.exists(Hashfile):
        print("Check file path")
        return "Wrong"
    elif not os.path.isfile(Hashfile):
        print("Check file path")
        return "Does not exist"
    else:
        return "Exists"
#Here I wrote a function that checks if for the file path 

def checkalgorithm(hashtype):
    if hashtype.lower() not in hashlib.algorithms_available:
        print("Invalid hash type")
        return "Wrong Algorithm"
    else:
        return "Accepted"
#This checks if the hasg type provided is part of the variosu hashing versions 

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
#i stored the hash value default as sha256 and genaretes a hash vale for the file 

def kepthash(Hashfile, hashedvalue, hashtxt='hashes.txt'):
    try:
        with open(hashtxt, 'a') as file:
            file.write(f"{hashedvalue} {Hashfile}\n")
        print("Hash saved")
    except IOError as E:
        print(f"Try again {E}")
#Writes the hased vale and saves it to a file called hashes.txt

def comparehashes(Hashfile, storedhash, hashtype='sha256'):
    currenthash = calchash(Hashfile, hashtype)
    if currenthash is None:
        return "Wrong hash"
    elif currenthash == storedhash:  
        return "Correct hash"
    else:
        return "Wrong hash"
#This takes the hash vale and the hashed file and compaires them

def main():
    print("File Hashing Tool")
    
    mode = input("Pick mode (Generate or Compare): ").lower()

    if mode == "generate":
        Hashfile = input("Enter the file path: ")
        validate = filepath(Hashfile)...
#This is the main function that takes the input form the user 
