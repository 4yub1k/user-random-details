# user-random-details
generate random and custom Email, password, phone number for users with custom rows.\
_Multiprocessing used so, increase the rows_lines as you want._
Data for **"1000000"** users.

**Options:**
```
rows_lines=1000000 //TOTAL ROWS/ENTRIES
password_length=20 //PASSWORD LENGTH
domain_names=['@yahoo.com','@gmail.com','@outlook.com'] //DOMAIN NAMES TO BE USED IN EMAILS
names_file='names.txt' //USE YOUR CUSTOM NAMES IN EMAILS
```
**Output:**
```
Time Pass : 12.061115999997128 seconds          //Time taken by function to generate Passwords
Time Email: 15.092245699997875 seconds          //Time taken by function to generate Emails
Time Phone : 17.01016879999952 seconds          //Time taken by function to generate Phone numbers
Time Email: 20.70942769999965 seconds           //Time taken by function to generate Emails
Time Main: 25.5371324000007 seconds             //Total time taken by script, "(12+15+17+20)=64 seconds", completed in 25 seconds

        Emails size : 21158.26 KB
        Custom Emails size : 24295.71 KB
        Passwords size : 10742.19 KB
        Phone size : 12695.31 KB
```
**Custom emails:**
```
AlejandrinaRivkah@yahoo.com
SamaraBlinnie@gmail.com
AngilCordula@gmail.com
ArleyneStarlene@outlook.com
BernettaWallis@gmail.com
```
**Random Emails:**
```
62rtw29k8@outlook.com
9hrqmdbtv@outlook.com
ai737.bio@yahoo.com
5tdu8d7tp@gmail.com
i5cma2eyv@outlook.com
```
**Random Password:(don't use random in production apps)**
```
w0buwifb_
*do19[brx
'ql$%6709
[$mqp\h6[
f8]848,\;
```
**Random Phone Number:**
```
559-986-937
601-293-955
695-415-111
688-471-634
939-845-818
```
**Files created:**
```
"user_emails.txt"
"user_custom_emails.txt"
"user_passwords.txt"
"user_phone_number.txt"
```

_Use for educational purposes 😉_
