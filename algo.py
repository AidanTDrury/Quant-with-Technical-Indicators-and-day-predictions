import math
import csv
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web
import matplotlib.animation as animation
import urllib
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

PClose=[]
print("Input the Symbol of the company")
symbol=input()

def start():
    print("Enter the year you would like to use")
    Y=int(input())
    print("Enter the month you would like to use")
    M=int(input())
    print("Enter the day you would like to use")
    D=int(input())

    start = datetime.datetime(Y,M,D)
    end = datetime.datetime.now()
    df = web.DataReader(symbol, "morningstar", start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df = df.drop("Symbol", axis=1)
    df.to_csv(symbol+".csv")

    pred()

def pred():
    global Mx1,Mx2,Mx3,Max,Mn1,Mn2,Mn3,Min,Mean
    df=pd.read_csv(symbol+'.csv')#,parse_dates=True,index_col=0)
    Date=df['Date']
    Close=df['Close']
    Open=df['Open']
    High=df['High']
    Low=df['Low']
    Volume=df['Volume']
    Am=len(Date)
    print(Am)
    Am=Am-1
    count=0
    failsA=0
    failsD=0
    PClose.append(Close[0])
    while count<Am:
        print("\n------------------------------------------------")
        print("The count is:",count)
        num=count
        num2=count+1
        count=count+1
        C=Close[num2]
        O=Open[num]
        G=C/O
        P=G*C
        A=Close[num2]-Close[num]
        B=P-Close[num]
        if(A>0 and B>0) or (A<0 and B<0):
            R=str(1)
        else:
            R=str(0)
            failsD=failsD+1
        Ap=100*(P/Open[num2])
        if Ap<80:
            N=str('R')
            failsA=failsA+1
        else:
            N=str('G')
        print("Date     | Close")
        print(num,Date[num],Close[num],'|--|',Date[num2],"("+R+")","    Accuracry:",Ap)
        print(num2,Date[num2],Close[num2],"|--|",P,"  ",N)
        PClose.append(P)

    print("\n------------------------------------------------")
    print("Finished")
    print("Review")
    print("Directional fails:",failsD,"Accuracy fails:",failsA)
    Dpe=(failsD/Am)*100
    Ape=(failsA/Am)*100
    print("Percentage of directional fails:",Dpe,"%")
    print("Percentage of accuracy fails:",Ape,"%")

    SortedPClose=sorted(PClose)
    Amt=len(SortedPClose)-1
    
    Mn1=SortedPClose[0]
    Mn2=SortedPClose[1]
    Mn3=SortedPClose[2]
    Mn4=SortedPClose[3]
    Mn5=SortedPClose[4]
    Mn6=SortedPClose[5]
    Mn7=SortedPClose[6]
    Mn8=SortedPClose[7]
    Mn9=SortedPClose[8]
    Mn10=SortedPClose[9]

    Mx1=SortedPClose[Amt]
    Mx2=SortedPClose[Amt-1]
    Mx3=SortedPClose[Amt-2]
    Mx4=SortedPClose[Amt-3]
    Mx5=SortedPClose[Amt-4]
    Mx6=SortedPClose[Amt-5]
    Mx7=SortedPClose[Amt-6]
    Mx8=SortedPClose[Amt-7]
    Mx9=SortedPClose[Amt-8]
    Mx10=SortedPClose[Amt-9]

    Max=(Mx1+Mx2+Mx3)/3
    Min=(Mn1+Mn2+Mn3)/3
    Mean=(Max+Min)/2

    Amt=Amt+1
    TLMax=[]
    N=0
    X1=PClose.index(Mx1)
    X2=PClose.index(Mx2)
    m=(Mx1-Mx2)/(X1-X2)
    Y=Mx1
    X=PClose.index(Mx1)
    C=Y-m*X

    while N<Amt:
        Y=m*N+C
        N=N+1
        TLMax.append(Y)

    TLMin=[]
    N=0
    X1=PClose.index(Mn1)
    X2=PClose.index(Mn2)
    X3=PClose.index(Mn3)
    X4=PClose.index(Mn4)
    X5=PClose.index(Mn5)
    X6=PClose.index(Mn6)
    X7=PClose.index(Mn7)
    X8=PClose.index(Mn8)
    X9=PClose.index(Mn9)
    X10=PClose.index(Mn10)
    m1=(Mn1-Mn2)/(X1-X2)
    m2=(Mn3-Mn4)/(X3-X4)
    m3=(Mn5-Mn6)/(X5-X6)
    m4=(Mn7-Mn8)/(X7-X8)
    #m5=(Mn9-Mn10)/(X9-X10)
    m=(m1+m2+m3+m4)/8
    Y=Mn1
    X=PClose.index(Mn1)
    C=Y-m*X

    while N<Amt:
        Y=m*N+C
        N=N+1
        TLMin.append(Y)

    LP=[]

    N=0
    while N<Amt:
        Amn=len(PClose)-1
        LastPrice=PClose[Amn]
        LP.append(LastPrice)
        N=N+1

    N=0
    num=0
    num2=1
    Nu=0
    Nd=0
    Ns=0
    UR=[]
    DR=[]
    SR=[]
    while N<Amn:
        V1=PClose[num]
        V2=PClose[num2]
        if V1<(V2/0.95):
            UR.append(V1)
            UR.append(V2)
        if V1>(0.95*V2):
            DR.append(V1)
            DR.append(V2)
        else:
            SR.append(V1)
            SR.append(V2)
        N=N+1
        num=num+1
        num2=num2+1
    l=len(UR)
    L=l/2
    Q=0
    count=0
    print("\n----------------------------------------\nUR")
    while count<L:
        print(Date[PClose.index(UR[Q])],UR[Q],PClose.index(UR[Q]))
        Q=Q+2
        count=count+1
    l=len(DR)
    L=l/2
    Q=0
    count=0
    print("\n----------------------------------------\nDR")
    while count<L:
        print(Date[PClose.index(DR[Q])],DR[Q],PClose.index(DR[Q]))
        Q=Q+2
        count=count+1
    l=len(SR)
    L=l/2
    Q=0
    count=0
    print("\n----------------------------------------\nSR")
    while count<L:
        print(Date[PClose.index(SR[Q])],SR[Q],PClose.index(SR[Q]))
        Q=Q+2
        count=count+1

    Data={'Date':Date
          ,'Close':PClose
          ,'Low':Low
          ,'Open':Open
          ,'High':High
          ,'Volume':Volume
          ,'Max Trend Line':TLMax
          ,'Min Trend Line':TLMin
          ,'Last Price':LP
          }

    df=pd.DataFrame(Data)
    df.set_index('Date',inplace=True)
    df.to_csv(symbol+'pred.csv')
    visual()
    
def visual():

    plt.style.use('seaborn')
    
    df=pd.read_csv(symbol+'pred.csv',parse_dates=True,index_col=0)

    df['Close'].plot(grid=True, color='blue')
    df['Max Trend Line'].plot(color='darkgreen',linewidth=2,linestyle='-')
    df['Min Trend Line'].plot(color='darkgreen',linewidth=2,linestyle='-')
    df['Last Price'].plot(color='black',linewidth=1,linestyle='--')
    df['50ma']=df['Close'].rolling(window=50,min_periods=0).mean()
    df['50ma'].plot(label='50MA(Short)',color='black')
    df['200ma']=df['Close'].rolling(window=200,min_periods=0).mean()
    df['200ma'].plot(label='200ma(Long)',color='darkred')

    plt.axhline(y=Mx1,label='Rise Resilliance',linewidth=3,color='black',linestyle='--')
    plt.axhline(y=Mn1,label='Fall Resilliance',linewidth=3,color='black',linestyle='--')
    plt.axhline(y=Mean,label='Return Line',linewidth=3,color='blue',linestyle='--')
    plt.legend()
    plt.ylabel('Closing Stock Price')
    plt.title(symbol+' Stock Graph')
    
    plt.show()
        
start()
