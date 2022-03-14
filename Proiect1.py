import random
import time
import sys
sys.setrecursionlimit(10**7)
def radixsort2(v):
    p=1
    ok=1
    sh=0
    while ok==1:
        galz = []
        galu = []
        ok=0
        for i in range(len(v)):
            var=v[i]>>sh
            if var!=0:
                ok=1
                if var&1==1:
                    galu.append(v[i])
                else:
                    galz.append(v[i])
            else:
                galz.append(v[i])
        sh = sh + 1
        v=galz+galu
    return v
def radixsort10(v):
    p=10
    ok=1
    gal=[0,1,2,3,4,5,6,7,8,9]
    while ok==1:
        ok=0
        for i in range(10):
            gal[i]=[]
        for i in range(len(v)):
            if len(str(v[i]))>=len(str(p))-1:
                ok=1
                var = (v[i] % p) // (p // 10)
                gal[var].append(v[i])
            else:
                gal[0].append(v[i])
        v=[]
        for i in range(10):
            v=v+gal[i]
        p=p*10
    return v
def radixsort8(v):
    p=1
    ok=1
    sh=0
    gal = [0, 1, 2, 3, 4, 5, 6, 7]
    while ok==1:
        for i in range(8):
            gal[i]=[]
        ok=0
        for i in range(len(v)):
            var=v[i]>>sh
            if var!=0:
                ok=1
                x=var&7
                gal[x].append(v[i])
            else:
                gal[0].append(v[i])
        sh = sh + 3
        v=[]
        for i in range(8):
            v=v+gal[i]
    return v
def qsortrandom(v,st,dr):
    if st<dr:
        z = random.randint(st, dr)
        aux=v[z]
        v[z]=v[st]
        v[st]=aux
        p=v[st]
        l=st+1
        h=dr
        ok=1
        while ok==1:
            while l<=h and v[l]<=p:
                l=l+1
            while l<=h and v[h]>=p:
                h=h-1
            if l<h:
                aux=v[l]
                v[l]=v[h]
                v[h]=aux
            else:
                ok=0
        aux=v[st]
        v[st]=v[h]
        v[h]=aux
        qsortrandom(v,st,h-1)
        qsortrandom(v,h+1,dr)
def qsortultim(v,st,dr):
    if st<dr:
        p=v[st]
        l=st+1
        h=dr
        ok=1
        while ok==1:
            while l<=h and v[l]<=p:
                l=l+1
            while l<=h and v[h]>=p:
                h=h-1
            if l<h:
                aux=v[l]
                v[l]=v[h]
                v[h]=aux
            else:
                ok=0
        aux=v[st]
        v[st]=v[h]
        v[h]=aux
        qsortultim(v,st,h-1)
        qsortultim(v,h+1,dr)
def shellsort2(v):
    n=len(v)
    h=n//2
    while h>0:
        for i in range(h,n):
            j=i
            while (j-h)>=0 and v[j]<v[j-h]:
                aux = v[j]
                v[j] = v[j-h]
                v[j-h] = aux
                j=j-h
        h=h//2
    return v
def shellsort3(v):
    n=len(v)
    h = 1;
    while h < n:
        h=h * 3 + 1;
    while h>0:
        for i in range(h,n):
            j=i
            while (j-h)>=0 and v[j]<v[j-h]:
                aux = v[j]
                v[j] = v[j-h]
                v[j-h] = aux
                j=j-h
        h=h//3
    return v
def mergesort(x,st,dr):
    if st<dr:
        m=((st+dr)//2)
        #print(m)
        #vs = x[st:(m + 1)]
        #vd = x[(m + 1):(dr+1)]
        #print(vs,vd)
        mergesort(x,st,m)
        mergesort(x,m+1,dr)
        vs = x[st:(m + 1)]
        vd = x[(m + 1):(dr + 1)]
        i=0
        j=0
        k=st
        while i<len(vs) and j<len(vd):
            if vs[i]<vd[j]:
                x[k]=vs[i]
                i=i+1
                k=k+1
            else:
                x[k]=vd[j]
                j=j+1
                k=k+1
        while i<len(vs):
            x[k] = vs[i]
            i = i + 1
            k = k + 1
        while j<len(vd):
            x[k] = vd[j]
            j = j + 1
            k = k + 1
def countsort(v):
    n=max(v)
    frecv=[0]*(n+1)
    for i in v:
        frecv[i]=frecv[i]+1
    c=0
    for i in range(len(frecv)):
        while frecv[i]!=0:
            frecv[i]=frecv[i]-1
            v[c]=i
            c=c+1
    return v
j=input("Alegeti propriul test?")
if j=="da" or j=="DA":
    h=int(input("Scrieti numarul de elemente"))
    H=int(input("Scrieti rangeul elementelor"))
    t=[(H,h)]
else:
    t=[(10000,10000),(1000,100),(100,100),(100000,1000),(10,10000),(1000000,100),(1000000,1000000)]
for Q in range(len(t)):
    print(f"Testul {Q+1}")
    v=[]
    for i in range(t[Q][1]):
        e=random.randint(1,t[Q][0])
        v.append(e)
    x=sorted(v)
    v1=v
    start = time.time()
    v1=radixsort2(v1)
    end = time.time()
    print(f"Runtime of radix sort in baza 2 is {end - start}")
    v2=v
    start = time.time()
    v2= radixsort10(v2)
    end = time.time()
    print(f"Runtime of radix sort in baza 10 is {end - start}")
    v3=v
    start = time.time()
    v3=radixsort8(v3)
    end = time.time()
    print(f"Runtime of radix sort in baza 8 is {end - start}")
    if (t[Q][1]>=10000000 and t[Q][0]<100000) or (t[Q][1]>=1000000 and t[Q][0]<1000)or(t[Q][1]>=100000 and t[Q][0]<100):
        print("Calculatorul nu poate rula quick sort random pivot din cauza numarului mare de recursiuni")
    else:
        v4=v
        u = len(v4) - 1
        start = time.time()
        qsortrandom(v4, 0, u)
        end = time.time()
        print(f"Runtime of random pivot quick sort is {end - start}")
    v5=v
    start = time.time()
    v5 = shellsort2(v5)
    end = time.time()
    print(f"Runtime of shell sort cu impartire la 2 is {end - start}")
    v6=v
    start = time.time()
    v6 = shellsort2(v6)
    end = time.time()
    print(f"Runtime of shell sort cu impartire Knuth's increments is {end - start}")
    v7=v
    u = len(v7) - 1
    start = time.time()
    mergesort(v7, 0, u)
    end = time.time()
    print(f"Runtime of merge sort is {end - start}")
    v8=v
    start = time.time()
    v8 = countsort(v8)
    end = time.time()
    print(f"Runtime of count sort is {end - start}")
    v9=v
    start = time.time()
    v9 = sorted(v9)
    end = time.time()
    print(f"Runtime of sortarea implicita python is {end - start}")
    j=input("Verficati corectitudinea unei sortari?")
    if j=="da" or j=="DA":
        h=int(input("Scrieti numarul sortarii de verificat."))
        if h==1:
            if x == v1:
                print("e corect")
        if h==2:
            if x == v2:
                print("e corect")
        if h==3:
            if x == v3:
                print("e corect")
        if h==4:
            if x == v4:
                print("e corect")
        if h==5:
            if x == v5:
                print("e corect")
        if h==6:
            if x == v6:
                print("e corect")
        if h==7:
            if x == v7:
                print("e corect")
        if h==8:
            if x == v8:
                print("e corect")
        if h==9:
            if x == v9:
                print("e corect")