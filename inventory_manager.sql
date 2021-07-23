-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 21, 2021 at 03:58 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory_manager `
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `reference` varchar(255) NOT NULL,
  `partname` varchar(255) NOT NULL,
  `minarea` float(10,2) NOT NULL,
  `maxarea` float(10,2) NOT NULL,
  `number_of_holes` int(11) NOT NULL,
  `mindiameter` float(10,2) NOT NULL,
  `maxdiameter` float(10,2) NOT NULL,
  `count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `reference`, `partname`, `minarea`, `maxarea`, `number_of_holes`, `mindiameter`, `maxdiameter`, `count`) VALUES
(3, 'B785', 'Bolt', 3900.00, 4100.00, 1, 90.50, 92.00, 4),
(4, 'W8945', 'Washer', 35000.00, 35100.00, 1, 55.20, 61.50, 7),
(5, 'M184', 'Mount', 17800.00, 18000.00, 6, 127.00, 128.50, 5),
(6, 'B864', 'Bolt', 4150.00, 5210.00, 1, 177.50, 778.50, 3),
(7, 'W785', 'Washer', 28900.00, 29100.00, 1, 195.50, 196.00, 8),
(8, 'M785', 'Mount', 27210.00, 27310.00, 5, 210.00, 212.00, 15),
(9, 'B777', 'Bolt', 7750.00, 7822.00, 1, 95.50, 97.00, 11),
(10, 'W425', 'Washer', 34700.00, 35050.00, 1, 78.00, 78.80, 5),
(11, 'M864', 'Mount', 9800.00, 9900.00, 4, 110.00, 110.50, 8),
(12, 'B988', 'Bolt', 19500.00, 20200.00, 1, 69.70, 70.30, 20),
(14, 'SC382', 'Screw', 29.30, 32.42, 2, 23.40, 23.53, 2),
(15, 'SC382', 'Screw', 29.30, 32.42, 2, 23.40, 23.53, 2),
(16, 'Ut8232', 'utopsy', 600.00, 200.00, 3, 23.00, 22.00, 2),
(17, 'Robokill', 'Robot', 32.23, 230.42, 10, 90.50, 92.00, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
