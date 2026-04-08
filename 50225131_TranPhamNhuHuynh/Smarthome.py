# Lớp Subscriber
#Đây là lớp chung cho tất cả thiết bị
#Có hàm update() để nhận thông báo
#pass nghĩa là “để trống cho lớp con tự định nghĩa”
class Subscriber: #lớp cha
    def update(self, message):  # phương thức nhận thông báo
        pass  # để lớp con override


# Publisher (SmartHub)
class SmartHub: #đây là bộ điều khiển trung tâm
    def __init__(self):
        self.devices = []  # danh sách thiết bị

    def attach(self, device):  
        self.devices.append(device)  # thêm thiết bị

    def detach(self, device):  
        self.devices.remove(device)  # xóa thiết bị

    def notify(self, event_type):  
        for device in self.devices:  # duyệt từng thiết bị
                device.update(event_type)  # gửi thông báo


# Thiết bị Light
#Chỉ quan tâm sự kiện trời tối
#Khi nhận → bật đèn
class Light(Subscriber):#Lớp  thiết bị tạo 1 lớp light
    def __init__(self):
        self.subscribed_events = ["Trời tối"]  # chỉ quan tâm sự kiện này

    def update(self, message):
        if message == "Trời tối":  # nếu trời tối
            self.on()  # bật đèn

    def on(self):
        print("Đè đã bật")  # hành động tự bật đèn khi trời tối


# Thiết bị Điều hòa
#Khi nóng → tự động làm mát
class AirConditioner(Subscriber):
    def __init__(self):
        self.subscribed_events = ["Nhiệt độ cao"]  # chỉ nhận nhiệt độ

    def update(self, message):
        if message == "Nhiệt độ cao":  # nếu nóng
            self.cool()  # bật làm mát

    def cool(self):
        print("Điều hòa đang làm mát")  # hành động làm mát


# Thiết bị Camera
#Khi không có người → bật ghi hình
class SecurityCamera(Subscriber):
    def __init__(self):
        self.subscribed_events = ["Vắng nhà"]  # chỉ nhận sự kiện này

    def update(self, message):
        if message == "Vắng nhà":  # nếu không có ai
            self.record_hd()  # bật ghi hình

    def record_hd(self):
        print("Ghi hình chất lượng cao")  #Nếu nhận thông báo "Vắng nhà" -> Bật chế độ ghi hình chất lượng cao.



# Chạy thử
hub = SmartHub()  # tạo trung tâm

light = Light()  # tạo đèn
ac = AirConditioner()  # tạo điều hòa
cam = SecurityCamera()  # tạo camera

hub.attach(light)  # thêm đèn
hub.attach(ac)  # thêm điều hòa
hub.attach(cam)  # thêm camera

hub.notify("Trời tối")  # chỉ đèn chạy
hub.notify("Nhiệt độ cao")  # chỉ điều hòa chạy
hub.notify("Vắng nhà")  # chỉ camera chạy