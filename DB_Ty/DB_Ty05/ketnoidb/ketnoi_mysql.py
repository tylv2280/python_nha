import mysql.connector
from mysql.connector import Error

def connect_mysql():
    """Hàm tạo kết nối đến MySQL"""
    try:
        connection = mysql.connector.connect(
            host='websitebanraucu.abc',        # hoặc 127.0.0.1
            port=3307,               # cổng mặc định của MySQL
            user='root',             # tên đăng nhập MySQL
            password='',             # mật khẩu (nếu có thì điền vào)
            database='qlthuocankhang'      # tên database bạn muốn kết nối
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
