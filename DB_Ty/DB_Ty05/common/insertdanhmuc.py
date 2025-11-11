from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(tenDM, moTa=None, trangThai=1):
    """Thêm một danh mục mới vào bảng danhmuc"""
    conn = connect_mysql()
    if conn is None:
        print("❌ Không thể kết nối MySQL")
        return

    try:
        cursor = conn.cursor()
        sql = "INSERT INTO danhmuc (tenDM, moTa, trangThai) VALUES (%s, %s, %s)"
        val = (tenDM, moTa, trangThai)
        cursor.execute(sql, val)
        conn.commit()
        print(f"✅ Đã thêm danh mục: {tenDM}")
    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        cursor.close()
        conn.close()
