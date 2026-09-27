def update_order():
    chai_type="Elaichi"
    def kitchen():
        nonlocal chai_type #update the local
        chai_type="kesar"
    kitchen()
    print(f"After kitchen update", chai_type)

update_order()
    