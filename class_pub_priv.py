class A:
    def pub(self):
        print('Public method.', self.__class__.__name__)

    def __priv(self):
        print('Private method.', self.__class__.__name__)

    def both(self):
        self.pub()
        self.__priv()


a = A()
a.both()



# class B(A):
#     def hello(self):
#         self.pub()
#         # self.__priv()
#         self.both()