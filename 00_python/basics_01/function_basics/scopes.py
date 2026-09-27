def serve_chai():
    chai_type="Masala" #local scope
    print("chai", chai_type)

chai_type="Ginger"
serve_chai()
print("chai", chai_type)

def chai_counter():
    chai_order = "Lemon" #Enclosing scope

    def print_order():
      chai_order = "Ginger" 
      print("chai", chai_order)
    print_order()
    print("Outer", chai_order)

chai_order = "Tulsi" #Global scope
chai_counter()
print("Global", chai_order)



