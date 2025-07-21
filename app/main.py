class SoftwareEngineer:
    def __init__(self, name: str, skills: list[str] = []) -> None:
        self.name = name
        self.skills = skills

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str,
                 skills: list[str]= ["JavaScript", "HTML", "CSS"]) -> None:
        super().__init__(skills)
        self.skills = skills
        self.name = name

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str,
                 skills: list[str] = ["Python", "SQL", "Django"]) -> None:
        super().__init__(skills)
        self.skills = skills
        self.name = name

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str,
                 skills: list[str] = ["Java", "Android studio"]) -> None:
        super().__init__(skills)
        self.skills = skills
        self.name = name

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str,
                 skills: list[str] = ["Python", "SQL", "Django", "JavaScript", "HTML", "CSS"]) -> None:
        super().__init__(skills)
        self.skills = skills
        self.name = name

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()







