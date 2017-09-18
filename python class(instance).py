class employee():
  def __init__(self, first,last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first+last+"@email.com"
  def fullname(self):
    return print("{}{}".format(self.first,self.last))
  def email(self):
    return "{}".format(self.pay)
emp1 = employee("s",'salekin','500k')
print(employee.email(emp1))
