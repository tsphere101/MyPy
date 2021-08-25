import time


class Frame:
    def __init__(self, seqno=None, data=None):
        self.seqno = seqno
        self.data = data

    @property
    def seqno(self):
        return self.seqno

    @seqno.setter
    def seqno(self, value):
        self.seqno = value

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, value):
        self.data = value


class Ack:
    def __init__(self, seqnum=None):
        self.seqnum = seqnum


class Medium:
    def __init__(self):
        self.data = []

    def get_data(self):
        return self.data.pop(0)

    def send_data(self, data):
        self.data.append(data)

    def peek(self):
        return self.data

    def has_data(self):
        return len(self.data) != 0



class Sender:

    def __init__(self,medium=None):
        self.medium = medium
        self.storage = [Frame(),Frame()]
        self.sn = 0

    def make_frame(self,data):
        frame = Frame(self.sn,data)
        self.storage[self.sn](frame)

    def send(self,medium:Medium):
        medium.send_data(self.storage[self.sn])
        self.sn = (self.sn+1)%2

    def store_frame(self,data:Frame):
        self.storage[data.seqno] = data

    def purge_frame(self,seqno):
        self.storage.pop(seqno)

    def start_timer(self):
        self.t1 = time.time()

    def stop_timer(self):
        self.t2 = time.time()
        return self.t2-self.t1

    def get_elapse_time(self):
        t2_temp = time.time()
        return t2_temp - self.t1

class Receiver:
    
    def __init__(self,medium = None):
        self.medium = medium
        self.storage = []

    def receive(self,frame):
        self.storage.append(frame)

    def send_ack(self,ack):
        



    

