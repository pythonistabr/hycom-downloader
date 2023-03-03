"""
Author: @pythonistabr
contact: gustavo.oceanografia@gmail.com

"""
import numpy as np

class DatesGenerator:

    def generate_dates(self, date_min, date_max):
        
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
    
    def get_dates(self):
        return print(self._dates)
  

def main():
    
    myobject = DatesGenerator()
    myobject.generate_dates('2017-02-02','2017-02-28')
    myobject.get_dates()

if __name__ == "__main__":
    main()