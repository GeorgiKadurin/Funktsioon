def square(tehe:float)->any:
    """
    Määrme square...
    :parem tehe a2: Järjend square numbridest
    :rtype: str
    """
    tehe=a*4










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




