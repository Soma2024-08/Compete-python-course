'''
# Implicit Conversion :-> python automatically converts smaller data types to larger ones to prevent data loss.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''
# Example of implicit conversion
num_int = 123          # integer
num_flo = 123.456      # float

num_new = num_int + num_flo
print("Data type of num_int:", type(num_int))
print("Data type of num_flo:", type(num_flo))   
print("Value of num_new:", num_new)
print("Data type of num_new:", type(num_new))

'''
# Explicit Conversion :-> when we convert data types manually using predefined functions like int(), float(), str() etc. 

 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 '''
# Example of explicit conversion

x = "12"   #string      
y=int(x)    # converting string to integer
print(y+5)