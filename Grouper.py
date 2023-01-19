import math
import time


class Grouper:

    def __init__(self, employees, size):
        self.employees = employees
        self.group_size = size
        self.group_amount = math.ceil(len(self.employees) / self.group_size)
        #given in tuple(hours,minutes,seconds)
        self.work_time = time
        self.groups = dict()
        self.group_key = 0

    #call everytime a new employee signs in
    def assign_to_group(self,employee):
        if self.group_key not in self.groups:
            self.groups[self.group_key] = [employee]
        else:
            self.groups[self.group_key].append(employee)
        if len(self.groups[self.group_key]) == self.group_size:
            self.group_key += 1

    def start_timer(self):
        if the group is full start timer for group could go in main