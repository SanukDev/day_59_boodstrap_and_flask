import requests

class Post:
    def __init__(self, id):
        self.id = id
        self.response = requests.get(url="https://api.npoint.io/51e4bf5f576774206625")
        self.title = ""
        self.body = ""
        self.subtitle = ""


    def collect_title(self):
        data = self.response.json()
        for post in data:
            if post['id'] == self.id:
                self.title = post['title']
        return self.title

    def collect_body(self):
        data = self.response.json()
        for post in data:
            if post['id'] == self.id:
                self.body = post['body']
        return self.body

    def collect_subtitle(self):
        data = self.response.json()
        for post in data:
            if post['id'] == self.id:
                self.subtitle = post['subtitle']
        return self.subtitle

    def data(self):
        data = self.response.json()
        return data


teste = Post(1)
data = teste.data()

print(data)