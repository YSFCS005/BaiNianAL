import yaml,os


class ReadYaml():
    def __init__(self,filename):
        self.filepath=os.getcwd()+os.sep+"Data"+os.sep+filename

    def read_yaml01(self):
        with open(self.filepath,"r",encoding="utf-8")as f:
            return yaml.load(f)
    def read_yaml(self):
        with open("../Date/login.yaml","r",encoding="utf-8")as f:
            return yaml.load(f)
if __name__ == '__main__':
    """
        最重要的格式：
        return [("12345678899","123456"),(),()]
    """
    datas=ReadYaml("login_yaml").read_yaml()
    print(datas)
    arrs=[]
    for data in datas.values():
        arrs.append((data.get("username"),data.get("password")))
    print(arrs)
