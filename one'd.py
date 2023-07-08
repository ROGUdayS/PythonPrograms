def get_bit():
    in_parity=input("Input a Bit Stream of max lenth of 7 :")
    if(len(in_parity)<=7):
        for i in range(len(in_parity)):
            if not(in_parity[i]=='1' or in_parity[i]=='0'):
                return get_bit()
        return in_parity
    else:
        return get_bit()

def count_fn(in_parity):
    ones_count=0
    for i in range(len(in_parity)):
        if(in_parity[i]=='1'):
            ones_count+=1
    return ones_count

def parity_corrector(in_parity,ones_count):
    if(ones_count%2==0):
        print("The input is an even parity")
        in_parity+='0'
        return in_parity
    else:
        print("The input is an odd parity")
        in_parity+='1'
        return in_parity

def one_d_paritycheck():
    in_parity=get_bit()
    print("The input bit Stream is :",in_parity)
    ones_count=count_fn(in_parity)
    corr_parity=parity_corrector(in_parity,ones_count)
    print("Thus the parity bit is :",ones_count)
    print("The corrected bit stream is :", corr_parity)

one_d_paritycheck()