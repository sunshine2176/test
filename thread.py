#coding:utf-8

import time  
import threading  
import Queue


def timer(no, interval):  
    global cnt,lock
    
    while cnt<10:  
        #print 'Thread:(%d) Time:%s\n'%(no, time.ctime())  
        time.sleep(interval)  
        #lock.acquire()
        cnt+=1
        #lock.release()   
        print '-----Thread:(%d) is %d' %(no,cnt)
     
    thread.exit() 
    
def time2(no, interval):
    global cnt,lock
    
    while True:  
        #print 'Thread:(%d) Time:%s\n'%(no, time.ctime())  
        time.sleep(interval)  
        #lock.acquire()
        if cnt > 0:
            cnt-=1
        #lock.release()   
        print '-----Thread:(%d) is %d' %(no,cnt)
     
    thread.exit() 
    
def time3(no, interval):
    global cnt,lock
    
    while True:  
        #print 'Thread:(%d) Time:%s\n'%(no, time.ctime())  
        time.sleep(interval)  
        #lock.acquire()
        if cnt > 0:
            cnt-=1
        #lock.release()   
        print '-----Thread:(%d) is %d' %(no,cnt)
     
    thread.exit() 
   
def listDict(no,dd):
    
    print '---' + str(no) +'---',dd['header'],'+++++++'
    
def listQueue():
    s = q.get()
        
    print '------',s['header'],'+++++++'    
   
def test(): #Use thread.start_new_thread() to create 2 new threads  
    thread.start_new_thread(time3, (3,2))
    thread.start_new_thread(timer, (1,1))  
    thread.start_new_thread(time2, (2,2))  
   
if __name__=='__main__':  
    
    q = Queue.Queue(maxsize=2)
    d = {'header':'abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890'}
    q.put(d)
    q.put(d)
    
    l = []
    l.append(d)
    l.append(d)
    
    #for i in range(2):
        
        #t = threading.Thread(target=listQueue,args=()) 
        #t.start()
    index = 1
    for j in l:
        t = threading.Thread(target=listDict,args=(index,j)) 
        t.start() 
        index += 1
      
    while 1:
        pass
