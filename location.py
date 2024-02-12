class Location:

    def __init__(self,address: String,city: String,state:String,zipcode:Long):
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def get_location()->object:
        return Location(self.address,self.city,sefl.state,self.zipcodes)