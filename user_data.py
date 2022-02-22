from random import sample,choices
from os.path import getsize,exists
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor

alpha='abcdefghijklmnopqrdtuvwxyz'
dot='._'
al=r'[];/.,][[\!@#$\'%^&*()_+""'
numerical='1234567890'

rows_lines=5
password_length=20
phone_pattern='12-230-22-111'
names_file='names.txt'
names=''

email=alpha+dot+numerical
password=alpha+al+numerical
domain_names=['@yahoo.com','@gmail.com','@outlook.com']

if exists(names_file): #don't use exception
    with open('names.txt','r') as file:
        names=file.readlines()

class Details():
    def custom_emails(rows_lines,domain_names,names):
        t1=perf_counter()
        if exists(names_file):
            with open('user_custom_emails.txt','a') as file:
                for n in range(rows_lines):
                    first_name = sample(names, 1)[0].strip()
                    last_name = sample(names, 1)[0].strip()
                    domain = choices(domain_names, k=1)[0]
                    user_email="{0}{1}{2}".format(first_name,last_name,domain)
                    file.write(user_email+'\n')
        else:
            with open('user_custom_emails.txt','a') as file:
                file.write("Empty")

        t2=perf_counter()
        print("Time Custom Email: {} seconds ".format(t2-t1))
    def emails(rows_lines,email,domain_names):
        t1=perf_counter()
        with open('user_emails.txt','a') as file: 
            for n in range(rows_lines):
                user_email="".join(choices(email, k=9))+choices(domain_names, k=1)[0]  #k=1 only one output
                file.write(user_email+'\n')
        t2=perf_counter()
        print("Time Email: {} seconds ".format(t2-t1))
    def passwords(rows_lines,password,password_length):
        t1=perf_counter()
        with open('user_passwords.txt','a') as file:
            for n in range(rows_lines):
                user_pass="".join(choices(password, k=password_length))
                file.write(user_pass+'\n') 
        t2=perf_counter()
        print("Time Pass : {} seconds ".format(t2-t1))
    def phone(rows_lines,phone_pattern):
        t1=perf_counter()
        with open('user_phone_number.txt','a') as file:
            user_phone=''
            for n in range(rows_lines):
                for num in phone_pattern:
                    try:
                        if int(num): #use num.isnumeric() for short code
                            user_phone+=str(sample(range(0,9),1)[0])
                    except ValueError:
                        user_phone+=num
                file.write(user_phone+'\n')
                user_phone=''
                
        t2=perf_counter()
        print("Time Phone : {} seconds ".format(t2-t1))

def main_program(rows_lines):
    t1=perf_counter()
    with ProcessPoolExecutor() as exe:
        exe.submit(Details.emails, rows_lines,email,domain_names)
        exe.submit(Details.passwords, rows_lines,password,password_length)
        exe.submit(Details.phone, rows_lines,phone_pattern)
        exe.submit(Details.custom_emails, rows_lines, domain_names, names)
    t2=perf_counter()
    print("Time Main: {} seconds ".format(t2-t1))

    size = '''
        Emails size : {0:.2f} KB
        Custom Emails size : {1:.2f} KB
        Passwords size : {2:.2f} KB
        Phone size : {3:.2f} KB'''.format(getsize("user_emails.txt")/(1024),
            getsize("user_custom_emails.txt")/(1024),
            getsize("user_passwords.txt")/(1024),
            getsize("user_phone_number.txt")/(1024))

    print(size)
if __name__=="__main__":
    main_program(rows_lines)
