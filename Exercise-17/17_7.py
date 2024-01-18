class Kangaroo():
    
    def __init__(self,name,contents = []):

        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents
    
    def put_in_pouch(self,item):
        self.pouch_contents.append(item)

    def __str__(self):
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)