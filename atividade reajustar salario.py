n= float(input("Digite seu salário: "))
s1= n * 15/100
s2= n * 10/100
s3= n * 5/100

if n<= 500:
    print ("Seu salário atual é de ", n,", e com os descontos você passará a receber: ", n+s1)
elif n<=1000:
    print ("Seu salário atual é de ", n,", e com os descontos você passará a receber: ", n+s2)
elif n > 1000:
    print ("Seu salário atual é de ", n,", e com os descontos você passará a receber: ", n+s3)