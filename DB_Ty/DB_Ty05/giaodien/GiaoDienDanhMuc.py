import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


# ===================== CÁC HÀM XỬ LÝ DỮ LIỆU =====================
def get_all_danhmuc(conn):
    data = []
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM danhmuc ORDER BY maDM ASC")
        data = cursor.fetchall()
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi lấy dữ liệu: {e}")
    finally:
        cursor.close()
    return data


def insert_danhmuc(conn, tenDM, moTa):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO danhmuc (tenDM, moTa) VALUES (%s, %s)"
        cursor.execute(sql, (tenDM, moTa))
        conn.commit()
        messagebox.showinfo("Thành công", "Đã thêm danh mục mới!")
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm danh mục: {e}")
    finally:
        cursor.close()


def update_danhmuc(conn, maDM, tenDM, moTa):
    try:
        cursor = conn.cursor()
        sql = "UPDATE danhmuc SET tenDM=%s, moTa=%s WHERE maDM=%s"
        cursor.execute(sql, (tenDM, moTa, maDM))
        conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Thành công", "Đã cập nhật danh mục!")
        else:
            messagebox.showwarning("Cảnh báo", "Không tìm thấy danh mục để cập nhật!")
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi cập nhật danh mục: {e}")
    finally:
        cursor.close()


def delete_danhmuc(conn, maDM):
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM danhmuc WHERE maDM=%s"
        cursor.execute(sql, (maDM,))
        conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Thành công", "Đã xóa danh mục!")
        else:
            messagebox.showwarning("Cảnh báo", "Không tìm thấy danh mục để xóa!")
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi xóa danh mục: {e}")
    finally:
        cursor.close()


# ===================== HÀM XỬ LÝ GIAO DIỆN =====================
def load_data():
    """Hiển thị dữ liệu danh mục lên Treeview"""
    for item in tree.get_children():
        tree.delete(item)

    conn = connect_mysql()
    if conn:
        data = get_all_danhmuc(conn)
        conn.close()
        for row in data:
            tree.insert("", "end", values=(row["maDM"], row["tenDM"], row["moTa"]))


def on_add():
    ten = entry_ten.get().strip()
    mota = entry_mota.get().strip()

    if ten == "":
        messagebox.showwarning("Cảnh báo", "Tên danh mục không được để trống!")
        return

    conn = connect_mysql()
    if conn:
        insert_danhmuc(conn, ten, mota)
        conn.close()
        refresh_form()


def on_update():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn danh mục cần sửa!")
        return

    values = tree.item(selected, "values")
    maDM = values[0]
    ten = entry_ten.get().strip()
    mota = entry_mota.get().strip()

    conn = connect_mysql()
    if conn:
        update_danhmuc(conn, maDM, ten, mota)
        conn.close()
        refresh_form()


def on_delete():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn danh mục cần xóa!")
        return

    values = tree.item(selected, "values")
    maDM, ten = values[0], values[1]

    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa '{ten}'?")
    if confirm:
        conn = connect_mysql()
        if conn:
            delete_danhmuc(conn, maDM)
            conn.close()
            refresh_form()


def on_select(event):
    """Khi chọn 1 dòng trong bảng"""
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")
        entry_ten.delete(0, tk.END)
        entry_ten.insert(0, values[1])
        entry_mota.delete(0, tk.END)
        entry_mota.insert(0, values[2])


def refresh_form():
    """Làm mới toàn bộ form"""
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)
    load_data()


# ===================== GIAO DIỆN CHÍNH =====================
root = tk.Tk()
root.title("Quản lý Danh mục Sản phẩm")
root.geometry("750x450")

# --- Frame nhập liệu ---
frame_input = tk.LabelFrame(root, text="Thông tin danh mục")
frame_input.pack(fill="x", padx=10, pady=10)

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_ten = tk.Entry(frame_input, width=40)
entry_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_mota = tk.Entry(frame_input, width=40)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

# --- Frame nút chức năng ---
frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)

tk.Button(frame_btn, text="➕ Thêm", width=10, bg="lightgreen", command=on_add).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="✏️ Sửa", width=10, bg="lightblue", command=on_update).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="🗑️ Xóa", width=10, bg="salmon", command=on_delete).grid(row=0, column=2, padx=5)
tk.Button(frame_btn, text="🔄 Làm mới", width=10, bg="khaki", command=refresh_form).grid(row=0, column=3, padx=5)

# --- Bảng Treeview ---
columns = ("maDM", "tenDM", "moTa")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.heading("maDM", text="Mã DM")
tree.heading("tenDM", text="Tên danh mục")
tree.heading("moTa", text="Mô tả")
tree.column("maDM", width=80, anchor="center")
tree.column("tenDM", width=200)
tree.column("moTa", width=400)
tree.pack(fill="both", expand=True, padx=10, pady=10)

tree.bind("<<TreeviewSelect>>", on_select)

# --- Load dữ liệu ban đầu ---
load_data()

root.mainloop()
