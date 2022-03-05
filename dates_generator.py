"""
Author: @pythonistabr
contact: gustavo.oceanografia@gmail.com

"""
import numpy as np

class DatesGenerator:

    def generateDates(self, date_min, date_max):
        
        self._dates = np.arange(np.datetime64(date_min),
        np.datetime64(date_max),
        dtype='datetime64[D]')

        return self._dates

    @property
    def start_dates(self):
        return self._dates[0:len(self._dates):2]

    @property
    def end_dates(self):
        return self._dates[1:len(self._dates):2]
  

def main():
    
    myobject = DatesGenerator()
    myobject.generateDates('2016-12-02','2017-01-31')

    print(myobject.start_dates[0])
    print()
    print(myobject.end_dates[0])

    
    #print(myobject) 
if __name__ == "__main__":
    main() DatesGenerator:

    
if __name__ == "__main__":
    main()
