from abc import abstractmethod, ABC


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class MyReceiver(IContent):

    def format(self):
        return ''.join(["I'm ", self.text])


class MySender(IContent):

    def format(self):
        return ''.join(["I'm ", self.text])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class Email(IEmail):

    def __init__(self):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.format()

    def set_receiver(self, receiver):
        self.__receiver = receiver.format()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


sender = MySender('Valentin')
receiver = MyReceiver('Valentin')
content = MyContent('Hello, There!')
my_email = Email()
my_email.set_sender(sender)
my_email.set_receiver(receiver)
my_email.set_content(content)
print(my_email)