from math import radians


def get_bit():
    in_parity=input("input:")
    if len(in_parity)<=7:
        for i in range(len(in_parity)):
            if not (in_parity[i]=='1' or in_parity[i]=='0'):
                return get_bit()
        return in_parity
    else:
        return get_bit()


def count_fn(in_parity):
    ones_count=0
    zeros_count=0
    for i in range(len(in_parity)):
        if(in_parity[i]=='1'):
            ones_count+=1
        if(in_parity[i]=='0'):
            zeros_count+=0
    return ones_count,zeros_count


def parity_corrector(ones_count, in_parity):  
    if(ones_count%2==0):
        in_parity+='0'
        print("The input stream is an even parity")
        return in_parity
    else:
        in_parity+='1'
        print("The input parity is an odd parity")
        return in_parity

def one_d_paritycheck():
    in_parity=get_bit()
    ones_count, zeros_count = count_fn(in_parity)
    corr_par=parity_corrector(ones_count, in_parity)
    print(corr_par)
    out_par=input("Output parity :")
    if (out_par==corr_par):
        print("The segment is valid")
    else:
        print("the segment is invalid")

one_d_paritycheck()