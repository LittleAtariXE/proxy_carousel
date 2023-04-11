import os
from pathlib import Path

base_dir = str(Path(__file__).parent.parent) + '/output/'
print(base_dir)


class Collector:
    def __init__(self, base_dir=base_dir, limit=2048):
        self.base_dir = base_dir
        self.trash_dir = self.base_dir + 'trash/'
        self.trash_file = None
        self.limit = limit
        self.make_dirs()



    def make_dirs(self):
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        if not os.path.exists(self.trash_dir):
            os.makedirs(self.trash_dir)
        index = len(os.listdir(self.trash_dir))
        self.trash_file = f"{self.trash_dir}logs{str(index + 1)}.txt"
        with open(self.trash_file, "w") as f:
            f.write('')

    def trash_header(self, request_dict):
        if len(request_dict) == 0:
            return None
        out = "***" * 60 + "\n"
        for req in request_dict:
            out += "####" * 100 + "\n"
            out += "-" * 100 + "\n"
            out += f"TARGET: {req}\n" + "-" * 100 + "\n" 
            out += "*" * 100 + "\n"
            for d in request_dict[req]:
                out += f"PROXY: {d[1]}\n" + "-" * 100 + "\n"
                try:
                    resp = d[0].json()
                    out += str(resp) + "\n" + "-" * 100 + "\n"
                except:
                    resp = d[0].text
                    if len(resp) > self.limit:
                        resp = f"Response is too long. Over {self.limit} bytes"
                    out += str(resp) + "\n" + "-" * 100 + "\n"
                self.add_logs(self.trash_file, out)

    def add_logs(self, file, content):
        with open(file, 'a+') as f:
            f.write(content)
        



      

            

        

    




###########


