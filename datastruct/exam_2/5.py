class Queue:

    def __init__(self):
        self.data_list = []

    def enQueue(self, data):
        self.data_list.append(data)

    def deQueue(self):
        return self.data_list.pop(0)

    def __str__(self):
        return "[" + ", ".join(str(data) for data in self) + "]"

    def __iter__(self):
        for data in self.data_list:
            yield data

    def __add__(self, o):
        for data in o:
            self.enQueue(data)
        return self

    def __len__(self):
        return len(self.data_list)


if __name__ == "__main__":

    init_data, command = input("Enter Input : ").split("/")

    q = Queue()
    q += [int(d) for d in init_data.split()]

    command = command.split(",")
    for com in command:
        if com.upper() == 'D':
            q.deQueue()
        else:
            command_type, value = com.split()
            value = int(value)

            if command_type.upper() == 'E':
                q.enQueue(value)

    if len(set(q)) == len(q):
        print("NO Duplicate")

    else:
        print("Duplicate")
