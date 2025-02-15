class MF:
    def __init__(self, message: str):
        self.message = message

    def AS(self):
        return f"*** {self.message.upper()} ***"

    def DSPLY(self):
        print(self.AS())

def main():
    GRTING = MF("Hello!")
    GRTING.DSPLY()

if __name__ == "__main__":
    main()
