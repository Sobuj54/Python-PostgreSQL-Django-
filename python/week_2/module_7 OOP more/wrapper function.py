def outside():
    print("outside function")
    def inside():
        print("inside function")
    return inside

outside()()