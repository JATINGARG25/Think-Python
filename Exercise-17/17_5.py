class Time:
    #opertaor overloading
    def __add__(self, other):
        # seconds = self.time_to_int() + other.time_to_int()
        # return int_to_time(seconds)
        pass

start = Time()
end = Time()

print(start+end)  # + sign is the operator overloading -- it invokes the add function by using + operator



