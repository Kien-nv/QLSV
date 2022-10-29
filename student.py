# ----------------------------------Create class person----------------


class person():

    # def showinfor(self):
    #     print(f"[{self.name}, {self.gender}, {self.age}]")
    def __init__(self, name=None, gender=None, age=None, address=None):
        self.name=name
        self.gender=gender
        self.age=age
        self.address=address
    def input_infor(self):
        self.name=input("Name: ")
        self.gender=input("Gender: ")
        self.age=input("Age: ")
        self.address=input("Address: ")
    def show_infor(self):
        return(f"'Name:'{self.name},'Gender:' {self.gender},'Age:' {self.age},'Address:' {self.address}")

#------------ Viet lop student kế thừa lớp person
 
class student(person):
    def check(self):
        if (self.Diem_TB)>=8:
            print("Student ability for scholaship")
            # ---------Overide hàm input_infor
            # name=None, gender=None, age=None, address=None,
    def __init__(self,  ID=None, Diem_TB=None, email=None):
        # super().__init__(name, gender, age, address)
        self.ID=ID
        self.Diem_TB=Diem_TB
        self.email=email
    def input_infor(self):
        super().input_infor()
        self.ID=input("ID: ")
        if len(self.ID)!=8:
            print("ID cần có đủ 8 ký tự")           
        self.Diem_TB=float(input("Diem: "))
        if 0.0 >(self.Diem_TB) or (self.Diem_TB)>10.0:
            print("Diem trung bình có thang điểm 10")
        self.email=input("Email: ")
        if not self.email:
            print("Please enter email address")
        if " "in self.email:
            print("Địa chỉ email, phải không được có dấu cách")
        if "@" not in self.email:
            print("Địa chỉ email phải chưa ký tự @")
    def show_infor(self):
       return super().show_infor() , (f"'ID:'{self.ID},'Gender:' {self.Diem_TB},'Age:' {self.email}")
 
        
kien=student()
kien.input_infor()
print(kien.show_infor())
kien.check()
        



