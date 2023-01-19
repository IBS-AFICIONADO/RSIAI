import time

class Timer:

    def __init__(self, work_length):
        #work length = tuple(H,M,S)
        self.work_time = work_length[0] * 3600 + work_length[1] * 60 + work_length[2]
        self.start_time = time.time()
        pass


    def seconds(self):
        if time.time() - self.start_time > self.work_time:
            self.start_time = time.time()
            return True
        else:
            time.sleep(5)
            return(self.seconds())