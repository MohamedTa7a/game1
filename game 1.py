board =[00,10,20,30,40,50,60,70,80,90]

def box() :
    print 
    print '|', board [1],'|',board[2],'|',board[3],'|'
    print '____________________'
    print '|', board [4],'|',board[5],'|',board[6],'|'
    print '____________________'
    print '|', board [7],'|',board[8],'|',board[9],'|'


p=1  
spt=[]
number=[]

box()
while p<10:
    while True:
        y=int(input("enter a spt : " ))
        if y in spt :
            print("the spt is selected")
        else:
            spt.append(y)
            break
    if p%2==0:
        while True:
            x=int(input("choose an odd between 1 and 9 : "))
            if x%2==1 and x<10 and x not in number:
                number.append(x)
                board[y]=x
                box()
                if board[1] +board[4] +board[7] ==15 or board[1]+board[2]+board[3] ==15 or board[2]+board[5]+board[8]==15 or board[4]+board[5]+board[6]==15 or board[6]+board[3]+board[9]==15 or board[9]+board[8]+board[7]==15:
                    print(" player (1) is win")
                    p=10
                break
            else:
                print("not avilabale ")
                  
    if p%2==1:
          while True:
            x=int(input("enter even between 0 and 8 : " ))
            if x%2==0 and x<10 and x not in number:
                number.append(x)
                board[y]=x
                box()
                if board[1] +board[4] +board[7] ==15 or board[1]+board[2]+board[3] ==15 or board[2]+board[5]+board[8]==15 or board[4]+board[5]+board[6]==15 or board[6]+board[3]+board[9]==15 or board[9]+board[8]+board[7]==15:
                    print("player (2) is win")
                    p=10
                break
            else:
                print("not avilabal")
                        
                  
    p+=1
    if p==9:
        print("Draw")              
                        
              
                
                
                  
                  
                 
                  
                
                
                
                 
                 
                 
                  
                 
                 
                 
                
                            
