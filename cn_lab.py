#1-D and 2-D parity checking 
#Used parity scheme is even parity scheme

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
 
#1-D parity   
in_par = input('Enter the parity: ')
parity = get_parity(in_par)

new_par = input('Enter a new parity to check: ')
new_parity = get_parity(new_par)

if (new_parity == parity):
    print("\n This is a valid segment")
else:
    print("\n This is an invalid segment")

#2-D parity

"""def get_2Dparity(mat):
    
    empty_string = '' #To calculate 2-D parity
    
    for i in range(len(mat[0])):
        temp = ''
        for j in range(len(mat)):
            temp = temp + mat[j][i]
        empty_string = empty_string + str(get_parity(temp))
    
    mat.append(empty_string)
    return

mat = []
size = int(input('Enter the number of data-segments: '))

for j in range(size):
    par = input('Enter the segment seq_number, all must be of same length: ')
    mat.append(par + str(get_parity(par)))
get_2Dparity(mat)

print('')

mat1 = []
for j in range(size):
    par = input('Enter the new segment seq_number, all must be of same length: ')
    mat1.append(par + str(get_parity(par)))
get_2Dparity(mat1)

for k in range(len(mat)):
    
    if mat[k][-1] == mat1[k][-1]:
        continue    
    elif mat[-1] == mat1[-1]:
        continue
    else:
        print('\n Error during transmission occured')
        break"""

# CheckSum
'''
def findChecksum(SentMessage, k):

	c1 = SentMessage[0:k]
	c2 = SentMessage[k:2*k]
	c3 = SentMessage[2*k:3*k]
	c4 = SentMessage[3*k:4*k]

	Sum = bin(int(c1, 2)+int(c2, 2)+int(c3, 2)+int(c4, 2))[2:]

	if(len(Sum) > k):
		x = len(Sum)-k
		Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
	if(len(Sum) < k):
		Sum = '0'*(k-len(Sum))+Sum

	Checksum = ''
	for i in Sum:
		if(i == '1'):
			Checksum += '0'
		else:
			Checksum += '1'
	return Checksum

def checkReceiverChecksum(ReceivedMessage, k, Checksum):

	c1 = ReceivedMessage[0:k]
	c2 = ReceivedMessage[k:2*k]
	c3 = ReceivedMessage[2*k:3*k]
	c4 = ReceivedMessage[3*k:4*k]

	ReceiverSum = bin(int(c1, 2)+int(c2, 2)+int(Checksum, 2) +
					int(c3, 2)+int(c4, 2))[2:]

	if(len(ReceiverSum) > k):
		x = len(ReceiverSum)-k
		ReceiverSum = bin(int(ReceiverSum[0:x], 2)+int(ReceiverSum[x:], 2))[2:]
	
	return str(ReceiverSum)



SentMessage = "10010101011000111001010011101100"
k = 8
ReceivedMessage = "10010101011000111001010011101100"

Checksum = findChecksum(SentMessage, k)

ReceiverChecksum = checkReceiverChecksum(ReceivedMessage, k, Checksum)

print("SENDER SIDE CHECKSUM: ", Checksum)
print("RECEIVER SIDE CHECKSUM: ", ReceiverChecksum)

finalcomp=''
for i in ReceiverChecksum:
	if(i == '1'):
		finalcomp += '0'
	else:
		finalcomp += '1'

if(int(finalcomp,2) == 0):
	print("Receiver Checksum is equal to 0. Therefore,")
	print("STATUS: ACCEPTED")
	
else:
	print("Receiver Checksum is not equal to 0. Therefore,")
	print("STATUS: ERROR DETECTED")
'''