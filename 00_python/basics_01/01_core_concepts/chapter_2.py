is_Editable=True
str_count=9

print(f"Str count is:- {str_count+is_Editable}")  #upcasting of boolean to integer

milk_present=1
print(f"Milk present is:- {bool(milk_present)}")  #0 is considered as False

# logical operators = and, or, not
a=True
b=False
c = a and b  #False
d = a or b   #True
e = not a    #False
print(f"Logical AND of a and b is:- {c} {d} {e}")
