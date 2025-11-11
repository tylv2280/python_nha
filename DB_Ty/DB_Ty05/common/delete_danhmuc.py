from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def delete_danhmuc(maDM):
    """Xóa 1 danh mục theo mã (maDM)"""
    conn = connect_mysql()
    if conn is None:
        print("❌ Không thể kết nối MySQL")
        return

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM danhmuc WHERE maDM = %s"
        val = (maDM,)
        cursor.execute(sql, val)
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có mã {maDM}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có mã {maDM}")
    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)
    finally:
        cursor.close()
        conn.close()
