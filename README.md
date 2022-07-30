# rho_birthday_attack
# 项目说明

**1.小组成员**：周睿泽。git账户名称：RuizeZhou

**2,所作项目名称：**

本项目名称为：Project:  implement the Rho method of reduced SM3

简介：实现SM3的生日攻击（优化版），编程语言为python。

完成人：周睿泽

**3.清单：**

完成的项目：

√Project: implement the naïve birthday attack of reduced SM3 

√Project: implement the Rho method of reduced SM3

√Project: implement length extension attack for SM3, SHA256, etc.

√Project: do your best to optimize SM3 implementation (software)

√Project: Impl Merkle Tree following RFC6962

√Project: report on the application of this deduce technique in Ethereum with ECDSA

√Project: Implement sm2 with RFC6979

√Project: verify the above pitfalls with proof-of-concept code

√Project: Implement a PGP scheme with SM2

未完成的项目：

Project: Try to Implement this scheme

Project: Implement the above ECMH scheme

Project: implement sm2 2P sign with real network communication

Project: implement sm2 2P decrypt with real network communication

Project: PoC impl of the scheme, or do implement analysis by Google

Project: forge a signature to pretend that you are Satoshi

Project: send a tx on Bitcoin testnet, and parse the tx data down to every bit, better write script yourself

Project: research report on MPT

Project: Find a key with hash value “sdu_cst_20220610” under a message composed of your name followed by your student ID. For example, “San Zhan 202000460001”.

有问题的项目及问题：\

**4.本项目具体内容：**具体内容如下
Project: implement the Rho method of reduced SM3

A.具体的项目代码说明

​	改进的生日攻击中，空间复杂度降低。需要的存储仅仅是$x_i,x_{2i}$。随机选择输入$x_0$，计算$x_i=H^i(x_0),x_{2i}=H^{2i}(x_0)$，如果相等，说明$x_0,x_1,...x_{2i-1}$存在碰撞。找到最小的$j(0\leq j\leq i)$使得$x_j=x_{j+i}$，输出$x_{j-1},x_{j+i-1}$即可。

```
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

    for j in range(i+1):
        temp_slow=sm3.sm3_hash(func.bytes_to_list(bytes(enc_slow,encoding='utf-8')))
        temp_fast=sm3.sm3_hash(func.bytes_to_list(bytes(enc_quick,encoding='utf-8')))

        if temp_fast[0:length]==temp_slow[0:length]:
            return enc_slow,enc_quick
        else:
            enc_slow=temp_slow
            enc_quick=temp_fast
    return None,None
```




B.运行指导(跑不起来的不算成功)

​	已有本项目需要的库后直接运行即可。

C.代码运行全过程截图(无截图无说明的代码不给分)

​	设置lenth=8时，表示寻找前两位的碰撞，得到结果如下，第二行为两个产生哈希碰撞的消息，下面是这两个消息及其对应的哈希值：

![1659155646102](https://cdn.jsdelivr.net/gh/RuizeZhou/images/1659155646102.png)

依次增加lenth大小，得到碰撞位更多：

增加lenth值的大小，lenth=12,寻找前三位碰撞：

![1659153075998](https://cdn.jsdelivr.net/gh/RuizeZhou/images/1659153075998.png)

​	lenth=16，寻找前四位碰撞：

![1659153678168](https://cdn.jsdelivr.net/gh/RuizeZhou/images/1659153678168.png)


​	以此类推。

D.每个人的具体贡献说明及贡献排序(复制的代码需要标出引用)

​	本人负责全部。
