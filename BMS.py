import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root", password="1234",database="bank_db")
cursor=conn.cursor()

class bank():
   def __init__(self):
    print("Bank Management System....")
    print("Connecting to the server...")
    self.home()

   def registration(self):
      name=input("Enter your Name: ")
      email=input("Enter your email: ")
      password=input("Enter your Password: ")
      
      self.save_reg_info_to_server( name, email, password)

   def save_reg_info_to_server(self,name,email,password):
     
     query= "insert into user(name, email, password) values(%s,%s,%s);"
    
     cursor.execute(query, (name, email, password))
     conn.commit()
     cursor.execute("select * from user where name=%s and email=%s and password=%s;",(name, email, password))
     
     user_data=cursor.fetchone()
     print("account_no", user_data[0],  "name", user_data[1])
     print("Registered Successfully....")


   def dashboard_portal(self):
     print("Dashboard Portal...")
     while True:
        choice=input('''1: Check Balance
                    2: Withdraw
                    3: Deposit
                    4: Change Password
                    5: Exit
                    ''')
        if choice=="1":
          print("your current balance is:" , self.check_bal())
        elif choice=="2":
         self.withdraw()
        elif choice=="3":
         self.deposit()
        elif choice=="4":
          self.update_password()
        elif choice=="5":
          exit()
        else:
          print("Invalid Choice Try Again...")
   
   def check_bal(self):
     cursor.execute("select balance from user where email=%s and password= %s; ",(self.email, self.password))
     current_bal=cursor.fetchone()[0]
     return current_bal
   
   def withdraw(self):
     try:
         amount=float(input("Enter Withdrawal amount: "))
         
         if amount>self.check_bal():
           print("Your account does not have sufficient amount Try Again..")
         elif amount<0:
           print("negative amount can not be withdrawn Try Again..")
         else:
           cursor.execute("update user set balance= balance - %s where email=%s and password= %s;",(amount, self.email, self.password))
           conn.commit()
                    
           print("Amount {amount} Withdrawn successfully..")
           print("your current balance is: ", self.check_bal())
     except:
       print("amount entered invalid...")
   
   def deposit(self):
    try:
        amount=float(input("Enter Amount to Deposit:  "))
        
        if amount<0:
          print("negative amount can not be entered")
        else:
           cursor.execute("update user set balance=balance + %s where email=%s and password= %s;",(amount, self.email, self.password))
           conn.commit()
           print("amount deposited successfully...")
           print("your current balance is : ", self.check_bal())
    except:
        print("Incorrect Amount Entered")
       
   def update_password(self):
     self.newpass=input("enter the new password: ")
     cursor.execute("update user set password = %s where email=%s and password=%s;", (self.newpass, self.email,self.password))
     conn.commit()
     print("your password has been updated.. new password=", self.checkpass())
 
   def checkpass(self):
     cursor.execute("select password from user where email=%s and password=%s;",(self.email,self.newpass))
     return cursor.fetchone()[0]
   
   def login(self):
     self.email=input("Email: ")
     self.password=input("Password: ")

     cursor.execute("select * from user where email=%s and password=%s;",(self.email,self.password))
     
     user_data=cursor.fetchone()

     if not user_data:
       print("email or password is wrong...")
     else:
       self.dashboard_portal()

   def home(self):
     print("Home Panel....")
     while True:
        choice=input('''1: Register
    2: Login
    3: exit 
        '''
             ) 
        if choice=="1":
         self.registration()
        elif choice=="2":
         self.login()
        elif choice=="3":
         exit()
        else:
          print("Invalid Choice") 

def main():
     bank()
if __name__ == '__main__':
    main()