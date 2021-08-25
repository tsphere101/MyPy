
import services as service
import time




if __name__ == '__main__':
    
    # A is sender
    # B is receiver
    MEDIUM = service.Medium()
    A = service.Sender(MEDIUM)
    B = service.Receiver(MEDIUM)

    A.request_to_send = ["A","B",5]
    A.request_to_send = [service.Frame(0,"A")]

    while (True):
        print("===Loop===")

        # Start code here

        if A.request_to_send != []:
            A.make_frame(A.request_to_send.pop(0))
            A.send(MEDIUM)

        if MEDIUM.has_data():
            print(MEDIUM.peek())

        if MEDIUM.has_data():
            frame = MEDIUM.get_data()
            B.receive(frame) 
            B.send_ack()


        









        # Delay
        time.sleep(1)

    