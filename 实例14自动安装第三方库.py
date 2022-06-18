import  os
libs = {"pygame","numpy"}
try:
    for lib in libs:
        os.system("pip install "+ lib)
    print("successful")
except:
    prinit("Failed somehow")
