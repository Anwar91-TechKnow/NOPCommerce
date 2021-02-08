import configparser

Config = configparser.RawConfigParser()
Config.read(".//Configuration//config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url= Config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=Config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = Config.get('common info', 'password')
        return password

class metadata():
        @staticmethod
        def projectName():
            project = Config.get('metadata', 'Project Name')
            return project

        @staticmethod
        def tester():
            Tester1 = Config.get('metadata', 'Tester')
            return Tester1

        @staticmethod
        def module():
            module1 = Config.get('metadata', 'Module Name')
            return module1