def print_with_quotes(l,h):
    #print(l)
    #print(' '.join(l).replace('"',''),end='')
    s=' '.join(l)
    k=0
    j=0
    for i in s:
        if i=="\"":
            k+=1
        j+=1
        if k==2:
            break
    s1=''
    for i in range(j,len(s)):
        if s[i] in h:
            s1+=str(h[s[i]])
        
        else:
            s1+=s[i]
    if len(s1)!=0:
        print(s[:j].replace('"','')+str(eval(s1)),end=' ')
    else:
        print(s[:j].replace('"',''),end=' ')

def print_without_quotes(tokens,h):
    s=''
    for i in range(2,len(tokens)):
        if(tokens[i].isalpha()):
            s+=str(h[tokens[i]])
        else:
            s+=str(tokens[i])
    s=s.replace('/','//')
    print(eval(s),end='')

def println_with_quotes(l,h):
    #s=' '.join(l).replace('"','')
    s=' '.join(l)
    k=0
    j=0
    for i in s:
        if i=="\"":
            k+=1
        j+=1
        if k==2:
            break
    s1=''
    for i in range(j,len(s)):
        if s[i] in h:
            s1+=str(h[s[i]])
        
        else:
            s1+=s[i]
    if len(s1)!=0:
        print(s[:j].replace('"','')+str(eval(s1)))
    else:
        print(s[:j].replace('"',''))

def println_without_quotes(tokens,h):
    s=''
    for i in range(2,len(tokens)):
        
        if(tokens[i].isalpha()):
            #print(h)
            if(tokens[i] in h):
                s+=str(h[tokens[i]])
            else:
                s+=str(tokens[i])
        else:
            s+=str(tokens[i])
    s=s.replace('/','//')
    print(eval(s))

def Create_Integers(l,Integer_table):
    for i in l:
        Integer_table[i]=0
    return Integer_table

def let_function(l,Integer_table):
    s=''
    #print(l)
    #print(Integer_table)
    #input("Enter a number to cont")
    for i in range(2,len(l)):
        '''for j in l[i]:
            if j.isalpha():
                s+=str(Integer_table[j])
            else:
                s+=j'''
        if l[i].isalpha():
            s+=str(Integer_table[l[i]])
        else:
            s+=l[i]
    Integer_table[l[0]]=eval(s)
    #print("Modified integer table")
    #print(Integer_table)
    return(Integer_table)

def input_function(l,Integer_table):
    number_of_integers=len(l[2:])
    #print("Enter number")
    integers=list(map(int,input().split(',')))
    if(number_of_integers!=len(integers)):
        print("Line ",l[0]," missing input value")
        exit()
    else:
        for i in range(2,len(l)):
            Integer_table[l[i]]=integers[i-2]
        #print(Integer_table)
        return(Integer_table)

def if_goto(l,Integer_table):
    s=''
    #print(l)
    for i in range(1,len(l)):
        if(l[i]=='THEN'):
            break
        if l[i] in Integer_table:
            s+=str(Integer_table[l[i]])
        else:
            for j in l[i]:
                if(j.isalpha()):
                    s+=str(Integer_table[j])
                elif(j=='='):
                    s+='=='
                elif(j=='!'):
                    s+='!='
                else:
                    s+=j
    if(eval(s)):
        return(int(l[-1]))
    else:
        return(0)

def if_second_function(l,Integer_table):
    s=''
    for i in range(1,len(l)):
        if(l[i]=='THEN'):
            if(eval(s)):
                if(l[i+1]=='PRINTLN'):
                    println_with_quotes(l[i+2:])
                else:
                    print_with_quotes(l[i+2:])
            break
        for j in l[i]:
            if(j.isalpha()):
                s+=str(Integer_table[j])
            elif(j=='='):
                s+='=='
            elif(j=='!'):
                s+='!='
            else:
                s+=j

def push_func(l,Integer_table,stack_push_pop):
    s=''
    for i in range(len(l)):
        if l[i] in Integer_table:
            s+=str(Integer_table[l[i]])
        else:
            for j in l[i]:
                if(j.isalpha()):
                    s+=str(Integer_table[j])
                elif(j=='='):
                    s+='=='
                elif(j=='!'):
                    s+='!='
                else:
                    s+=j
    #print("if condition",s)
    stack_push_pop.append(eval(s))
    return stack_push_pop
    

file=open("Input_9_2.txt","r")
lines=file.readlines()
h={}
line_num={}#To store line numbers
instructions=[]
line=0
for i in lines:
    i=i.upper()
    i=i.replace(',',' ')
    tokens=i.split()
    #print(tokens)
    h[int(tokens[0])]=line
    line_num[line]=int(tokens[0])
    instructions.append(tokens)
    line+=1
curr_line=0
#print(line_num)
#print(h)
instruction=''
Integer_table={}
k=0
stack=[]#To store gosub lines
stack_push_pop=[]
#print(h)
while(True):
    #print(instruction)
    #print("curr_line" ,curr_line)
    #print(instructions[curr_line])
    instruction=instructions[curr_line][1]
    #print("Instruction===",instruction)
    if(instruction=='END'):
        exit()
    if(instruction=='INTEGER'):
        Integer_table=Create_Integers(instructions[curr_line][2:],Integer_table)
    if(instruction=='LET'):
        Integer_table=let_function(instructions[curr_line][2:],Integer_table)
    if(instruction=='INPUT'):
        Integer_table=input_function(instructions[curr_line],Integer_table)
    if(instruction=='PRINT'):
        #print()
        if(instructions[curr_line][2][:1]=='\"'):
            print_with_quotes(instructions[curr_line][2:],Integer_table)
        else:
            print_without_quotes(instructions[curr_line],Integer_table)
    
    if(instruction=='PRINTLN'):
        #print(instructions[curr_line])
        if(instructions[curr_line][2][:1]=='\"'):
            println_with_quotes(instructions[curr_line][2:],Integer_table)
        else:
            println_without_quotes(instructions[curr_line],Integer_table)

    if instruction=='IF':
        #print(instructions[curr_line])
        if 'GOTO' in instructions[curr_line]:
            
            k=if_goto(instructions[curr_line][1:],Integer_table)
            #print("k after if goto condition",k)
        else:
            if_second_function(instructions[curr_line][1:],Integer_table)
    
    if instruction=='GOTO':
        k=int(instructions[curr_line][2])
    if instruction=='GOSUB':
        
        stack.append(curr_line)#pushing the line number
        k=int(instructions[curr_line][2])
        #curr_line=h[int(instructions[curr_line][2])]
    if instruction=='RET':
        k=line_num[stack.pop()+1]
        #curr_line=h[line_num[stack.pop()+1]]
    if instruction=='PUSH':
        
        stack_push_pop=push_func(instructions[curr_line][2:],Integer_table,stack_push_pop)

    if instruction=='POP':
        Integer_table[instructions[curr_line][2]]=stack_push_pop.pop()
    
    
    

    if(k==0):
        curr_line+=1
    else:
        curr_line=h[k]
        k=0
    
