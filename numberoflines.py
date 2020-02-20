import os,sys

def count(dir, filetype,exclude, counter=0):
    for root, dirs, files  in os.walk(dir):
        dirs[:] = [d for d in dirs if d not in exclude]
        for f in files:
            if f.endswith(filetype):
                file=root+"\\"+f
                try:
                    counter += len(open(file).readlines())
                except:
                    print (file)
    return dir + " : " + str(counter) + " lines"

print(count("D:\\projects\\krg\\Alexa Server Azure",
            ".ts",
            [".git","node_modules"]))