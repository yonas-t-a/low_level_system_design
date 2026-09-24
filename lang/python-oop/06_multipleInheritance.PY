class Logger:
    def log(self, message:str) -> None:
        print(f"[lOG]: {message}")
    def warn(self, message: str) -> None:
        print(f"[LOG WARNING]: {message}")
        
class Saveable:
    def save(self) -> None:
        print("[SAVE]: object Saved")
    def warn(self, message: str) -> None:
        print(f"[SAVE WARNING]: {message}")


class User(Logger, Saveable):
    def __init__(self, name):
        self.username = name
        
    def update_username(self, newName):
        oldName = self.username
        self.username = newName
        
        Logger.warn(self, "Logging...")
        self.log(f"User: {oldName} has changed his name to {self.username}")
        
        Saveable.warn(self, "Saving...")
        self.save()
        
if __name__ == "__main__":
    user = User("Luke")
    user.update_username("Greenwood")