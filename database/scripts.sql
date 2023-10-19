-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 19, 2023 at 05:00 PM
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
-- Table structure for table `candidates`
--

CREATE TABLE `candidates` (
  `candidate_id` int(11) NOT NULL,
  `term_id` varchar(255) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `position_id` int(11) DEFAULT NULL,
  `no_of_votes` int(11) DEFAULT NULL,
  `deleted_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `positions`
--

CREATE TABLE `positions` (
  `position_id` int(11) NOT NULL,
  `name_of_position` varchar(255) NOT NULL,
  `rules` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
(10, 'SCM', 'James', 'Sanders', 'cgoodman@student.cuk.ac.ke', '$2b$12$b2tHbJ.eR2j6DKNvDwVY1ul.y4wkrdNsCx3s4sSH0lIB5sBQDv2Za', '2023-10-14 11:09:17', '2023-10-14 11:09:17'),
(11, 'SBE', 'Charles', 'James', 'aguirrejoshua@student.cuk.ac.ke', '$2b$12$cU7xnethJLIFctQrmFaPueNcujIXMu7VK/UqLT5GU2SO8.kb69U2K', '2023-10-17 19:11:41', '2023-10-17 19:11:41'),
(12, 'SCCD', 'Kevin', 'Collins', 'alisonhudson@student.cuk.ac.ke', '$2b$12$zFp.t7fIDKHvL8ctuwBXNeAFSodPE5kuRegiqHScQ0GLcM0qYapmm', '2023-10-17 19:11:42', '2023-10-17 19:11:42'),
(13, 'SCM', 'Michele', 'Allen', 'samantha59@student.cuk.ac.ke', '$2b$12$ETxK4/BChiOckC2wAek1U.JOFXpkuaEAsJwwOj63Wh6KpcbdzX4QK', '2023-10-17 19:11:42', '2023-10-17 19:11:42'),
(14, 'SCM', 'Christopher', 'Mcdonald', 'adamjohnson@student.cuk.ac.ke', '$2b$12$GFeVgPjJeNoNWTfeAriGJeIRpzaEnu6a5ANH.i5qa9FUDEk5sDmye', '2023-10-17 19:11:43', '2023-10-17 19:11:43'),
(15, 'SBE', 'Amanda', 'Ray', 'ryan66@student.cuk.ac.ke', '$2b$12$ZAPKHF1n2jRHdAbj8nQL7eVXu0m0U2g1qk47LeC.f6iikTZPpyINq', '2023-10-17 19:11:44', '2023-10-17 19:11:44'),
(16, 'SBE', 'Kelly', 'Davis', 'thomas14@student.cuk.ac.ke', '$2b$12$K2WwToWgaV6sbxTbfJRX8e0Z//tGLUkVjgt4TgShZlabK.gxwovsC', '2023-10-17 19:11:45', '2023-10-17 19:11:45'),
(17, 'SCCD', 'Kayla', 'Hamilton', 'jeffreyboone@student.cuk.ac.ke', '$2b$12$cbbTMstiJzQSbeT1m8mMROhH.bfq0dO/APKw7yrJt9V3cJ1avqa16', '2023-10-17 19:11:45', '2023-10-17 19:11:45'),
(18, 'SCM', 'Nicole', 'Johnson', 'justin10@student.cuk.ac.ke', '$2b$12$DZMN2gxjKEV/e/VtVm1ZSO.4ve3vIM1PQhN5x7.DpYHNs6xn8ZbEi', '2023-10-17 19:11:46', '2023-10-17 19:11:46'),
(19, 'SCM', 'Edward', 'Vincent', 'ivan00@student.cuk.ac.ke', '$2b$12$3LbNOZfJl4aH3dTVQ75oCOHMGfEcAV2NEQDyYWxUZWB7ZWA2ezD72', '2023-10-17 19:11:47', '2023-10-17 19:11:47'),
(20, 'SCM', 'Cynthia', 'Hill', 'xhess@student.cuk.ac.ke', '$2b$12$c6mm6CflMR1P5EjtnJKx2.Zey4TvexnkEA./bZoybvo/HKsyJNCoy', '2023-10-17 19:11:48', '2023-10-17 19:11:48'),
(21, 'SCCD', 'Michael', 'Hughes', 'greg18@student.cuk.ac.ke', '$2b$12$wDZotbEryOQTvdcYmRNdgO50cjVxM.UyfwpCOkTE.CjlYE36GCLrC', '2023-10-17 19:13:00', '2023-10-17 19:13:00'),
(22, 'SBE', 'Brandon', 'Walker', 'jackieclark@student.cuk.ac.ke', '$2b$12$PIjKhxVRlJUivoWxilSiUOryXmMw2qrroHiCc7EBqTqKKmEBP0grO', '2023-10-17 19:13:01', '2023-10-17 19:13:01'),
(23, 'SCM', 'Eric', 'Bryant', 'caldwelljohn@student.cuk.ac.ke', '$2b$12$xMxhQg.S7RHQLPuN7/al8Oi96HW6HsEwHKMYG.7NqG2YneJbAgvRa', '2023-10-17 19:13:02', '2023-10-17 19:13:02'),
(24, 'SCCD', 'Amber', 'Coleman', 'camachobrian@student.cuk.ac.ke', '$2b$12$eZgQkyoWNoAeuCzIW6DFw.tmx0SWA7ElbLy8HBCoNhM4ca9Zqjn2.', '2023-10-17 19:13:03', '2023-10-17 19:13:03'),
(25, 'SCCD', 'Michael', 'Davies', 'troy32@student.cuk.ac.ke', '$2b$12$0U/Yj9cWAXiHjiyT5idTnO96xEWfmIV7njoGbski4DXniJoyhHMO6', '2023-10-17 19:13:03', '2023-10-17 19:13:03'),
(26, 'SCM', 'Brandy', 'Miller', 'alvarezjeffrey@student.cuk.ac.ke', '$2b$12$y8OlwMFH2ALcKMeY/gcHyO1QsWjrGmseQHg/mqHOPtpKmVT721gvq', '2023-10-17 19:13:04', '2023-10-17 19:13:04'),
(27, 'SCCD', 'Jason', 'Vazquez', 'dperry@student.cuk.ac.ke', '$2b$12$PXJMkg92L/vm5jysOaBvOOSgWj1tnDLuJ3dN5J9h55e0L6jljEJ9K', '2023-10-17 19:13:05', '2023-10-17 19:13:05'),
(28, 'SBE', 'Benjamin', 'Gross', 'jeffreymiller@student.cuk.ac.ke', '$2b$12$gURQJAKoQUoBBMqTu3XkJeMrrs.4eh9JVs5HwyJKfmdwYp3/9qmeK', '2023-10-17 19:13:06', '2023-10-17 19:13:06'),
(29, 'SCM', 'Janet', 'Watson', 'laurie80@student.cuk.ac.ke', '$2b$12$Vd3jpL2K9SIjNioGgdXUQ.ogRIVeUGnUo1qhw3EoK1pq93GO0S8/C', '2023-10-17 19:13:07', '2023-10-17 19:13:07'),
(30, 'SBE', 'David', 'Frank', 'samuelsanders@student.cuk.ac.ke', '$2b$12$s/516nTAa./6TxSZP5WnGuKiZzN1GXpe2afd1B/rDzdcwwFrGD7ja', '2023-10-17 19:13:07', '2023-10-17 19:13:07'),
(31, 'SBE', 'Robert', 'Campbell', 'jermaineromero@student.cuk.ac.ke', '$2b$12$Joqe4jBZQFOcilWl1YIKju2stBDcFc3JXcJY7YpvFR0ihwkHvPMsK', '2023-10-18 02:56:19', '2023-10-18 02:56:19'),
(32, 'SCCD', 'Austin', 'Harmon', 'dianawells@student.cuk.ac.ke', '$2b$12$2Gs1uKpwDfxMrHC383iMH.ZP9Bw1G4QWuLMAfwk30MM9Hq7whH7CG', '2023-10-18 02:56:20', '2023-10-18 02:56:20'),
(33, 'SBE', 'Gina', 'Cochran', 'glen38@student.cuk.ac.ke', '$2b$12$SZXxTbold2jWFBAIXoV3nOoqOHFma1gfpsviUf4sTyQpIZyQdo2/i', '2023-10-18 02:56:21', '2023-10-18 02:56:21'),
(34, 'SBE', 'Jesse', 'Mckay', 'jeffreytate@student.cuk.ac.ke', '$2b$12$4W3ohU9c5VDYXc/S4vu4eerd7AIB1XYA6aedIHGeMVcnVg6cF5Fyq', '2023-10-18 02:56:22', '2023-10-18 02:56:22'),
(35, 'SCCD', 'Gloria', 'Rowland', 'ruthmoreno@student.cuk.ac.ke', '$2b$12$4gDC0PH2967mBBe8XqsWyedR.JAG2S162dHSsj4OwikXUkw9aeOnm', '2023-10-18 02:56:22', '2023-10-18 02:56:22'),
(36, 'SCCD', 'Jordan', 'Norton', 'hoganryan@student.cuk.ac.ke', '$2b$12$gRMeAMK/VLg.qN1Ew3GgXeJCVJsNGhhXORIJOhnv4jsbGgQJwIc3u', '2023-10-18 02:56:23', '2023-10-18 02:56:23'),
(37, 'SBE', 'Joshua', 'Noble', 'jacob89@student.cuk.ac.ke', '$2b$12$CPICsWJB0p1PJSsP7eYHdu0TltLUbTODQsApCbualI.vTgibGT6gy', '2023-10-18 02:56:24', '2023-10-18 02:56:24'),
(38, 'SCCD', 'Maria', 'Chambers', 'ohenderson@student.cuk.ac.ke', '$2b$12$LFdnd7sUqa0q6ax7nzgAO.nXhRjfoDcAiAjDo1eZWWN.kSdRvfTbi', '2023-10-18 02:56:25', '2023-10-18 02:56:25'),
(39, 'SCM', 'Courtney', 'Owens', 'tony94@student.cuk.ac.ke', '$2b$12$dk5KboovtMQFvYUJ0.oP.eRWJ2zVE4BeWAN/nMCWdnfG.yWU9YCiK', '2023-10-18 02:56:25', '2023-10-18 02:56:25'),
(40, 'SCCD', 'Thomas', 'Joseph', 'hgeorge@student.cuk.ac.ke', '$2b$12$dGznya/gEpebohpQcf/h/egc1XGO3GKdg.Dbloy40oysOBEeR9r5.', '2023-10-18 02:56:26', '2023-10-18 02:56:26'),
(41, 'SCM', 'sam', 'sam', 'sam%40student.ac.ke', '$2b$12$0f5d2xnTtfSOJio1jCs7metDlVrFtQdTBtOKml91SP4aikhq/Lsty', '2023-10-18 04:44:29', '2023-10-18 04:44:29'),
(42, 'SBE', 'Raven', 'Sullivan', 'thomasamanda@student.cuk.ac.ke', '$2b$12$4IDb51Q6N6ne.0E2.Ai.8u/6kRgDuaq2sBWvetARoHWNyBdfjZjHq', '2023-10-18 08:12:05', '2023-10-18 08:12:05'),
(43, 'SCCD', 'Seth', 'Meyer', 'kimberly52@student.cuk.ac.ke', '$2b$12$6QLLqz0CLFkYd0foBu2XUOLlY.mTPNrwNJXWOnhddGhecLqHr0oj6', '2023-10-18 08:12:06', '2023-10-18 08:12:06'),
(44, 'SCM', 'Jessica', 'Atkinson', 'boydrebecca@student.cuk.ac.ke', '$2b$12$YQjP4heKpoQHuU6c4ZKMae51KnHwWv9QKiICrflVcJDqmbccdWRK2', '2023-10-18 08:12:07', '2023-10-18 08:12:07'),
(45, 'SCM', 'Nicole', 'Barker', 'browntony@student.cuk.ac.ke', '$2b$12$zeITccp/KwScDWFtnIwM9eVE95QDvki8bHHaKeay60hrCaLgjpXEq', '2023-10-18 08:12:09', '2023-10-18 08:12:09'),
(46, 'SBE', 'Cesar', 'Decker', 'hintondawn@student.cuk.ac.ke', '$2b$12$01XjI6l/rFsxz9EZuTjmY.9/MlZgZl5Nz6vV1.N/JdWV.W0Wzrh/2', '2023-10-18 08:12:10', '2023-10-18 08:12:10'),
(47, 'SBE', 'Chris', 'Jordan', 'maria38@student.cuk.ac.ke', '$2b$12$ah3MCdMHyBYx9E0fDiTTW.XBF.EwjrNILlUq.H62wwjWemCIzCfr2', '2023-10-18 08:12:11', '2023-10-18 08:12:11'),
(48, 'SCM', 'Matthew', 'Horton', 'sotolindsay@student.cuk.ac.ke', '$2b$12$Wzg/3U6cCfSdkn8Tf95nWeSzRWzmhEZhMkDlJi8s.wzd0Z4Gh2kP6', '2023-10-18 08:12:12', '2023-10-18 08:12:12'),
(49, 'SCM', 'Marissa', 'Page', 'antonio59@student.cuk.ac.ke', '$2b$12$LVl5J/ZgE0y0QQIin/AKeuVB76xnZ9NeWaha4xxREXQ/lI1vpg0FW', '2023-10-18 08:12:14', '2023-10-18 08:12:14'),
(50, 'SCM', 'William', 'Summers', 'rodriguezbrandon@student.cuk.ac.ke', '$2b$12$cLYLxa0H1nN/bcHv17ieh.e0phGeKCnXgmFwY/YGOdz6jluXfcs/W', '2023-10-18 08:12:15', '2023-10-18 08:12:15'),
(51, 'SCM', 'Cynthia', 'Poole', 'ashleyharvey@student.cuk.ac.ke', '$2b$12$9O/UJuWFiYfXBOR.CGw6UOgmg1cKFil1xT3mTqMWhG9r9jHq.iAQi', '2023-10-18 08:12:16', '2023-10-18 08:12:16'),
(52, 'SCM', 'qwerty', 'qwerty', 'qwerty%40student.cuk.ac.ke', '$2b$12$mSQZtEq7HIQa7WtKwAVy/eEYCLrnVtF3g8tLz5U6mUTrhLqXq9DY2', '2023-10-18 08:14:44', '2023-10-18 08:14:44'),
(53, 'SCM', 'qqqq', 'qqqq', 'sad%40jiberuin.ac.ke', '$2b$12$xwuto6tljvnZcl8H7kPqx.KICtDfRxHjbqJQSvZ29PMfTyKI42jtq', '2023-10-18 08:47:54', '2023-10-18 08:47:54'),
(54, 'SBE', 'Jasmine', 'Gonzales', 'erichernandez@student.cuk.ac.ke', '$2b$12$o5nFvr9CbPiqsrV.pYhgTuzaQxPyttwPQhPhh5z7UTC38ZMG6UEcO', '2023-10-18 08:50:42', '2023-10-18 08:50:42'),
(55, 'SBE', 'Deanna', 'Berg', 'nicholasramirez@student.cuk.ac.ke', '$2b$12$jk.mLVsjz0k/3APL4yk3rOrxmq2O0E7OLsRuHRxgSZPGCJ0IjkzCO', '2023-10-18 08:50:43', '2023-10-18 08:50:43'),
(56, 'SBE', 'Julia', 'Castillo', 'dylanmiller@student.cuk.ac.ke', '$2b$12$1QVFeg.XfQm6y/aa8zto2uuapbj1.dyKm7ehwUxjdTKHQ1BCzqT3e', '2023-10-18 08:50:45', '2023-10-18 08:50:45'),
(57, 'SCM', 'Wendy', 'Collier', 'isaac53@student.cuk.ac.ke', '$2b$12$MLOnIf49NJLg25pBP51/yugQ6fCa1rzuzXNIiZxAfjYheE6bWl.q.', '2023-10-18 08:50:46', '2023-10-18 08:50:46'),
(58, 'SBE', 'Michele', 'Cox', 'dcarter@student.cuk.ac.ke', '$2b$12$.Zb4LmSTsCwT60ORB/9tCevkP4ptoaGSHhL67PLPmgOjj23MbucIS', '2023-10-18 08:50:47', '2023-10-18 08:50:47'),
(59, 'SBE', 'Ronald', 'Graham', 'rhodges@student.cuk.ac.ke', '$2b$12$puIgf1Yq6m9dLs8mJuJmxuZIwruld0vnaUY6wAeTnZOs.vXv5296W', '2023-10-18 08:50:49', '2023-10-18 08:50:49'),
(60, 'SCCD', 'Michael', 'Cantu', 'jonathan02@student.cuk.ac.ke', '$2b$12$kaqokkzaOyL6.8uFIICenOnbOkGx/0UfOUeoDESrKAvtWfG2F7Qra', '2023-10-18 08:50:50', '2023-10-18 08:50:50'),
(61, 'SCCD', 'Jessica', 'Baker', 'benjamin81@student.cuk.ac.ke', '$2b$12$R0lxmiRYHWyrIZX/vgZva.JjcmfTmBLZvnWonTgxPL2bVNyoRYhE2', '2023-10-18 08:50:51', '2023-10-18 08:50:51'),
(62, 'SBE', 'Emily', 'Davis', 'patrickfriedman@student.cuk.ac.ke', '$2b$12$d.3ebJujawIM5c232sHp9.6w544JrlACCYflW9S2zlPiKwLmREkdO', '2023-10-18 08:50:52', '2023-10-18 08:50:52'),
(63, 'SCM', 'Dawn', 'Grant', 'chadpennington@student.cuk.ac.ke', '$2b$12$/C4qM7hm/ESOidcwmNXR3eL5V3QkJR3AcZ5ZzAVUkWhQJurzIhNOO', '2023-10-18 08:50:53', '2023-10-18 08:50:53');

-- --------------------------------------------------------

--
-- Table structure for table `term`
--

CREATE TABLE `term` (
  `term_id` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `status` enum('ongoing','completed','pending','cancelled') DEFAULT NULL,
  `start_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `end_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `admin_id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `user_type` enum('delegate','admin','polling_officer') DEFAULT NULL,
  `password` char(60) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`admin_id`, `email`, `user_type`, `password`, `created_at`, `updated_at`) VALUES
