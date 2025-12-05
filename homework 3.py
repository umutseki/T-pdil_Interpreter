output = ""
def main():
    # DO NOT CHANGE
    global output
    handle = open('input.tup')
    code = handle.read()
    handle.close()
    def mylower(var): #it will make everything in lowercase (except strings but then i gave up about them)
        str_=False
        new=""
        for a in var:
            if a=="!": 
                if str_:
                    str_=False
                else:
                    str_=True
            if not str_:
                if a=="İ":
                    new+="i"
                elif a=="I":
                    new+="ı"
                else:
                    new+=a.lower()
            elif str_:
                new+=a
        return new
    
    def boslukvarmı(check): #again, if its not string, it will check if there is double space
        str_=False
        global comperr
        for a in check:
            for b in range(len(a)):
                if a[b]=="!":
                    if str_:
                        str_=False
                    else:
                        str_=True
                if not str_:
                    if a[b:b+2]=="  ":
                        comperr.append(check.index(a)+1)
                       
    def tamsayımı(check): #its checking if argument is tam-sayı in tüpdil
        if check==None:
            return False
        if len(str(check))==4:
            return False
        if check==True or check==False:
            return False
        characters="1234567890-."
        nokta=0
        for a in check:
            if a not in characters:
                return False
            
            if a==".":
                nokta+=1
        if nokta>1:
            return False
  
        if nokta==1:
            if check.index(".")!=len(check)-4:
                return False
            if check.index(".")==0:
                return False
            check=check.replace(".","")
        for a in range(1,len(check)):
            if a=="-":
                return False
        try:
            check=int(check)
        except:
            return False
        if check>10000 or check<-10000:
            return False
        if not -1000<check<1000:
            if nokta==0:
                return False
        return True
    
    def reelsayımı(check): #its checking if argument is reel-sayı in tüpdil
        if check==None or check==False or check==True:
            return False
        characters="1234567890-.,"
        nokta=0
        virgül=0
        if check==None:
            return False
        for a in check:
            if a not in characters:
                return False
            if a==".":
                nokta+=1
            if a==",":
                virgül+=1
            if a=="-":
                if check.index("-")!=0:
                    return False
        if virgül==0:
            return False
        if nokta>=2:
            return False
        if nokta==1:
            if virgül==0:
                return False
            if check.index(".")!=check.index(",")-4:
                return False
            check=check.replace(".","")
        if check.index(",")<=len(check)-5:
            return False
        if check[-1]==",":
            return False
        if check[0]==",":
            return False
        check=check.replace(",",".")
        try:
            check=float(check)
        except:
            return False
        if check>10000 or check<-10000:
            return False
        if check<=-1000 or check>=1000:
            if nokta==0:
                return False
        return True
    
    def metinmi(*args): #I GAVE UP about them :(
        check=" ".join(args)
        if check[0]!="!" or check[-1]!="!":
            return False
        else:
            check=check[1:-1]
        characters="1234567890ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz .,:;"
        for a in check:
            if a not in characters:
                return False
        if len(check)>50:
            return False
        return True
    forb=False #i dont even remember what is this
    def varexpmi(args): #its checking expression and looking if its full of variables
        global vartypes
        global comperr
        global operatörler
        operatörler=["artı","eksi","çarp","bölü"]
        ops=[]
        values=[]
        for a in args:
            if args.index(a)==0:
                line=a
            elif args.index(a)%2==1:
                values.append(a)
            elif args.index(a)%2==0:
                ops.append(a)
        for a in values:
            if a not in vartypes:
                comperr.append(line)
                return False
        for a in ops:
            if a not in operatörler:
                comperr.append(line)
                return False
        return True
    
    def integerconverter(e): #its converting tam-sayı to integer
        if e is int:
            return e
        characters="1234567890-."
        nokta=0
        check=e
        for a in check:
            if a not in characters:
                return None
            if a==".":
                nokta+=1
        if nokta>1:
            return None
        if nokta==1:
            if check.index(".")!=len(check)-4:
                return None
            check=check.replace(".","")
        for a in range(1,len(check)):
            if a=="-":
                return False
        try:
            check=int(check)
        except:
            return None
        if check>10000 or check<-10000:
            return None
        if not -1000<check<1000:
            if nokta==0:
                return None
        return check

    def intlenebilirmi(a): #for zıpla function, its checking if the argument is integer convertable
        if reelsayımı(a):
            a=a.replace(".","")
            a=a.replace(",",".")
            a=float(a)
            if (a-a//1)!=0:
                return False
            else:
                return a
        elif tamsayımı(a):
            return int(a)

    def floatconverter(check): #its converting reel-sayı to float
        if check is float:
            return check
        characters="1234567890-.,"
        nokta=0
        virgül=0
        for a in check:
            if a not in characters:
                return False
            if a==".":
                nokta+=1
            if a==",":
                virgül+=1
            if a=="-":
                if check.index("-")!=0:
                    return False
        if virgül==0:
            return False
        if nokta>=2:
            return False
        if nokta==1:
            if virgül==0:
                return False
            if check.index(".")!=check.index(",")-4:
                return False
            check=check.replace(".","")
        if check.index(",")<=len(check)-5:
            return False
        if check[-1]==",":
            return False
        if check[0]==",":
            return False
        check=check.replace(",",".")
        try:
            check=float(check)*1000
        except:
            return False
        if check>10000000 or check<-10000000:
            return False
        if check<=-1000000 or check>=1000000:
            if nokta==0:
                return False
        return check

    def reelsayıreverseconverter(check): #its making float back to reel-sayı
        check=check/1000
        if forb:
            check=check*1000
        if -1000<check<1000:
            check=str(check)
            check=check.replace(".",",")
        elif -10000<=check<=10000:

            check=str(check)
            check=check.replace(".",",")
            virgül=check.index(",")
            check=check[:virgül-3]+"."+check[virgül-3:]
        return check

    def tamsayıreverseconverter(a): #its making integer a tam-sayı in tüpdil
        if -1000<a<1000:
            return str(a)
        else:
            bu=str(a)
            new=bu[:-3]+"."+bu[-3:]
            return new

    def sabitexpmi(args): #its checking if expression is full of constants
        global vartypes
        global comperr
        global linein
        ops=[]
        values=[]
        operatörs=["artı","eksi","çarp","bölü"]
        for a in args:
            if args.index(a)==0:
                line=a
            elif args.index(a)%2==0:
                ops.append(a)
            elif args.index(a)%2==1:
                values.append(a)
        for a in ops:
            if a not in operatörs:
                comperr.append(line)
                return False
        for a in values:
            if reelsayımı(a) or tamsayımı(a):
                pass  
            else:
                return False
        return True

    def variablemı(check): #if the argument is a valid variable checking function
        global vartypes
        if check in vartypes:
            return True

    def toplasabit(a,b): #sum up
        if tamsayımı(a):
            typea="tam-sayı"
        elif reelsayımı(a):
            typea="reel-sayı"
        else:
            return False
        if tamsayımı(b): 
            typeb="tam-sayı"
        elif reelsayımı(b):
            typeb="reel-sayı"
        else:
            return False
        if typea=="tam-sayı" and typeb=="tam-sayı":
            inta=integerconverter(a)
            intb=integerconverter(b)
            if inta+intb<=-10000 or inta+intb>=10000:
                return False
            return tamsayıreverseconverter(inta+intb)
        if (typea=="tam-sayı" and typeb=="reel-sayı"):
            return False
        if typea=="reel-sayı" and typeb=="tam-sayı":
            return False
        if typea=="reel-sayı" and typeb=="reel-sayı":
            floata=floatconverter(a)
            floatb=floatconverter(b)
            if floata+floatb<=-10000000 or floata+floatb>=10000000:
                return False
            res=reelsayıreverseconverter(floata+floatb)
            return res

    def çıkarsabit(a,b): #subtracting
        if tamsayımı(a):
            typea="tam-sayı"
        elif reelsayımı(a):
            typea="reel-sayı"
        elif metinmi(a):
            typea="metin"
        else:
            pass
        if tamsayımı(b): 
            typeb="tam-sayı"
        elif reelsayımı(b):
            typeb="reel-sayı"
        elif metinmi(b):
            typeb="metin"
        if typea=="tam-sayı" and typeb=="tam-sayı":
            inta=integerconverter(a)
            intb=integerconverter(b)
            if inta-intb>=10000 or inta-intb<=-10000:
                return False
            return tamsayıreverseconverter(inta-intb)
        if (typea=="tam-sayı" and typeb=="reel-sayı"):
            return False
        if typea=="reel-sayı" and typeb=="tam-sayı":
            return False
        if typea=="reel-sayı" and typeb=="reel-sayı":
            floata=floatconverter(a)
            floatb=floatconverter(b)
            if floata-floatb<=-10000000 or floata-floatb>=10000000:
                return False
            return reelsayıreverseconverter(floata-floatb)

    def çarpsabit(a,b): #multiplying
        if tamsayımı(a):
            typea="tam-sayı"
        elif reelsayımı(a):
            typea="reel-sayı"
        elif metinmi(a):
            typea="metin"
        else:
            pass
        if tamsayımı(b): 
            typeb="tam-sayı"
        elif reelsayımı(b):
            typeb="reel-sayı"
        elif metinmi(b):
            typeb="metin"
        if typea=="tam-sayı" and typeb=="tam-sayı":
            inta=integerconverter(a)
            intb=integerconverter(b)
            if not -10000<=inta*intb<=10000:
                return False
            res=reelsayıreverseconverter(inta*intb*1000)
            return res
        if (typea=="tam-sayı" and typeb=="reel-sayı"):
            return False
        if typea=="reel-sayı" and typeb=="tam-sayı":
            return False
        if typea=="reel-sayı" and typeb=="reel-sayı":
            floata=floatconverter(a)
            floatb=floatconverter(b)
            if not -10000000000<=floata*floatb<=10000000000:
                return False
            res=reelsayıreverseconverter(floata*floatb/1000)
            cont=res.split(",")
            if len(cont[1])>3:
                return False
            return reelsayıreverseconverter(floata*floatb/1000)

    def bölsabit(a,b): #division
        global forb
        forb=True
        if tamsayımı(a):
            typea="tam-sayı"
        elif reelsayımı(a):
            typea="reel-sayı"
        elif metinmi(a):
            typea="metin"
        else:
            return False
        if tamsayımı(b): 
            typeb="tam-sayı"
        elif reelsayımı(b):
            typeb="reel-sayı"
        elif metinmi(b):
            typeb="metin"
        else:
            return False
        if typea=="metin" or typeb=="metin":
            return False
        if typea=="tam-sayı" and typeb=="tam-sayı":
            inta=integerconverter(a)
            intb=integerconverter(b)
            if intb==0:
                return False
            res=reelsayıreverseconverter(inta/intb*1000)
            return res
        if (typea=="tam-sayı" and typeb=="reel-sayı"):
            return False
        if typea=="reel-sayı" and typeb=="tam-sayı":
            return False
        if typea=="reel-sayı" and typeb=="reel-sayı":
            floata=floatconverter(a)
            floatb=floatconverter(b)
            if floatb==0:
                return False
            res=reelsayıreverseconverter(floata/floatb*1000)
            cont=res.split(",")
            try:
                if len(cont[1])>3:
                    return False
            except:
                pass
            return res

    def typecalculator(abcd): #its checking the type of result of an abcd expression
        global vartypes
        if sabitexpmi(abcd):
            line=0
            ops=[]
            values=[]
            for a in range(len(abcd)):
                if a==0:
                    line=abcd[0]
                elif a%2==1:
                    values.append(abcd[a])
                else:
                    ops.append(abcd[a])
            while len(values)>1:         
                val1=values[0]
                typeval1=""
                if tamsayımı(val1):
                    typeval1="tam-sayı"
                elif reelsayımı(val1):
                    typeval1="reel-sayı"
                else:
                    return False
                val2=values[1]
                typeval2=""
                if tamsayımı(val2):
                    typeval2="tam-sayı"
                elif reelsayımı(val2):
                    typeval2="reel-sayı"
                else:
                    return False
                op=ops[0]
                if op=="artı" or op=="eksi":
                    if typeval1==typeval2:
                        if typeval1=="tam-sayı":
                            values.pop(0)
                            values.pop(0)
                            values.insert(0,"1")
                            ops.pop(0)
                        elif typeval1=="reel-sayı":
                            values.pop(0)
                            values.pop(0)
                            values.insert(0,"1,0")
                            ops.pop(0)
                    else:
                        return False
                elif op=="çarp" or op=="bölü":
                    if typeval1==typeval2:
                        if typeval1=="tam-sayı":
                            values.pop(0)
                            values.pop(0)
                            values.insert(0,"1,0")
                            ops.pop(0)
                        elif typeval1=="reel-sayı":
                            values.pop(0)
                            values.pop(0)
                            values.insert(0,"1,0")
                            ops.pop(0)
                    else:
                        return False
                else:
                    return False
            if tamsayımı(values[0]):
                return "tam-sayı"
            elif reelsayımı(values[0]):
                return "reel-sayı"
            else:
                return False
        elif varexpmi(abcd):
            line=0
            types=[]
            ops=[]   
            for a in range(len(abcd)):
                if a==0:
                    line=abcd[0]
                elif a%2==1:
                    types.append(vartypes[abcd[a]])
                else:
                    ops.append(abcd[a])
            if "metin" in types:
                return False
            while len(types)>1:
                val1=types[0]
                val2=types[1]
                op=ops[0]
                if op=="artı" or op=="eksi":
                    if val1==val2:
                        if val1=="tam-sayı":
                            types.pop(0)
                            types.pop(0)
                            types.insert(0,"tam-sayı")
                            ops.pop(0)
                        elif val1=="reel-sayı":
                            types.pop(0)
                            types.pop(0)
                            types.insert(0,"reel-sayı")
                            ops.pop(0)
                    else:
                        return False
                if op=="çarp" or op=="bölü":
                    if val1==val2:
                        if val1=="tam-sayı":
                            types.pop(0)
                            types.pop(0)
                            types.insert(0,"reel-sayı")
                            ops.pop(0)
                        elif val1=="reel-sayı":
                            types.pop(0)
                            types.pop(0)
                            types.insert(0,"reel-sayı")
                            ops.pop(0)
                    else:
                        return False
            return types[0]
 
    def typecalculator(abcd): # i dont remember whats the difference
        global vartypes
        global varexetypes
        if sabitexpmi(abcd):
            line=0
            ops=[]
            values=[]
            for a in range(len(abcd)):
                if a==0:
                    line=abcd[0]
                elif a%2==1:
                    values.append(abcd[a])
                else:
                    ops.append(abcd[a])
            while len(values)>1:           
                val1=values[0]
                typeval1=""
                if tamsayımı(val1):
                    typeval1="tam-sayı"
                elif reelsayımı(val1):
                    typeval1="reel-sayı"
                else:
                    return False
                val2=values[1]
                typeval2=""
                if tamsayımı(val2):
                    typeval2="tam-sayı"
                elif reelsayımı(val2):
                    typeval2="reel-sayı"
                else:
                    return False
                op=ops[0]
                if op=="artı" or op=="eksi":
                    if typeval1==typeval2:
                        if typeval1=="tam-sayı":
                            values.pop(0)
                            values.pop(0)
                            values.insert(0,"1")
                            ops.pop(0)
                        elif typeval1=="reel-sayı":
                            values.pop(0)
                            values.pop(0)
                            values.insert(0,"1,0")
                            ops.pop(0)
                    else:
                        return False
                elif op=="çarp" or op=="bölü":
                    if typeval1==typeval2:
                        if typeval1=="tam-sayı":
                            values.pop(0)
                            values.pop(0)
                            values.insert(0,"1,0")
                            ops.pop(0)
                        elif typeval1=="reel-sayı":
                            values.pop(0)
                            values.pop(0)
                            values.insert(0,"1,0")
                            ops.pop(0)
                    else:
                        return False
                else:
                    return False
            if tamsayımı(values[0]):
                return "tam-sayı"
            elif reelsayımı(values[0]):
                return "reel-sayı"
            else:
                return False
        elif varexpmi(abcd):
            line=0
            types=[]
            ops=[]   
            for a in range(len(abcd)):
                if a==0:
                    line=abcd[0]
                elif a%2==1:
                    types.append(varexetypes[abcd[a]])
                else:
                    ops.append(abcd[a])
            if "metin" in types:
                return False
            while len(types)>1:
                val1=types[0]
                val2=types[1]
                op=ops[0]
                if op=="artı" or op=="eksi":
                    if val1==val2:
                        if val1=="tam-sayı":
                            types.pop(0)
                            types.pop(0)
                            types.insert(0,"tam-sayı")
                            ops.pop(0)
                        elif val1=="reel-sayı":
                            types.pop(0)
                            types.pop(0)
                            types.insert(0,"reel-sayı")
                            ops.pop(0)
                    else:
                        return False
                if op=="çarp" or op=="bölü":
                    if val1==val2:
                        if val1=="tam-sayı":
                            types.pop(0)
                            types.pop(0)
                            types.insert(0,"reel-sayı")
                            ops.pop(0)
                        elif val1=="reel-sayı":
                            types.pop(0)
                            types.pop(0)
                            types.insert(0,"reel-sayı")
                            ops.pop(0)
                    else:
                        return False
            return types[0]

    def variablecalc(abcd): #if its an expression full of variable, its calculating the result
        global varexetypes
        global varvalues
        if sabitexpmi(abcd):
            line=0
            ops=[]
            values=[]
            for a in range(len(abcd)):
                if a==0:
                    line=abcd[0]
                elif a%2==1:
                    values.append(abcd[a])
                else:
                    ops.append(abcd[a])
            while len(values)>1:
                val1=values[0]
                val2=values[1]
                op=ops[0]
                if op=="artı":
                    values.pop(0)
                    values.pop(0)
                    values.insert(0,toplasabit(val1,val2))
                    ops.pop(0)
                elif op=="eksi":
                    values.pop(0)
                    values.pop(0)
                    values.insert(0,çıkarsabit(val1,val2))
                    ops.pop(0)
                elif op=="çarp":
                    values.pop(0)
                    values.pop(0)
                    values.insert(0,çarpsabit(val1,val2))
                    ops.pop(0)
                elif op=="bölü":
                    values.pop(0)
                    values.pop(0)
                    values.insert(0,bölsabit(val1,val2))
                    ops.pop(0)    
                else:
                    return False
            return values[0]

    def calculator(abcd): #its looking the expression and then solving it, (its better than me)
        global varexetypes
        global vartypes
        if sabitexpmi(abcd):
            line=0
            ops=[]
            values=[]
            for a in range(len(abcd)):
                if a==0:
                    line=abcd[0]
                elif a%2==1:
                    values.append(abcd[a])
                else:
                    ops.append(abcd[a])
            while len(values)>1:
                val1=values[0]
                val2=values[1]
                op=ops[0]
                if op=="artı":
                    res=toplasabit(val1,val2)
                    values.pop(0)
                    values.pop(0)
                    values.insert(0,toplasabit(val1,val2))
                    ops.pop(0)
                elif op=="eksi":
                    values.pop(0)
                    values.pop(0)
                    values.insert(0,çıkarsabit(val1,val2))
                    ops.pop(0)
                elif op=="çarp":
                    values.pop(0)
                    values.pop(0)
                    values.insert(0,çarpsabit(val1,val2))
                    ops.pop(0)
                elif op=="bölü":
                    values.pop(0)
                    values.pop(0)
                    values.insert(0,bölsabit(val1,val2))
                    ops.pop(0)    
                else:
                    return False
            return values[0]            
        else:
            newlist=[]
            for a in abcd:
                if a in varvalues:
                    newlist.append(varvalues[a])
                else:
                    newlist.append(a)
            return variablecalc(newlist)                
    def comperrcheck(code): #its checking the code if there are any compile errors
            global comperr
            global output
            global lowcodelines
            global lowcode
            global linein
            global vartypes
            global varexetypes
            comperr=[] #list of compile error(s)
            codelines=code.split("\n") 
            for a in codelines:
                if a=="":  
                    if codelines.index(a)+1!=len(codelines):
                        comperr.append(codelines.index(a)+1)                        
                    else:
                        codelines.pop(-1)          
            lowcode=""  
            validch="abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ.,:;!- 0123456789" #valid characters of code
            letters="abcçdefgğhıijklmnoöprsştuüvyz"            #valid characters for variable name
            for a in codelines:
                for b in a:
                    if b not in validch:
                        comperr.append(codelines.index(a)+1)
            lowcodelines=[]
            lowcode=mylower(code)
            lowcodelines=lowcode.split("\n") 
            for a in lowcodelines:
                if a=="":
                    if lowcodelines.index(a)+1!=len(lowcodelines):
                        comperr.append(lowcodelines.index(a)+1)                        
                    else:
                        lowcodelines.pop(-1)       
            boslukvarmı(lowcodelines)
            if lowcodelines[0]=="programı başlat.":
                pass
            else:
                comperr.append(1)
            if lowcodelines[-1]!="programı bitir.":
                comperr.append(len(lowcodelines))
            for a in range(1,len(lowcodelines)):
                try:
                    if lowcodelines[a][-1]!=".":
                        comperr.append(a+1)
                except:
                    pass            
            vartypes={}           
            keywords=["programı","başlat","bir","olsun","değeri","yazdır","zıpla","satıra","metin","tam-sayı","reel-sayı","artı","eksi","çarp","bölü"]
            types=["metin","tam-sayı","reel-sayı"]
            for a in lowcodelines:       
                words=a.split()
                try:
                    if "bir" in words:    #this is remembering the types with the purpose of ddedecting compile errors
                        if len(words)!=4:
                            comperr.append(lowcodelines.index(a)+1)
                            continue
                        if words[2] not in types:
                            comperr.append(lowcodelines.index(a)+1)
                            continue
                        if words[0] in keywords:
                            comperr.append(lowcodelines.index(a)+1)
                            continue
                        if len(words[0])<=20:
                            pass
                        else:
                            comperr.append(lowcodelines.index(a)+1)
                            continue
                        for let in words[0]:
                            if let not in letters:
                                comperr.append(lowcodelines.index(a)+1)
                                continue
                        if words[3]!="olsun.":
                            comperr.append(lowcodelines.index(a)+1)
                            continue
                        vartypes[words[0]]=words[2]
                except:
                    pass       
            for line in lowcodelines:
                linein=lowcodelines.index(line)+1
                words=line.split()
                try:
                    if "değeri" in words:
                        if len(words)<4:
                            comperr.append(linein)                            
                            continue
                        if words.index("değeri")!=1:
                            comperr.append(linein)
                            continue
                        if words[-1]!="olsun.":
                            comperr.append(linein)                            
                            continue
                        elif words[0] not in vartypes:
                            comperr.append(linein)                            
                            continue
                        if len(words)==4:
                            if vartypes[words[0]]=="tam-sayı":
                                if variablemı(words[2]):
                                    continue
                                elif tamsayımı(words[2]):
                                    continue
                                else:
                                    comperr.append(linein)                                    
                                    continue                                
                            elif vartypes[words[0]]=="reel-sayı":
                                if variablemı(words[2]):
                                    continue
                                elif reelsayımı(words[2]):
                                    continue
                                else:
                                    comperr.append(linein)                                   
                                    continue                                
                            elif vartypes[words[0]]=="metin":
                                comperr.append(linein)
                        else:
                            wxp=[linein]+words[2:-1]
                            if not typecalculator(wxp):
                                comperr.append(linein)                               
                                continue
                            else:
                                if vartypes[words[0]]!=typecalculator(wxp):
                                    comperr.append(linein)                                    
                                    continue
                    elif "satıra" in words and "zıpla." in words:                       
                        if words.index("satıra")!=len(words)-2 or words.index("zıpla.")!=len(words)-1:
                            comperr.append(linein)                            
                            continue
                        if len(words)==3:
                            sayı=words[0][:-1]

                            if tamsayımı(sayı):
                                if integerconverter(sayı)>len(lowcodelines):
                                    comperr.append(linein)
                                    continue
                                else:
                                    continue
                            elif reelsayımı(sayı):
                                if intlenebilirmi(sayı)!=False:
                                    if intlenebilirmi(sayı)>=len(lowcodelines):
                                        comperr.append(linein)
                                        continue
                                    else:
                                        continue
                                else:
                                    comperr.append(linein)
                            elif variablemı(sayı):
                                pass
                            else:
                                comperr.append(linein)
                                continue
                        else:
                            kxp=[]
                            kxp.append(linein)
                            for a in range(len(words)-2):
                                if words.index(words[a])!=len(words)-3:
                                    kxp.append(words[a])
                                else:
                                    kxp.append(words[a][:-1])
                            if typecalculator(kxp)==False:
                                comperr.append(linein)
                                continue                    
                    elif "yazdır." in words:
                        if words.index("yazdır.")!=len(words)-1:
                            comperr.append(linein)                        
                            continue
                        if len(words)>2:
                            newxp=[]
                            newxp.append(linein)
                            newxp+=words[:-1]
                            if typecalculator(newxp)==False:
                                comperr.append(linein)                               
                                continue
                    elif words==["programı","başlat."]:
                        pass
                    elif words==["programı","bitir."]:
                        pass
                    elif "bir" in words:
                        pass
                    else:
                        comperr.append(linein)          
                except:
                    pass
    def your_function(code): 
        global output
        global comperr
        global lowcodelines
        global lowcode
        global varexetypes
        global varvalues  
        hata=False 
        comperrcheck(code)
        if comperr!=[]:  #if its not an empty list, it will print an error message
            hata=True #if hata is true, our code will stop so if there is a CE, this makes the code stop
            output="Compile Error at line "+str(min(comperr))+"." #if i have to explain this, what are we even doing here
        activeline=0
        varvalues={}
        varexetypes={}
        while not hata:
            activeline=int(activeline) #if the result of jump is float, this makes it integer
            lineinex=activeline+1 #purpose of this is for printing error messages
            if activeline==len(lowcodelines)-1:
                break
            line=lowcodelines[activeline]
            words=line.split()
            if line=="programı başlat.":
                activeline+=1
                continue
                
            elif "bir" in words:
                varexetypes[words[0]]=words[2]
                activeline+=1
                continue
            elif "yazdır." in words:
                calc=[]
                calc.append(activeline)
                words=line.split()
                calc=calc+words[:-1]
                if calculator(calc)==None or calculator(calc)==False:
                    hata=True
                    output+="Runtime error at line "+str(lineinex)+"."+"\n"
                    continue
                output=output+str(calculator(calc))+"\n" #its printing out the result
                activeline+=1
                continue
            elif "zıpla." in words:
                hopla=[]
                hopla.append(activeline)
                if len(words)==3:
                    hopla.append(words[0][:-1])
                else:
                    hopla=hopla+words[:-3]
                    hopla.append(words[-3][:-1])
                if calculator(hopla)==False:
                    hata=True
                    output+="Runtime error at line "+str(lineinex)+"."+"\n"
                    continue
                else:
                    if intlenebilirmi(calculator(hopla))!=False:
                        if calculator(hopla)==False:
                            hata=True
                            output+="Runtime error at line "+str(lineinex)+"."+"\n"
                            continue
                        elif intlenebilirmi(calculator(hopla))>len(lowcodelines):
                            hata=True
                            output+="Runtime error at line "+str(lineinex)+"."+"\n"
                            continue
                        activeline=intlenebilirmi(calculator(hopla))-1 #this is where the magic happens (jumps)
                        if activeline<0:
                            hata=True
                            output+="Runtime error at line "+str(lineinex)+"."+"\n"
                            continue
                        continue
                    else:
                        hata=True
                        output+="Runtime error at line "+str(lineinex)+"."+"\n"
                        continue
            elif "değeri" in words:       
                if words[0] in varexetypes:
                    wilcalc=[activeline]
                    for a in range(2,len(words)-1):
                        wilcalc.append(words[a])
                    if calculator(wilcalc)==False:
                        output+="Runtime error at line "+str(lineinex)+"."+"\n"
                        hata=True
                        continue
                    deger=calculator(wilcalc)
                    if varexetypes[words[0]]=="tam-sayı":
                        if tamsayımı(deger):
                            varvalues[words[0]]=calculator(wilcalc)
                        else:
                            hata=True
                            output+="Runtime error at line "+str(lineinex)+"."+"\n"
                            continue
                    if varexetypes[words[0]]=="reel-sayı":
                        if reelsayımı(deger):
                            varvalues[words[0]]=calculator(wilcalc)
                        else:
                            hata=True
                            output+="Runtime error at line "+str(lineinex)+"."+"\n"
                            continue
                    activeline+=1
                    continue
                else:
                    output+="Runtime error at line "+str(lineinex)+"."+"\n"
                    hata=True
                    continue
            if "bitir." in words:
                break 
    your_function(code)
    for a in range(len(output)-1,0,-1):
        if output[a]=="": 
            output.pop(a)
    outlines=output.split("\n") 
    if outlines[-1]!="": #if there is no empty line at last, this will fix it.
        output=output+"\n" #1071 lines for dedication to the opening of Anatolia's gates to the Turks.

    # DO NOT CHANGE
    handle = open('output.txt','w')
    handle.write(output)
    handle.close()

main()
