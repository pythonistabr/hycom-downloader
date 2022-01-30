"""
Author: @pythonistabr
contact: gustavo.oceanografia@gmail.com
"""

# class Hycom Link Creator

from dates_generator import DatesGenerator
time_creator = DatesGenerator()

class Hycom_Link_Creator:
    
    def __init__(self, url, time_start, time_end, time_step):
        self._links = []
        
        self.url = url
        
        self.time_end = time_end
        
        self.time_step = time_step
        
        self.time_start = time_start

       
    def create_dates(self):
        self.dates = time_creator.generateDates(self.time_start,
        self.time_end, self.time_step)
        
        return self.dates
        
    def generate_urls(self):
        
        time_start_index = self.url.find('time_start')
        time_end_index = self.url.find('time_end')
        
        slice1 = self.url[0:time_start_index + len('time_start=')]
        slice2 = 'T12%3A00%3A00Z&time_end='

        slice3 = self.url[time_end_index +
            len('time_end=') + 
            len('yyyy-mm-dd'):]
        
        for date in self.dates:
            
            time_start = date[0]
            time_end = date[1]
            
            self._links.append(slice1 + time_start +
             slice2 + time_end + slice3)
        
        return self._links

    @property
    def links(self):
        return self._links
    
    def __iter__(self):
        return iter(self._links)
    
    def __next__(self):
        return next(self._links)
    
    def __len__(self):
        return len(self._links)
    
    def __getitem__(self, index):
        return self._links[index]

def main():
    
    with open('hycom-url.txt','r') as file:
        file = file.readlines()
    
    url = ''.join(file)

    mylist = Hycom_Link_Creator(url, '2017-02-01', '2017-06-01', 7)
    mylist.create_dates()
    mylist.generate_urls()
    
    for ii in mylist:
        print(ii)
    
    

if __name__ == "__main__":
    main()
