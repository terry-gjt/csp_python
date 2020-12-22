# 没做完 等系统放出题目了再优化一下
def NewFile(profolder,filename,size):
    
    print()
def NewFolder(propath,foldername):
    propath[5][foldername]=[0,0,0,0,propath,{},{}]

def changesize(pathlist,size):
    dangqiangpath = root
    for i in range(len(pathlist)-1):
        dangqiangpath['houdaiuse/']+=size
        dangqiangpath=dangqiangpath[pathlist[i]]

def create(pathlist,size):

    dangqiangpath=root
    for i in range(len(pathlist)-1):
        if dangqiangpath['houdai/']==0 or dangqiangpath['houdai/']>=size+dangqiangpath['houdaiuse/']:
            if pathlist[i] in dangqiangpath:
                dangqiangpath=dangqiangpath[pathlist[i]]
            else:
                dangqiangpath[pathlist[i]]={'mulu/':0,'houdai/':0,'muluuse/':0,'houdaiuse/':0}
        else:
            print('N')
            return
    wenjian=pathlist[len(pathlist)-1]
    if wenjian in dangqiangpath:
        print('N')
    elif wenjian+'/' in dangqiangpath:
        yuansize=dangqiangpath[wenjian+'/']
        dangqiangpath[wenjian+'/']=size
        changesize(pathlist,size-yuansize)
        print('Y')
    else:
        dangqiangpath[wenjian + '/'] = size
        changesize(pathlist, size)
        print('Y')

def remove(pathlist):
    dangqiangpath = root
    size=0
    for i in range(len(pathlist) - 1):
        dangqiangpath = dangqiangpath[pathlist[i]]
    wenjian = pathlist[len(pathlist) - 1]
    if wenjian in dangqiangpath:
        dangqiangpath.pop(wenjian)
    print('Y')
def q(pathlist,ld,lr):
    print()
def st3():
    n=int(input())
    for i in range(n):
        lista=input().split()
        if lista[1][0] != '/':
            print('N')
            break
        pathlist = lista[1][1:].split('/')
        if '' in pathlist:
            print('N')
            break
        if lista[0]=='C':
            create(pathlist,lista[2])
        elif lista[0]=='R':
            remove(pathlist)
        elif lista[0]=='Q':
            q(pathlist,lista[2],lista[3])

root= [0,0,0,0,None,{},{}]
st3()