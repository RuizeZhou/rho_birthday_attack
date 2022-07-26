#coding:utf-8
#22/05/15  Ruize Zhou
import utils
IV='7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e'
import numpy as np
from gmssl import sm3, func


seed=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','\0']
# string IV = "7380166F4914B2B9172442D7DA8A0600A96F30BC163138AAE38DEE4DB0FB0E4E";
# unsigned int Tj[2] = { 0x79cc4519, 0x7a879d8a };
# string hex_num = "0123456789ABCDEF";
# unsigned int* Extend_m_1 = new unsigned int[68];
# unsigned int* Extend_m_2 = new unsigned int[64];

def getinput(len=10):
    input_data=''
    for i in range(0,len):
        input_data+=seed[np.random.randint(0,17)]

    return input_data





def naive_birthday(n):
    memory=[]
    for i in range(2**n):
        memory+=['blank']
    temp=n//2
    for i in range(2**temp):
        input_data=getinput()
        joint_b=bytes(input_data,encoding='utf-8')
        output_data= sm3.sm3_hash(func.bytes_to_list(joint_b))


        # output_data=sm3(input_data).label
        prefix=output_data[0:(temp//2)]
        index=int(prefix,16)

        if memory[index]=="blank":
            memory[index]=input_data
        else:
            return memory[index],input_data








def rho_birthday(n):
    length=n//4
    i=1
    input_data=getinput(100)
    input_data=bytes(input_data,encoding='utf-8')

    enc_slow=sm3.sm3_hash(func.bytes_to_list(input_data))

    enc_quick= sm3.sm3_hash(func.bytes_to_list(bytes(enc_slow,encoding='utf-8')))

    while enc_slow[0:length]!= enc_quick[0:length]:
        enc_slow=sm3.sm3_hash(func.bytes_to_list(bytes(enc_slow,encoding='utf-8')))

        enc_qu_temp=sm3.sm3_hash(func.bytes_to_list(bytes(enc_quick,encoding='utf-8')))
        enc_quick=sm3.sm3_hash(func.bytes_to_list(bytes(enc_qu_temp,encoding='utf-8')))
        i+=1
    print(i)
    enc_slow=sm3.sm3_hash(func.bytes_to_list(input_data))
    enc_quick=sm3.sm3_hash(func.bytes_to_list(input_data))

    for j in range(i):

        enc_quick=sm3.sm3_hash(func.bytes_to_list(bytes(enc_quick,encoding='utf-8')))

    # temp_slow=''
    # temp_fast=''

    # enc_slow_te=enc_slow
    # enc_quick_te=enc_quick
    for j in range(i+1):

        temp_slow=sm3.sm3_hash(func.bytes_to_list(bytes(enc_slow,encoding='utf-8')))


        temp_fast=sm3.sm3_hash(func.bytes_to_list(bytes(enc_quick,encoding='utf-8')))

        if temp_fast[0:length]==temp_slow[0:length]:
            return enc_slow,enc_quick
        else:
            enc_slow=temp_slow
            enc_quick=temp_fast

    return None,None






if __name__=='__main__':

    lenth=8
    # a1,a2=naive_birthday(lenth)
    # print(a1,'\t',a2)
    #
    # enc_a1=bytes(a1,encoding='utf-8')
    # enc_a1= sm3.sm3_hash(func.bytes_to_list(enc_a1))
    # print(a1,':',enc_a1)
    #
    # enc_a2=bytes(a2,encoding='utf-8')
    # enc_a2= sm3.sm3_hash(func.bytes_to_list(enc_a2))
    # print(a2,':',enc_a2)



    a1,a2=rho_birthday(lenth)
    print(a1,'\t',a2)

    enc_a1=bytes(a1,encoding='utf-8')
    enc_a1= sm3.sm3_hash(func.bytes_to_list(enc_a1))
    print(a1,':',enc_a1)

    enc_a2=bytes(a2,encoding='utf-8')
    enc_a2= sm3.sm3_hash(func.bytes_to_list(enc_a2))
    print(a2,':',enc_a2)

