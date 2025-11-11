from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


def get_all_danhmuc():
    """Lấy toàn bộ danh sách danh mục"""
    conn = connect_mysql()
    if conn is None:
        print("❌ Không thể kết nối MySQL")
        return []

    danh_sach = []
    try:
        cursor = conn.cursor(dictionary=True)  # trả kết quả dạng dict
        cursor.execute("SELECT * FROM danhmuc ORDER BY maDM ASC")
        danh_sach = cursor.fetchall()

        print(f"✅ Đã lấy {len(danh_sach)} danh mục từ cơ sở dữ liệu.")
    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
    finally:
        cursor.close()
        conn.close()

    return danh_sach
