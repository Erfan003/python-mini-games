class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(username=data['username'], password=data['password'])