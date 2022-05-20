#Q3. Program to check if a string contains anyspecil character.

import re 
  

def check_splcharacter(test): 
  

 
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
      
    
     
    if(string_check.search(test) == None): 
        print("statement is accepted.")
          
    else: 
        print("statement is not accepted.") 
      
  
 
if __name__ == '__main__' : 
      
    
 
    given_statement = input("enter the statement : ")
      
    
  
    check_splcharacter(given_statement) 
 