(1, 'shawncabrera@student.cuk.ac.ke', 'admin', '$2b$12$raJbau9vFIlb2eDyUK3xSuvtkIVrhL7MqGdO2GlaxOEeWwddPwpuO', '2023-10-14 11:09:18', '2023-10-14 11:09:18'),
(2, 'xrodriguez@student.cuk.ac.ke', 'polling_officer', '$2b$12$WyGI8GgQ.hXaUYCc4lxKxeYt3exL/o2ksJKRwEPc/cpALboDxTtdG', '2023-10-14 11:09:19', '2023-10-14 11:09:19'),
(3, 'greenebrandon@student.cuk.ac.ke', 'polling_officer', '$2b$12$Q9anS7sp.Bd/eT4/h78GjuR.eq.MXqXYJpiONNYho9rs.1FJmOEaW', '2023-10-14 11:09:20', '2023-10-14 11:09:20'),
(4, 'cheyenneolsen@student.cuk.ac.ke', 'admin', '$2b$12$uwHrJm29pAxDH1TQBwF3leXmYr3paeHb8KR9IYJdjfa4KO5z5CbPy', '2023-10-14 11:09:21', '2023-10-14 11:09:21'),
(5, 'loricarpenter@student.cuk.ac.ke', 'delegate', '$2b$12$Pgy8G13t3jYm1fFPWN9TKOcFvm.DC.glUjBGCiPv2UxZoND/SZ61.', '2023-10-14 11:09:22', '2023-10-14 11:09:22'),
(6, 'slee@student.cuk.ac.ke', 'polling_officer', '$2b$12$Wnw5ELzOYcH8xqkeUz3X3OSzpWyy.2GvoKzJqN4pVNikqgfkyPS/y', '2023-10-14 11:09:23', '2023-10-14 11:09:23'),
(7, 'craig99@student.cuk.ac.ke', 'delegate', '$2b$12$zrs3MjikPcDBflg1u2mlpOp9wHci4ywKdwmpwdzV3u5TQL1rHLkM2', '2023-10-14 11:09:24', '2023-10-14 11:09:24'),
(8, 'tinafreeman@student.cuk.ac.ke', 'admin', '$2b$12$MYyxEL1wc3Snmdl8Qg2Sfehz90aI56aHkeA.NfCBJefhLWZhQ4LHy', '2023-10-14 11:09:25', '2023-10-14 11:09:25'),
(9, 'qferguson@student.cuk.ac.ke', 'polling_officer', '$2b$12$3cB8EVeogmN1KwOGhu7/y.uomjNW4S3Lq6jGkx7sRDO9BbEVWC.FC', '2023-10-14 11:09:25', '2023-10-14 11:09:25'),
(10, 'patelsarah@student.cuk.ac.ke', 'delegate', '$2b$12$20qvYmOLtuAJxfMBy2tomewUvxnOzzYsrjypYhGBDKTEGyoJrpnw2', '2023-10-14 11:09:26', '2023-10-14 11:09:26'),
(11, 'darin45@student.cuk.ac.ke', 'admin', '$2b$12$fpIsIdGezJdikLKSM2JL5eT2v0x6mgQGdbf9LNQ9qAku79V3rEfny', '2023-10-17 19:13:08', '2023-10-17 19:13:08'),
(12, 'ryanhicks@student.cuk.ac.ke', 'delegate', '$2b$12$GqSfdgiTtSQSiZbHkXYhd.GSlZjaz5fGId/ueLPXNLJ1bF6n7FuZ2', '2023-10-17 19:13:09', '2023-10-17 19:13:09'),
(13, 'richardchavez@student.cuk.ac.ke', 'polling_officer', '$2b$12$QWKnU3wW4PcE8ZWt7h3n2ehqTTQSui4dfOoCH3yy5gt7QJu3xZmUW', '2023-10-17 19:13:10', '2023-10-17 19:13:10'),
(14, 'wdavenport@student.cuk.ac.ke', 'polling_officer', '$2b$12$ixW7RuYXL/3DeQ0wZAFHUeStQVH4Qf0s1mZMKy46btnDLRfRm6wGe', '2023-10-17 19:13:11', '2023-10-17 19:13:11'),
(15, 'liuconnor@student.cuk.ac.ke', 'admin', '$2b$12$APhp6GtAeslKMN3TKB1leevWqDwhCEv1DEqtR8X2AA5pqJPINcGR6', '2023-10-17 19:13:11', '2023-10-17 19:13:11'),
(16, 'wadams@student.cuk.ac.ke', 'admin', '$2b$12$Um1wssO9AE/QL3cPquyaCOubUe7tKYC90X.2LiDgJIqcthRz4CkkG', '2023-10-17 19:13:12', '2023-10-17 19:13:12'),
(17, 'sandersalan@student.cuk.ac.ke', 'admin', '$2b$12$4WY2FL5RAWDfbeBAkavlEuaAfsmtuXgnaL8NG3bs1tx4vNWBfWAdS', '2023-10-17 19:13:13', '2023-10-17 19:13:13'),
(18, 'janeleblanc@student.cuk.ac.ke', 'admin', '$2b$12$yRGBBwsVIAs1/792L2FdfOXn/MfDU.t8.SGGqfzdfwqCtJJbELJS.', '2023-10-17 19:13:14', '2023-10-17 19:13:14'),
(19, 'qcarter@student.cuk.ac.ke', 'polling_officer', '$2b$12$dAFip0k6d0VNTkqjFZOuJu4dzn/QUwT0qoSXbhYSa4D.MWJAnwTJu', '2023-10-17 19:13:15', '2023-10-17 19:13:15'),
(20, 'dwebb@student.cuk.ac.ke', 'polling_officer', '$2b$12$xw5M.MWmnBIFbjG5bqF5quGYuRtjawTFNKSFbxgq6gXPwBkQbGzcu', '2023-10-17 19:13:15', '2023-10-17 19:13:15'),
(21, 'jessicabrock@student.cuk.ac.ke', 'polling_officer', '$2b$12$26ukqqZI89uTglf8PcYHRukcpP/xqEphYmLH98wiKM.TGkPDjjYoW', '2023-10-18 02:56:27', '2023-10-18 02:56:27'),
(22, 'cruzdominique@student.cuk.ac.ke', 'polling_officer', '$2b$12$QgnlyLsbduZbaVjNDGx2HukwfrFIX3YFiHzuPKyUx8D6dNYvH50ye', '2023-10-18 02:56:28', '2023-10-18 02:56:28'),
(23, 'michelle49@student.cuk.ac.ke', 'delegate', '$2b$12$Zwl72VVGc8ZiZc/fSsko/ubvlx.f6.IW5K8E4ha9fJ5MRWK8OfEBe', '2023-10-18 02:56:29', '2023-10-18 02:56:29'),
(24, 'jennifer95@student.cuk.ac.ke', 'admin', '$2b$12$mjrKZ5GeQCFmupM4SRrGHe6XOgRNxe9nOhVPnWa79p.Ia.ZTJCP1e', '2023-10-18 02:56:29', '2023-10-18 02:56:29'),
(25, 'thomasjonathan@student.cuk.ac.ke', 'delegate', '$2b$12$yIRnLjXZkUdSXIVW1b7LZONbQgDYpn9d.R6DeD.sHDZU7bMvr/qTi', '2023-10-18 02:56:30', '2023-10-18 02:56:30'),
(26, 'pfoster@student.cuk.ac.ke', 'delegate', '$2b$12$Ha32/jXQmdlTL.dH7A6hn.n6dFlfHR.2jL6.WYFEGsiov3pibRaSm', '2023-10-18 02:56:31', '2023-10-18 02:56:31'),
(27, 'kevin11@student.cuk.ac.ke', 'delegate', '$2b$12$A2clG4CBewPAoJj4TG5m9ucDwFRoU2OAERy94z43JMu0ZaqNSIwMy', '2023-10-18 02:56:31', '2023-10-18 02:56:31'),
(28, 'aconway@student.cuk.ac.ke', 'admin', '$2b$12$zDRRYYOKjGLgMVfCSXUWX.vzwp7kVwko/f0IYxgqkBv0lu6xVJHXO', '2023-10-18 02:56:32', '2023-10-18 02:56:32'),
(29, 'kellygray@student.cuk.ac.ke', 'polling_officer', '$2b$12$hfKWRSc006qPB0h18zF0/uh2Qm1wwXeu57F2TjJKSsBqBVjxUGUWu', '2023-10-18 02:56:33', '2023-10-18 02:56:33'),
(30, 'westdustin@student.cuk.ac.ke', 'polling_officer', '$2b$12$4O0/N1PlPLLP.JzbLm00eeG4P9WIxhpLqNMcHXcjIGih1Dh7q7t/q', '2023-10-18 02:56:34', '2023-10-18 02:56:34'),
(31, 'ugarcia@student.cuk.ac.ke', 'admin', '$2b$12$S1YgI2X.7uAEwPrJUQyOEeauk6wblcvbju0UM3ZhtB2Ix94810ORC', '2023-10-18 08:12:17', '2023-10-18 08:12:17'),
(32, 'vgarrett@student.cuk.ac.ke', 'delegate', '$2b$12$thkPI8Mc.N/m.4G4HgvhveyiT06Aj8U5PhwezlBaeDnoRV4qgHabm', '2023-10-18 08:12:19', '2023-10-18 08:12:19'),
(33, 'yhebert@student.cuk.ac.ke', 'polling_officer', '$2b$12$FYfM0gvwBvRit9w2woL4uegStmplMj1RWcGYzWjtgFUcYcIOokK3K', '2023-10-18 08:12:21', '2023-10-18 08:12:21'),
(34, 'kelseymorrison@student.cuk.ac.ke', 'polling_officer', '$2b$12$P21QLSxkl635ETKPRfusJOKXOF.WV0d5esPtDa/Mt5jMM3CJKVwz6', '2023-10-18 08:12:22', '2023-10-18 08:12:22'),
(35, 'zlopez@student.cuk.ac.ke', 'polling_officer', '$2b$12$fyy/Nj1FG1zlImIT8xxMp.3soeEQd.DjbO1LlfQQeUVUuLhArFEOO', '2023-10-18 08:12:23', '2023-10-18 08:12:23'),
(36, 'crystal15@student.cuk.ac.ke', 'polling_officer', '$2b$12$kZNyBGHLoL4V1M0Lmh5LmObdgSPKF8m/.9kFImvNO4agOW35FFXne', '2023-10-18 08:12:25', '2023-10-18 08:12:25'),
(37, 'angela11@student.cuk.ac.ke', 'admin', '$2b$12$sN7cVB54BBygYmENGodSUu4soFQF3IUE0Dh2XyUCnWg6tJ6vMbeBK', '2023-10-18 08:12:26', '2023-10-18 08:12:26'),
(38, 'austin12@student.cuk.ac.ke', 'delegate', '$2b$12$vrVGXa9QHRONKfV0YJXJZe4/IcKzjef75PNA5vWVKb2culA0c7Lte', '2023-10-18 08:12:27', '2023-10-18 08:12:27'),
(39, 'mcunningham@student.cuk.ac.ke', 'polling_officer', '$2b$12$n0eBvRNKkGQKKkS1y2YrFua/iDUdqhggl2ZRBJWb8464zdAqz/u7u', '2023-10-18 08:12:28', '2023-10-18 08:12:28'),
(40, 'mlopez@student.cuk.ac.ke', 'admin', '$2b$12$1xnsakl4mYVeMjCz8XylfO.CQt6E/gwxP8dKzE/gtCoda/bm0w1.C', '2023-10-18 08:12:29', '2023-10-18 08:12:29'),
(41, 'kurt36@student.cuk.ac.ke', 'delegate', '$2b$12$CB.Ao4/fV1y2FuQGAKs8jetCYhsuoP70ATBKlz5WhAgtcVjv/v1I6', '2023-10-18 08:50:54', '2023-10-18 08:50:54'),
(42, 'john64@student.cuk.ac.ke', 'polling_officer', '$2b$12$hcoTwq4Imkkvhn0LVGfoUefN4.5Lh6qzCIwRY26feonQ/nDJ/OCdq', '2023-10-18 08:50:56', '2023-10-18 08:50:56'),
(43, 'davisjames@student.cuk.ac.ke', 'delegate', '$2b$12$6UN9w3TOwG4XDTjMKJltO.iE0QOjrJksTHIjI7AKI8zqbvFPgv2lG', '2023-10-18 08:50:58', '2023-10-18 08:50:58'),
(44, 'marshallwilliam@student.cuk.ac.ke', 'polling_officer', '$2b$12$AiDj/98.rkmSNm8Ew4z1ZuE5QQ9JUY1hxVXk51VsE4E716GDBR5R6', '2023-10-18 08:50:59', '2023-10-18 08:50:59'),
(45, 'nicholsonandrew@student.cuk.ac.ke', 'delegate', '$2b$12$uyeLtokbyZVmS0Pd3Qoe4eVVOnIP2ywqAtcJJXAHbwpMzrWEJnpYy', '2023-10-18 08:51:00', '2023-10-18 08:51:00'),
(46, 'richardparks@student.cuk.ac.ke', 'admin', '$2b$12$AsVbf0WkmzuXznsEKzVl4eqHwzF6kygl5df9rqvQOKyLu.RelEDES', '2023-10-18 08:51:01', '2023-10-18 08:51:01'),
(47, 'ckelly@student.cuk.ac.ke', 'polling_officer', '$2b$12$eoZqc9b7szbVuwx8zVOOUujfxtp9WyYKWSX5IL689Vi0kU3rLU14y', '2023-10-18 08:51:03', '2023-10-18 08:51:03'),
(48, 'valdezcameron@student.cuk.ac.ke', 'delegate', '$2b$12$x7eUfFZ.H7s1R0a3GwhjHuXEwqG0UB8BJfs4FKriczT/7ZozylYY2', '2023-10-18 08:51:04', '2023-10-18 08:51:04'),
(49, 'phelpssara@student.cuk.ac.ke', 'delegate', '$2b$12$C2Ca.e.wOUPE9iDyOGdJRuKc2eqGuPZNeQ7x2VnXiNBTEQ1b8c64.', '2023-10-18 08:51:06', '2023-10-18 08:51:06'),
(50, 'michaelmcdonald@student.cuk.ac.ke', 'admin', '$2b$12$M30puO4JfITWp1C4mbWao.rLzqzsYl0sewbXWMZLrRBfEjr3i2w.m', '2023-10-18 08:51:08', '2023-10-18 08:51:08');

