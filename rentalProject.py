# nested dictionary
dict = {
        '44101': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.01  }, 
        '44102': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.0115}, 
        '44103': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.0115},
        '44104': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.0115},
        '44105': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.0115},
        '44106': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.0115},
        '44107': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.0115},
        '44108': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.0115},
        '44109': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.0115},
        '44100': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.0115},
        '44111': {'vacancy': 0.05, 'eviction': 0.05, 'propertyRate': 0.0115},
        '44112': {'vacancy': 0.05, 'eviction': 0.11, 'propertyRate': 0.0115},
        '44113': {'vacancy': 0.05, 'eviction': 0.13, 'propertyRate': 0.0115},
        '44114': {'vacancy': 0.10, 'eviction': 0.11, 'propertyRate': 0.0115},
        '44115': {'vacancy': 0.10, 'eviction': 0.12, 'propertyRate': 0.0115},
        '44117': {'vacancy': 0.10, 'eviction': 0.09, 'propertyRate': 0.0115},
        '44119': {'vacancy': 0.10, 'eviction': 0.11, 'propertyRate': 0.0115},
        '44120': {'vacancy': 0.10, 'eviction': 0.12, 'propertyRate': 0.0115},
        '44121': {'vacancy': 0.10, 'eviction': 0.12, 'propertyRate': 0.0115},
        '44122': {'vacancy': 0.10, 'eviction': 0.09, 'propertyRate': 0.0115},
        '44126': {'vacancy': 0.10, 'eviction': 0.04, 'propertyRate': 0.0115},
        '44127': {'vacancy': 0.10, 'eviction': 0.07, 'propertyRate': 0.0115},
        '44128': {'vacancy': 0.10, 'eviction': 0.17, 'propertyRate': 0.0115},
        '44129': {'vacancy': 0.10, 'eviction': 0.12, 'propertyRate': 0.0115},
        '44134': {'vacancy': 0.10, 'eviction': 0.12, 'propertyRate': 0.0115},
        '44135': {'vacancy': 0.10, 'eviction': 0.09, 'propertyRate': 0.0115},
        '44142': {'vacancy': 0.10, 'eviction': 0.27, 'propertyRate': 0.0115},
        '44144': {'vacancy': 0.10, 'eviction': 0.18, 'propertyRate': 0.0115},
}

#These are global variables and are going to be the same, no matter which property is evaluated
incomeTaxRate = 0.25
propertyManageRate = 0.06

"""
I have created a model to evaulate the ROI for multifamily properties in Cleveland, OH.  When you purchase a property, 
the seller provides a financial model thay often understate the costs of operating the building by not taking into 
account: (1) cities set the taxable value to the purchase price and which is almost always higher than what the seller is 
currently paying (2) repair costs are often understated and don't match tax statements; and (3) property management are 
often not disclosed because the seller may operate themselves and (4) capital will need to be spent upfront in order to 
address maintenance issues often deferred by a seller who was reluctant to make investment in a property for sale.

For the building I'm evaulating please use the following inputs, but feel free to use your own so long as you enter 
a Cleveland OH Zip Code

1) annual rent is 100,000 2) laundry is 3,000 3) annual utility is 18,300 4) offer to seller is 630,000 
5) anticipate closing costs are $30,000 6) number of units is 18 7) monthly mortgage is $2,500 8) insurance is 
4,700 9) annual repairs are 6000 and 10) property zip code is 44102

"""


class Rental:

    def __init__(self, annualRent, laundry, utilities, propertyValue, closingCost, units, mortgage, insurance, repairs, zipCode):
        self.annualRent = annualRent
        self.laundry = laundry
        self.utilities = utilities
        self.propertyValue = propertyValue
        self.closingCost = closingCost
        self.mortgage = mortgage
        self.insurance = insurance
        self.repairs = repairs
        self.zipCode = zipCode
        self.units = units
    
    def getRevenue(self):
        #vacancy rate is indexed by zip code
        self.revenue = self.annualRent * (1-dict[self.zipCode]['vacancy']) + self.laundry
        return self.revenue

    def getTotalExpenses(self):
        #adjust for evictions. assume $600 cost per eviction.  Cost to pay attorney and remain unoccupied.  Net against deposits.
        #property taxes based on city statutory rate in dict multiplied by purchase price
        propertyTax =  self.propertyValue * dict[self.zipCode]['propertyRate']
        evictionCost = self.units * dict[self.zipCode]['eviction'] * 600
        
        
        return self.utilities + propertyManageRate * self.annualRent + self.mortgage * 12 + self.insurance + propertyTax + evictionCost

    def getAcquisitionCost(self):
        return self.propertyValue + self.closingCost

    def getROI(self):
        
        #mortgage is assumed to be at 75% Loan to Value, or you're borrowing 75% of what's need to buy the building
        note = .75 * self.getAcquisitionCost()
        #The property, per IRS, is depreciated on a straightline basis over 27.5 years 
        cashFlow = self.getRevenue() - self.getTotalExpenses()  
        taxPayment = (self.getRevenue() - self.getTotalExpenses() + self.mortgage - (self.getAcquisitionCost() / 27.5)) * incomeTaxRate
        
        #there are two ways to calculate return.
           #the levered ROI for the property.  This takes in account the leverage used for purchase
           #the second is the unlevered return a/k/a cap rate.  Allows an apples to apple evalation of multiple properties
        return (cashFlow - taxPayment)/(self.getAcquisitionCost() - note), (cashFlow - taxPayment + self.mortgage * 12) / (self.getAcquisitionCost())
        
        
rentalList = []
annualRent=[]
laundry=[]
utilities=[]
propertyValue=[]
closingCost=[]
units=[]
mortgage=[]
insurance=[]
repairs=[]
zipCode=[]

numberProperties=int(input('How many properties are you evaluating? \n'))

for i in range(numberProperties):
    print("What is your annual rent roll for Building ",i,"?")
    annualRent.append(int(input()))
    print("what is your laundry revenue for Building ",i,"?")
    laundry.append(int(input()))
    print("What are your annual utility expenses for Building ",i,"?")
    utilities.append(int(input()))
    print("What are you prepared to offer the Seller for Building ",i,"?")
    propertyValue.append(int(input()))
    print("What are your anticipated closing costs (should range from 3-6% of offer) for Building ",i,"?")
    closingCost.append(int(input()))
    print("How many units in the building for Building ",i,"?")
    units.append(int(input()))
    print("How much is monthly mortgage payment (interest only) for Building ",i,"?")
    mortgage.append(int(input()))
    print("What is your annual insurance premium for Building ",i,"?")
    insurance.append(int(input()))
    print("What is your annual repair costs for Building ",i,"?")
    repairs.append(int(input()))
    print("What is the property zip code (MUST be in CLEVELAND, OH) for building ",i,"?")
    zipCode.append(input())
    rentalList.append(Rental(annualRent[i], laundry[i], utilities[i], propertyValue[i], closingCost[i], units[i], mortgage[i], insurance[i], repairs[i], zipCode[i]))

for i, rental in enumerate(rentalList):
    Madison,b =rental.getROI()
    print(f"Your levered ROI on the building is {i} is {Madison}")
    print(f"Your unlevered return on the building is {i} is {b}")
    