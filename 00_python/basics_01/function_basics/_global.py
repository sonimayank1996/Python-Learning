chai_type="plain"

def front_desk():
    def kitchen():
        global chai_type #update the global
        chai_type="Irani"
    kitchen()

front_desk()
print("final chai", chai_type)