
import json
from datetime import datetime

class Ency:
    def __init__(self, ency_data="ency_data.json", encryption_log="encryption_log.txt", text_output="text.txt"):
        self.ency_data = ency_data
        self.encryption_log = encryption_log
        self.text_output = text_output
        with open(self.ency_data, "r") as file:
            self.data = json.load(file)

        self.ency_status = self.data['ency']

    def get_ency_status(self):
        return self.ency_status

    def encrypt(self, key):
        while key == 0:
            raise ValueError("Key cannot be 0.")

        with open(self.text_output, "r") as file:
            text = file.read()

        encrypted_data = encrypt(text, key)
        ency_status = 1
        dump_data = {'ency': ency_status, 'data': encrypted_data}
        dump_out(dump_data,self.ency_data)
        write_to_text("",self.text_output)
        log_encrypt_info(encrypted_data,self.encryption_log)

    def decrypt(self, key):
        while key == 0:
            raise ValueError("Key cannot be 0.")
        decrypted_data = decrypt(self.data['data'], key)
        ency_status = 0
        dump_data = {'ency': ency_status, 'data': decrypted_data}
        dump_out(dump_data,self.ency_data)
        write_to_text(decrypted_data,self.text_output)
        print("Data decrypted.")

    def toggle(self,key):
        with open(self.ency_data, "r") as file:
            self.data = json.load(file)

        self.ency_status = self.data['ency']

        key = int(key)
        if self.ency_status == 1:
            self.decrypt(key)
        else :
            self.encrypt(key)

def log_encrypt_info(encrypted_data,log_path):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    print("data encrypted :", dt_string)
    log_str = "\n" + dt_string + " : " + encrypted_data + "\n"
    with open(log_path, "a") as file:
        file.write(log_str)


def encrypt(data, key):
    result = []
    for c in data:
        c_ascii = ord(c)
        result.append(c_ascii*key)
    return "-".join(str(c) for c in result)


def decrypt(data, key):
    result = []
    data = [int(d) for d in data.split('-')]
    for c in data:
        result.append(chr(int(c/key)))
    return "".join(c for c in result)


def dump_out(data,dump_path):
    with open(dump_path, "w") as file:
        json.dump(data, file)


def write_to_text(data,text_output_path):
    with open(text_output_path, "w") as file:
        file.write(data)

import hashlib

if __name__ == "__main__":

    new = Ency()