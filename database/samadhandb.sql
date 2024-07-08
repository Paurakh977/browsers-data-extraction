-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 08, 2024 at 09:38 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `samadhandb`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_usage_info`
--

CREATE TABLE `app_usage_info` (
  `tab_name` varchar(100) NOT NULL,
  `used_time` int(11) NOT NULL,
  `browser` varchar(100) DEFAULT NULL,
  `SN` int(11) NOT NULL,
  `used_day` varchar(10) DEFAULT NULL,
  `used_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `app_usage_info`
--

INSERT INTO `app_usage_info` (`tab_name`, `used_time`, `browser`, `SN`, `used_day`, `used_date`) VALUES
('localhost/phpmyadmin/index', 5, 'Google Chrome', 1, 'Tuesday', '2024-07-09'),
('youtube', 15, 'Firefox', 2, 'Wednesday', '2024-07-10'),
('instagram', 20, 'Safari', 3, 'Thursday', '2024-07-11'),
('facebook', 45, 'Opera', 4, 'Friday', '2024-07-12'),
('twitter', 30, 'Microsoft Edge', 5, 'Saturday', '2024-07-13'),
('reddit', 10, 'Google Chrome', 6, 'Sunday', '2024-07-14'),
('whatsapp', 35, 'Safari', 8, 'Tuesday', '2024-07-16'),
('snapchat', 40, 'Opera', 9, 'Wednesday', '2024-07-17'),
('tiktok', 50, 'Microsoft Edge', 10, 'Thursday', '2024-07-18'),
('discord', 7, 'Microsoft Edge', 32, 'Monday', '2024-07-08');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_usage_info`
--
ALTER TABLE `app_usage_info`
  ADD PRIMARY KEY (`SN`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_usage_info`
--
ALTER TABLE `app_usage_info`
  MODIFY `SN` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
