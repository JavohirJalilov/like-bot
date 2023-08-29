import json

class LikeDB:
    def __init__(self, file_path):
        self.file_path = file_path

        try:
            with open(file_path, 'r') as f:
                self.data = json.load(f)
        except:
            self. data = {}


    def add_user(self, chat_id: str):
        data = self.data
        if chat_id not in data.keys():
            data[chat_id] = {
                "like": 0,
                "dislike": 0
            }
        
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

        return data
    
    def add_like(self, chat_id: str):
        data = self.data
        data[chat_id]['like'] += 1

        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

        return data

    def add_dislike(self, chat_id: str):
        data = self.data
        data[chat_id]['dislike'] += 1

        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

        return data

    # def save(self, data):
    #     with open(self.file_path, 'w') as f:
    #         json.dump(data, f, indent=4)

