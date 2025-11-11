-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1:3307
-- Thời gian đã tạo: Th10 04, 2025 lúc 05:14 AM
-- Phiên bản máy phục vụ: 10.4.17-MariaDB
-- Phiên bản PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlthuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `maDM` int(11) NOT NULL,
  `tenDM` varchar(100) NOT NULL,
  `moTa` text DEFAULT NULL,
  `trangThai` tinyint(4) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`maDM`, `tenDM`, `moTa`, `trangThai`) VALUES
(1, 'Hot Sale', 'None', 1),
(2, 'Thuốc', NULL, 1),
(3, 'Thực phẩm chức năng', NULL, 1),
(4, 'Dược mỹ phẩm', NULL, 1),
(6, 'Do an', 'Do an CHAM', 1),
(8, 'nuoc uong', 'nuoc uong co ga', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `maSP` int(11) NOT NULL,
  `tenSP` varchar(150) NOT NULL,
  `giaGoc` decimal(10,0) NOT NULL,
  `giaKM` decimal(10,0) DEFAULT NULL,
  `giamGia` int(11) DEFAULT NULL,
  `hinhAnh` varchar(255) DEFAULT NULL,
  `moTa` text DEFAULT NULL,
  `soSuat` int(11) DEFAULT 0,
  `maDM` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`maSP`, `tenSP`, `giaGoc`, `giaKM`, `giamGia`, `hinhAnh`, `moTa`, `soSuat`, `maDM`) VALUES
(1, 'Nước tẩy trang Bioderma Sensibio', '535000', '398750', 25, 'bioderma.jpg', NULL, 20, 1),
(2, 'Tăm chỉ nha khoa Okamura 734503', '22000', '18000', 18, 'okamura.jpg', NULL, 20, 1),
(3, 'Nước súc miệng Listerine Cool Mint', '169000', '81000', 52, 'listerine.jpg', NULL, 20, 1),
(4, 'Nước Yến Collagen Green Bird Nutrienst', '30000', '22500', 25, 'greenbird.jpg', NULL, 60, 1);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`maDM`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`maSP`),
  ADD KEY `maDM` (`maDM`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `maDM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `maSP` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`maDM`) REFERENCES `danhmuc` (`maDM`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
