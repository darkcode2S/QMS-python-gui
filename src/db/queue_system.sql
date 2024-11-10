-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 15, 2024 at 04:48 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `queue_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(250) NOT NULL,
  `username` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `role` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`, `role`) VALUES
(1, 'admin', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `id` int(250) NOT NULL,
  `school_id` varchar(250) NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `affiliation` varchar(250) NOT NULL,
  `role` varchar(250) NOT NULL,
  `office` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`id`, `school_id`, `full_name`, `affiliation`, `role`, `office`) VALUES
(1, '43-6787', 'ssssssssssssssssssss', 'dasdsadasd', 'asdasdasd', 'School staff'),
(2, '35-5555', 'sadasd', 'asdasd', 'asdadsasd', 'School faculty');

-- --------------------------------------------------------

--
-- Table structure for table `operator`
--

CREATE TABLE `operator` (
  `id` int(250) NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `operate_area` varchar(250) NOT NULL,
  `phone_number` varchar(250) NOT NULL,
  `username` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `role` varchar(250) NOT NULL,
  `school_id` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `operator`
--

INSERT INTO `operator` (`id`, `full_name`, `operate_area`, `phone_number`, `username`, `password`, `role`, `school_id`) VALUES
(9, 'Roselyn basan', 'Scholarship coordinator', '0954353454353', 'rose', '$2b$12$/Ey35pSo9j31PUK6vxrYyusNyQ9NCZ3/ChyldbG6Cmu.yIEQc2C6W', 'operator', '11-1111'),
(10, 'Nina cabahug', 'Cashier service', '090675565766', 'nina', '$2b$12$plqMqzH9n1gZYm9za4i9MuJPn2ntVG8ZL8flk9FsD1gH8tY4kAKsi', 'operator', '22-2222'),
(11, 'Charlo aguillon', 'Promisorry note coordinator', '0989798787988', 'char', '$2b$12$fKNl9mrbxfLADzli3vdFbOzuozp45S7fWrkt2u7xZ.OWBikxsqyC2', 'operator', '33-3333'),
(12, 'Anthony crausus', 'Promisorry note coordinator', '099879879789', 'anton', '$2b$12$AEBMOxugXWimsY3DYvS/9.9GeyqYRRjOZVTxhkmoE8OEI.dJNjRz6', 'operator', '44-4444');

-- --------------------------------------------------------

--
-- Table structure for table `queue`
--

CREATE TABLE `queue` (
  `id` int(250) NOT NULL,
  `queue_number` varchar(250) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `school_id` varchar(250) NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `transaction` varchar(250) NOT NULL,
  `affiliation` varchar(250) NOT NULL,
  `phone` varchar(250) NOT NULL,
  `purpose_of_visit` varchar(250) NOT NULL,
  `compilition_time` varchar(250) NOT NULL,
  `voided` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `queue`
--

INSERT INTO `queue` (`id`, `queue_number`, `created_at`, `school_id`, `full_name`, `transaction`, `affiliation`, `phone`, `purpose_of_visit`, `compilition_time`, `voided`) VALUES
(3, '144', '2024-10-15 14:39:05', '35-5555', 'sadasd', 'Promisorry note coordinator', 'Staff/Faculty', '', 'Promisorry note', '', ''),
(5, '82', '2024-10-15 14:40:31', '35-5555', 'sadasd', 'Promisorry note coordinator', 'Staff/Faculty', '', 'Promisorry note', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `queue_admin`
--

CREATE TABLE `queue_admin` (
  `id` int(250) NOT NULL,
  `queue_number` varchar(250) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `school_id` varchar(250) NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `transaction` varchar(250) NOT NULL,
  `affiliation` varchar(250) NOT NULL,
  `phone` varchar(250) NOT NULL,
  `purpose_of_visit` varchar(250) NOT NULL,
  `compilation_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `voided` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `queue_admin`
--

INSERT INTO `queue_admin` (`id`, `queue_number`, `created_at`, `school_id`, `full_name`, `transaction`, `affiliation`, `phone`, `purpose_of_visit`, `compilation_time`, `voided`) VALUES
(1, '91', '2024-10-15 12:05:06', '21-0882', 'Anthony crausus', 'Cashier Service', 'Student', '', 'Tuition fee', '0000-00-00 00:00:00', 'Yes'),
(2, '4', '2024-10-15 14:31:08', '', 'dddddddddddddd', 'Scholarship coordinator', 'Visitor', '098967876575', 'Scholarship application', '2024-10-15 14:39:44', 'Yes'),
(3, '158', '2024-10-15 14:40:19', '21-0882', 'Anthony crausus', 'Cashier Service', 'Student', '', 'Tuition fee', '2024-10-15 14:40:58', ''),
(4, '5', '2024-10-15 14:44:29', '', 'ssssssssss', 'Scholarship coordinator', 'Visitor', '0978977686', 'Scholarship application', '2024-10-15 14:45:00', 'Yes');

-- --------------------------------------------------------

--
-- Table structure for table `queue_display`
--

CREATE TABLE `queue_display` (
  `id` int(250) NOT NULL,
  `queue_num` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `queue_display_promisorry`
--

CREATE TABLE `queue_display_promisorry` (
  `id` int(250) NOT NULL,
  `promisorry_number` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `queue_display_promisorry`
--

INSERT INTO `queue_display_promisorry` (`id`, `promisorry_number`) VALUES
(1, '144'),
(2, '82');

-- --------------------------------------------------------

--
-- Table structure for table `queue_display_sc`
--

CREATE TABLE `queue_display_sc` (
  `id` int(250) NOT NULL,
  `queue_sc` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(250) NOT NULL,
  `school_id` varchar(250) NOT NULL,
  `full_name` varchar(250) NOT NULL,
  `course` varchar(250) NOT NULL,
  `year_level` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `school_id`, `full_name`, `course`, `year_level`) VALUES
(1, '21-0882', 'Anthony crausus', 'BSCS', '3rd Year'),
(3, '67-7878', 'asddsasad', 'BSSW', '2nd Year'),
(4, '56-7867', 'asdasdasd', 'BSEE', '3rd Year'),
(5, '45-9089', 'asdasdasd', 'BSMT', '4rth Year'),
(6, '12-9798', 'asdasdasd', 'BSM', '5th Year'),
(7, '67-9099', 'asdasdads', 'BEED', '6th Year'),
(8, '77-0677', 'dfdsfsdfsdf', 'BSED', '7th Year'),
(9, '67-8777', 'asdasdasd', 'BSBA', '8th Year'),
(10, '77-9090', 'sdadasdads', 'BSHM', '9th Year'),
(11, '66-9879', 'sdfdsfsdfs', 'BSA', '10th Year'),
(12, '23-7878', 'dgdgfdg', 'BAPS', '10th Year'),
(13, '45-6765', 'gdsgdfgfd', 'BS-CRIM', '10th Year');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `operator`
--
ALTER TABLE `operator`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `queue`
--
ALTER TABLE `queue`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `queue_admin`
--
ALTER TABLE `queue_admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `queue_display`
--
ALTER TABLE `queue_display`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `queue_display_promisorry`
--
ALTER TABLE `queue_display_promisorry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `queue_display_sc`
--
ALTER TABLE `queue_display_sc`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `operator`
--
ALTER TABLE `operator`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `queue`
--
ALTER TABLE `queue`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `queue_admin`
--
ALTER TABLE `queue_admin`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `queue_display`
--
ALTER TABLE `queue_display`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `queue_display_promisorry`
--
ALTER TABLE `queue_display_promisorry`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `queue_display_sc`
--
ALTER TABLE `queue_display_sc`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
