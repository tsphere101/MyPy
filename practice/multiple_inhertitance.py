class Camera:
    def take_photo(self):
        print("take a photo")

    def delete_photo(self):
        print("delete a photo")


class Phone:
    def call(self, number):
        print(f"calling {number}")

    def send_sms(self, number, message):
        print(f"sending {message} to {number}")


class SmartPhone(Camera, Phone):
    pass


if __name__ == "__main__":
    s = SmartPhone()
    s.take_photo()
    s.delete_photo()
