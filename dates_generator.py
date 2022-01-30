"""
Author: @pythonistabr
contact: gustavo.oceanografia@gmail.com

"""
from copy import copy
from datetime import datetime 
from datetime import timedelta

class DatesGenerator:
    
    def __init__(self):
        self._items = []

    def generateDates(self, date_min, date_max, time_step):
        self.date_min = date_min
        self.date_max = date_max
        self.time_step = time_step
        self.date1 = datetime.strptime(self.date_min,'%Y-%m-%d')
        self.date2 = datetime.strptime(self.date_max,'%Y-%m-%d')

        self.range_of_dates = self.date2 - self.date1
        self.range_of_dates = str(self.range_of_dates)
        self.range_of_dates = self.range_of_dates[0: self.range_of_dates.find(' ')+1]
        self.range_of_dates = int(self.range_of_dates) // self.time_step

        date1 = copy(self.date1)

        for ii in range(0, self.range_of_dates):

            date2 = date1 + timedelta(days = self.time_step)

            date1_formated = '{}-{:02d}-{:02d}'.format(date1.year,
            date1.month, date1.day )
            
            date2_formated = '{}-{:02d}-{:02d}'.format(date2.year,
            date2.month, date2.day )
        
            self._items.append((date1_formated, date2_formated))
            
            date1 = date2

        return self._items

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)
    

    def __getitem__(self, index):
        return self._items[index]
 
    
    def __str__(self):
        length = len(self._items)
        return "Date List has {} items".format(length)
    
    
    

def main():
    myobject = DatesGenerator()
    myobject.generateDates('2017-10-01','2017-12-31', 7)
    
    for ii in myobject:
        print(ii)
    
    print(myobject)
    
if __name__ == "__main__":
    main()
