-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 14, 2023 at 02:02 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ovs_student`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `student_id` int(11) NOT NULL,
  `department` enum('SCM','SBE','SCCD') DEFAULT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` char(60) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`student_id`, `department`, `first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES
(1, 'SCM', 'Paul', 'Thomas', 'carlos46@student.cuk.ac.ke', '$2b$12$TG..uoW5Xze1con/K7pnc.V2AwzuoSuUKPz.td35jYvLUnng2I7ne', '2023-10-14 11:09:09', '2023-10-14 11:09:09'),
(2, 'SCM', 'Steven', 'Harrison', 'jayalvarez@student.cuk.ac.ke', '$2b$12$74ikq8Z.Ya8wLoe9UAJfUebzGOSS5HdjUVGC6TkhJf4NBRHbu.pCC', '2023-10-14 11:09:10', '2023-10-14 11:09:10'),
(3, 'SBE', 'Cory', 'Mayo', 'anthonyweaver@student.cuk.ac.ke', '$2b$12$ibdLsKq8wJBEU8uA0bwkwuEPy/KpvhRzQNXAweXkobBGUz4M/Kl3G', '2023-10-14 11:09:11', '2023-10-14 11:09:11'),
(4, 'SCCD', 'Seth', 'Ruiz', 'vfinley@student.cuk.ac.ke', '$2b$12$RbmuLuOpGzzVCw7ccbzsDuo7YDy51kytO2FfLn0dRDDlfjE1FI85e', '2023-10-14 11:09:12', '2023-10-14 11:09:12'),
(5, 'SBE', 'Christopher', 'Lucas', 'sjohnson@student.cuk.ac.ke', '$2b$12$q2fU89chowXXj2jEbuNlmeyGvoHLeFYk8TRe47pmne1M6kX2h8ZJO', '2023-10-14 11:09:13', '2023-10-14 11:09:13'),
(6, 'SBE', 'Sarah', 'Mitchell', 'scottwalters@student.cuk.ac.ke', '$2b$12$j/xeiU4OOXKZqiPR5ZZHRe/18IQHdwdmDAWCwPoVj/MT.DSSPUkiK', '2023-10-14 11:09:14', '2023-10-14 11:09:14'),
(7, 'SCCD', 'Brett', 'Clay', 'kennethallen@student.cuk.ac.ke', '$2b$12$9GEd.MQZ3r9NaN9wq87UBudQSslCElxtlke6T91rs5OpdXmlGEM/u', '2023-10-14 11:09:14', '2023-10-14 11:09:14'),
(8, 'SCCD', 'Pamela', 'Howell', 'reyesdouglas@student.cuk.ac.ke', '$2b$12$8aqVkMM83zWAm/nXdqOCm.gVNN5aY2mkJPxTz9yeZeo.MrXqgPrk2', '2023-10-14 11:09:15', '2023-10-14 11:09:15'),
(9, 'SCCD', 'Amy', 'Murphy', 'debra58@student.cuk.ac.ke', '$2b$12$hCMGXDdIfWecrRaZv9n6w.XRwWfow7S7Y76kIs9KmI0/qb4WV54vK', '2023-10-14 11:09:16', '2023-10-14 11:09:16'),
(10, 'SCM', 'James', 'Sanders', 'cgoodman@student.cuk.ac.ke', '$2b$12$b2tHbJ.eR2j6DKNvDwVY1ul.y4wkrdNsCx3s4sSH0lIB5sBQDv2Za', '2023-10-14 11:09:17', '2023-10-14 11:09:17');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`student_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
