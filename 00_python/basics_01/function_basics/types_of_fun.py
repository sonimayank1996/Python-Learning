#pure function
def pure_Fun(cups):
    return cups*10

total_chai=10

# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups

#Recursive functions
def pour_chai(n):
    if n==0:
        return
    return pour_chai(n-1)

#lambdas
chai_type = ["light", "dark", "kadak", "Sweet"]

strong_chai = filter(lambda val: val == "kadak", chai_type)
print("Strong", list(strong_chai))