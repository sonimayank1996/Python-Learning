def make_chai():
    print("Hi")

return_value = make_chai() # Nothing => implicitly retern None
print(return_value)

def chai_prepare(size):
    if size==0:
        return "No chai"  #early return
    return "Chai is ready"

chai_prepare(0)

def chai_report():
    return 1,2  #mulitple return

print(chai_report())
first, second = chai_report()
print(first, second)

