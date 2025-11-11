from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def update_danhmuc(maDM, tenDM=None, moTa=None, trangThai=None):
    """Cập nhật thông tin danh mục theo mã maDM"""
    conn = connect_mysql()
    if conn is None:
        print("❌ Không thể kết nối MySQL")
        return

    try:
        cursor = conn.cursor()

        # Xây dựng câu SQL linh hoạt tùy dữ liệu truyền vào
        fields = []
        values = []

        if tenDM is not None:
            fields.append("tenDM = %s")
            values.append(tenDM)
        if moTa is not None:
            fields.append("moTa = %s")
            values.append(moTa)
        if trangThai is not None:
            fields.append("trangThai = %s")
            values.append(trangThai)

        if not fields:
            print("⚠️ Không có dữ liệu nào để cập nhật!")
            return

        sql = f"UPDATE danhmuc SET {', '.join(fields)} WHERE maDM = %s"
        values.append(maDM)

        cursor.execute(sql, tuple(values))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục có mã {maDM}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có mã {maDM}")
    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
    finally:
        cursor.close()
        conn.close()
