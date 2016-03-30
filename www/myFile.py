#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#创建文件，并写入
# fileHandle = open('test.txt','w') 
# fileHandle.write ('This is a test\nReally,it is.')
# fileHandle.close()


#读取文件
# fileHandle1 = open('test.txt')
# # fileList = fileHandle1.readlines()
# # for fileLine in fileList:
# # 	print (fileLine)
# #fileHandle1.write('\n\nBottom line')
# print (fileHandle1.readlines())
# fileHandle1.close()

#追加输入
# fileHandle1 = open('test.txt','a')
# fileHandle1.write('\n\nBottom line')
# fileHandle1.close()

#读取文件的属性
# import os  
# import stat  
# import time
  
# fileStats = os.stat ( 'test.txt' )  
# fileInfo = {  
#     'Size' : fileStats [ stat.ST_SIZE ],  
#     'LastModified' : time.ctime ( fileStats [ stat.ST_MTIME ] ),  
#     'LastAccessed' : time.ctime ( fileStats [ stat.ST_ATIME ] ),  
#     'CreationTime' : time.ctime ( fileStats [ stat.ST_CTIME ] ),  
#     'Mode' : fileStats [ stat.ST_MODE ]  
# }  

# for infoField,infoValue in fileInfo.items():  
#     print (infoField + ':' + str(infoValue))
# if stat.S_ISDIR ( fileStats [ stat.ST_MODE ] ):  
#     print ('Directory. ' )
# else:  
#     print ('Non-directory.' )

#也可os.path获取基本信息

#StringIO 在内存创建虚拟文件

#模块化编组  序列化
# import pickle 
# fileHandle = open ('pickleFile.txt', 'wb') 
# testList = [ 'This', 2, 'is', 1, 'a', 0, 'test.' ] 
# pickle.dump(testList, fileHandle) 
# fileHandle.close() 

#模块化编组  反持久化
import pickle 
fileHandle = open ('pickleFile.txt','rb')
testList = pickle.load(fileHandle)
for ite in testList:
	print (ite)
fileHandle.close() 