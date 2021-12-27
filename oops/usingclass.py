class Cat:
    #name='tom'
    #breed='house cat'
    #color='gray'
    def __init__(self,name,breed,color):

         self.name = name
         self.breed = breed
         self.color = color
    def speak(self):
        print(self.name+' speaks')
        
mycat= Cat('Tom','House cat','gray')
print(mycat.color)
print(mycat.name)
mycat.speak()




mycat2=Cat('Snowbell','Classic Russian','White')
print(mycat2.name)
print(mycat2.color)
print(mycat2.speak())
