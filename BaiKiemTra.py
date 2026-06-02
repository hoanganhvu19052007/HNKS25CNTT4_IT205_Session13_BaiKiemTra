parking_lot = []

while True:
    choice = input("""
=============================================
        QUẢN LÝ BÃI XE - SMART PANKING
=============================================
    1. Thêm xe mới vào bãi
    2. Hiển thị danh sách xe trong bãi
    3. Tìm kiếm xe theo mã (id)
    4. Xóa xe khỏi bãi (khi xe ra)
    5. Thoát chương trình
=============================================
Mời bạn nhập lựa chọn từ (1-5): """)

    match choice:
        case "1":
            found = False
            car_id = 1
            type = input("Nhập vào loại xe: ").strip()
            if type.isspace() or type == "":
                print("Loại xe không được để trống").strip()
            owner = input("Nhập vào chủ xe: ")
            if owner.isspace() or owner == "":
                print("Chủ xe không được để trống")
            parking_lot.append({
                        "id": car_id,
                        "type": type,
                        "owner": owner
            })            
            car_id = car_id + 1
        case "2":
            if len(parking_lot) == 0:
                print("Bãi xe hiện đang rỗng")
            else: 
                print(f"{'ID': <5} | {'Loại xe': <10} | {'Chủ xe'}" )
                for index, car in enumerate(parking_lot, start= 1):
                    print(f"{index: <5} | {car['type']: <10} | {car['owner']}")
        case "3":
            sreach_id = int(input("Nhập vào id cần tìm kiếm: "))
            found = False
            for car in parking_lot:
                if car['id'] == sreach_id:
                    print(f"id: {car['id']}, type: {car['type']}, owner:{car['owner']} ")
                    found = True
            if not found:
                print(f"Không tìm thấy xe có id: {sreach_id}")
        case "4":
            delete_id = int(input("Nhập id xe cần xóa: "))
            found = False
            for car in parking_lot:
                if car['id'] == delete_id :
                    parking_lot.remove(car)
                    print(f"Đã xóa xe ID {car['id']} thành công!")
                    found = True
            if not found:
                print("Không tìm thấy xe để xóa")
        case "5":
            break


