
def get_parity(value):
    count = 0
    for i in range(len(value)):
        if value[i] == '1':
            count = count+1
        else:
            continue
    if count%2 == 0:
        return 0
    else:
        return 1
        
def StopnWait(segment):
    recieved = [0]*len(segment)
    #Wt = 1
    #Wr = 1
    for i in range(len(segment)):
        
        count = 0
        if i == 1:
            count += 1
        recieved[i] = segment[i]
    if (count%2):
        recieved.append('0')
        return recieved
    else:
        recieved.append('1')
        return recieved    



def GoBackN(segment,user_recieved):
    
    count = 0
    print('Window\tReciever')
    recieved = [0]*len(segment)
    for i in range(len(segment)):
        new_seg = segment[i:i+3]
        print(new_seg,'\t',new_seg[0])
        recieved[i] = new_seg[0]
        if (new_seg[0] == '1'):
            count += 1
    
    if (count%2 == 0):
        recieved.append('0')
    else:
        recieved.append('1')
    print(recieved)
    
    if str(get_parity(user_recieved)) == recieved[-1]:
        print('No error occured during transmission')
    else:
        print('Error occured during transmission')


segment= input('Enter a segment to transfer: ')
user_recieved = input('Enter the recieved segment: ')
n=StopnWait(segment)
print(n)