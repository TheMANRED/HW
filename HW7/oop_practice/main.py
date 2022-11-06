# from Controller import Controller
#
# controller = Controller
# controller.menu()


# --------------------------------------------------------------------------------------------------------------------


# 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """
# class Concert:
#     def __new__(cls, *args, **kwargs):
#         max_visitors_num = None
#         visitors_count = None
#         return super(Concert, cls).__new__(cls)
#
#     # def __init__(self):
#     #     visitors_count = None
#     #
#     #     if max_vistors_num < self.visitors.count
#
#
#     # def visitors_count(self, visitors_count):
#     #     self.visitors_count = visitors_count
#     #
#     #     if self.max_visitors_num < visitors_count:
#     #         self.visitors_count = self.max_visitors_num
#     #         return self.max_visitors_num
#     #     else:
#     #         return visitors_count
#
#
# Concert.max_visitor_num = 50
# concert = Concert()
# concert.visitors_count = 1000
# print(concert.visitors_count)  # 50

# concert = Concert(50)
# print(concert.visitors_count(30))


class Concert:
    max_visitor_num = None

    def __setattr__(self, key, value):
        if key == "visitors_count" and value < self.max_visitor_num:
            return object.__setattr__(self, key, value)
        else:
            return object.__setattr__(self, key, self.max_visitor_num)


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 30
print(concert.visitors_count)
