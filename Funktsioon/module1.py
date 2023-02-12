


#7
def date(d:int,m:int,y:int)->any:
    """
    Määrme date..
    :parem int d,int m, int y:Järjend date numbridest
    :rtype: str
    """




#6
def is_prime(arv:int)->any:
    """
    Määrme is_prime...
    :parem int arv: Järjend is_prime numbridest
    :rtype: str
    """

    for i in range(2,arv):
        if arv%i==0:
            return False

    if arv==1:
        return False

    return True
#5
def bankk(yea:float, a:float)->int:
    """
    Määrme bank....
    :parem float yea, float a: Järjend bank numbridest
    :rtype: str
    """

    vast=a*(1+1/10)**yea
    return vast



    #i=0
    #while i>0:
    #    for i in range(yea):
    #        a*=1.1
    #    return a


    #i=0
    #while i<yea:
    #    a=float(a+a*0.1)
    #    i=i+1
    #return a


#4
def season(m:int)->any:
    """
    Määrme season...
    :parem int m: Järjend season numbridest
    :rtype: str
    """
    if  m in (12,1,2):
        vas= "talv"
    elif m in (3,4,5):
        vas="kevad"
    elif m in (6,7,8):
        vas="suvi"
    elif m in (9,10,11):
        vas="sügis"
    else:
        vas="Viga"
    return vas







#3
def square(tehe:float)->any:
    """
    Määrme square...
    :parem tehe a2: Järjend square numbridest
    :rtype: str
    """
    a = tehe * 4
    b = tehe**2
    c = (tehe * 1.414)//1
    return a,b,c




#2

def  is_year_leap(a1:int)->bool:
    """
    Määrme is_year_leap...
    :parem int a1: Järjend is_year_leap numbridest
    :rtype: str
    """
    if a1%4==0:
         t=True 

    else:
        t= False

    return t
        

       

#1

def arithmetic(a:float,faraon:str, b:float)->any:
    """
    Määrme arithmetic....
    :parem str faraon,float a, float b: Järjend arithmetic numbridest
    :rtype: str
    """
    if faraon=='+':
        vastus= a+b
    elif faraon=="-":
        vastus= a-b
    elif faraon=="*":
        vastus= a*b
    elif faraon=="/":
        if b==0:
            vastus="DIV0"
        else:
            vastus=a/b

    else:
         vastus="Tundmatu tehe"
    return vastus




