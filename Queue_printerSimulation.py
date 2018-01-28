from Queue import Queue
import random

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
        
    def get_stamp(self):
        return self.timestamp
        
    def get_pages(self):
        return self.pages
        
    def wait_time(self, current_time):
        return current_time - self.timestamp

class Printer:
    def __init__(self,ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
        
    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate
            
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
        
    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            
            if self.time_remaining <= 0:
                self.current_task = None

def simulation(num_seconds, pages_per_minutes):
    lab_printer = Printer(pages_per_minutes)
    print_queue = Queue()
    waiting_times = []
    
    for current_second in range(num_seconds):
       
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)
            
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
            
        lab_printer.tick()
        
    average_wait = sum(waiting_times) / len(waiting_times)
    print("AVg wait %6.3f secs %3d tasks remainig %d total tasks."\
            %(average_wait,print_queue.size(),len(waiting_times)))
        
        
def new_print_task():
    num = random.randrange(1, 61)
    if num == 60:
        return True
    else:
        return False
        
for i in range(10):
    simulation(3600, 10)
print'='*50
for i in range(10):
    simulation(3600, 5)
