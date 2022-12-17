def str_numbers(num_str):
    s = (('one','odin','odna',1),('dva','two',2),('tri','three',3),('chetyre','four',4),('pyat','five',5),\
        ('six','shest',6),('sem','seven',7),('vosem','eight',8),('devyat','nine',9),('desyat','ten',10),\
        ('odinnadcat','eleven',11),('dvenadcat','twelve',12),('trinnadcat','thirteen',13),('chetyrnadcat','fourteen',14),('pyatnadcat','fifteen',15),\
        ('sixteen','shestnadcat',16),('seventeen','semndadcat',17),('vosemnadcat','nineteen',18),('devyatnadcat','nineen',19),('dvadcat','twenty',20),\
        ('thirty','tridcat',30),('fourty','sorok',40),('fifty','pyatdesyat',50),('shestdesyat','sixty',60),('semdesyat','seventy',70),\
        ('eighty','vosemdesyat',80),('devyanosta','ninety',90),('devyatsot',900))
    for i in s:
        if num_str in i:
            return i[-1]
    return 0

def str_counter(n_str):
    n_list = n_str.split()
    current_num = 0
    while len(n_list) != 0:
        word = n_list.pop(0)
        if word in 'billion':
            current_num*=1000000000
        if word in 'million':
            remainder_million = current_num%1000000
            current_num+=(remainder_million*1000000)-remainder_million
        if word in 'thousand':
            remainder_thausands=current_num%1000
            current_num+=(remainder_thausands*1000)-remainder_thausands 
        if word in 'tysyacha':
            remainder_thausands=current_num%1000
            current_num+=(remainder_thausands*1000)-remainder_thausands 
        if word in 'hundred':
            remainder_hundred=current_num%100
            current_num+=(remainder_hundred*100)-remainder_hundred
        if word in 'sto':
            remainder_hundred=current_num%100
            current_num+=(remainder_hundred*100)-remainder_hundred
        else:
            current_num+=str_numbers(word)
    return current_num
num_str = input('type your number: ')
print((str_counter(num_str)))