-- --------------------------------------------------------

--
-- Table structure for table `voting`
--

CREATE TABLE `voting` (
  `voting_id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `term_id` varchar(255) DEFAULT NULL,
  `candidate_id` int(11) DEFAULT NULL,
  `position_id` int(11) DEFAULT NULL,
  `hash` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `candidates`
--
ALTER TABLE `candidates`
  ADD PRIMARY KEY (`candidate_id`),
  ADD KEY `term_id` (`term_id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `position_id` (`position_id`);

--
-- Indexes for table `positions`
--
ALTER TABLE `positions`
  ADD PRIMARY KEY (`position_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`student_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `term`
--
ALTER TABLE `term`
  ADD UNIQUE KEY `term_id` (`term_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`admin_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `voting`
--
ALTER TABLE `voting`
  ADD PRIMARY KEY (`voting_id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `term_id` (`term_id`),
  ADD KEY `candidate_id` (`candidate_id`),
  ADD KEY `position_id` (`position_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `candidates`
--
ALTER TABLE `candidates`
  MODIFY `candidate_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `positions`
--
ALTER TABLE `positions`
  MODIFY `position_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `voting`
--
ALTER TABLE `voting`
  MODIFY `voting_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `candidates`
--
ALTER TABLE `candidates`
  ADD CONSTRAINT `candidates_ibfk_1` FOREIGN KEY (`term_id`) REFERENCES `term` (`term_id`),
  ADD CONSTRAINT `candidates_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`),
  ADD CONSTRAINT `candidates_ibfk_3` FOREIGN KEY (`position_id`) REFERENCES `positions` (`position_id`);

--
-- Constraints for table `voting`
--
ALTER TABLE `voting`
  ADD CONSTRAINT `voting_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`),
  ADD CONSTRAINT `voting_ibfk_2` FOREIGN KEY (`term_id`) REFERENCES `term` (`term_id`),
  ADD CONSTRAINT `voting_ibfk_3` FOREIGN KEY (`candidate_id`) REFERENCES `candidates` (`candidate_id`),
  ADD CONSTRAINT `voting_ibfk_4` FOREIGN KEY (`position_id`) REFERENCES `positions` (`position_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
