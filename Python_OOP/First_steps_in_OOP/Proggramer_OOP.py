class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, course_language, skill):
        if course_language == self.language:
            self.skills += skill
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {course_language}"

    def change_language(self, new_language, skill):
        if new_language == self.language:
            return f"{self.name} already knows {new_language}"
        elif skill <= self.skills:
            the_print = f"{self.name} switched from {self.language} to {new_language}"
            self.language = new_language
            return the_print
        else:
            return f"{self.name} needs {skill - self.skills} more skills"






programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
