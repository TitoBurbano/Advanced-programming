class News:
    def __init__(self, message:str, sender: Optional[User] = None, recipient: Optional[User] = None):
        pass

    def send(self) -> None:
        pass

    def set_message(self, content: str) -> None:
        pass

    def get_recipient(self) -> Optional[User]:
        pass

    def notify_release(self, song: Song) -> None:
        pass

    def notify_shared(self, song: Song, sender: User, recipient: User) -> None:
        pass
    