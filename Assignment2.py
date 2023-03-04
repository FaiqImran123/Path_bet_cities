from stack import *
class CityData:
    def __init__(self,name,outConCount,outCons):
        self.name =name
        self.outConCount =outConCount
        self.outCons =outCons
        self.seen =False
        self.predecessor =-1
    def set_seen(self):
        self.seen =True
    def set_pred(self, ind):
        self.predecessor  =ind
def read_file(f):
    fi =open(f,"r")

    le =fi.readline().rstrip(" ")
    l =[]

    for i in range(int(le)):
        val =fi.readline().rstrip("\n").split(" ")
        name =val[1].rstrip(",")
        count =int(val[2])
        li =[]
        for i in range(3,len(val)):
            li.append(int(val[i]))

        c =CityData(name, count, li)
        l.append(c)
    return l

def search(val):
    s =LinkedStacks()
    st =input("Enter starting city: ")
    
    while True:
        for i in range(len(val)):
            if val[i].name==st:
                break
        if val[i].name==st:
                break

        st =input("Enter Valid Starting City: ")
    d =input("Enter destination city: ")
    while True:
        for i in range(len(val)):
            if val[i].name==d:
                break
        if val[i].name==d:
                break
    for i in range(len(val)):

  
        if val[i].name==st:
        
            s.push(i)
            t =i
            break
    
   
    while s.is_empty()!=True:
        cc =s.pop()

        if val[cc].name==d:
            print("JOB DONE PATH IS FOUND")
            p =[val[cc].name]
            while val[cc].predecessor!=-1:
                cc =val[cc].predecessor
                p.append(val[cc].name)
            
            st =""
            for i in range(len(p)-1,-1,-1):
                if i==0:
                    st +=p[i]
                else:
                    st +=p[i]+"-->"
              
            print(st)
            return






                
                    

        else:
            
           
            outcons =val[cc].outCons
          
           
            for i in range(len(outcons)):
               
                if val[outcons[i]].seen==False:
                   
                    val[outcons[i]].set_seen()
                    val[outcons[i]].set_pred(cc)
            
                    s.push(outcons[i])
                   
            
                


    if s.is_empty()==True:
        print("Empty Path Not found")


def main():
    f =input("Please Enter a file name storing network: ")
    val =read_file(f)

  
    search(val)





main()