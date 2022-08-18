import argparse
import os
import sys
import shutil

def GetSubFolderNamesByPath(rootDir):
    folderArray = []

    for root, folders, files in os.walk(rootDir, topdown=False):
        for name in folders:
            folderArray.append(os.path.join(root, name))
    return folderArray

def main():
    folderarray = GetSubFolderNamesByPath(os.path.abspath(os.path.join(os.getcwd())))

    for folder in folderarray:
        print("%s"%folder)
        key,value  = os.path.split(folder)
        shortname = value.split('-')
        if len(shortname) > 1:
            print("%s %s %s" % (key,value,shortname[len(shortname)-1]))
            dst = "%s\\%s" % (key,shortname[len(shortname)-1])
            print("%s"%dst)
            os.rename(folder,dst)

if __name__ == "__main__":
   main()
