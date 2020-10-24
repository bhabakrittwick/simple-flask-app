import os
def updatedb():
    os.chdir('/home/rayan13/mysite/')
    os.system('git add new.txt')
    os.system('git commit -m "new update"')
    os.system('git push')

if __name__=="__main__":
    updatedb()