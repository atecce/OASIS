-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2+deb7u1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 16, 2016 at 10:06 PM
-- Server version: 5.5.44
-- PHP Version: 5.4.45-0+deb7u1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `marsoasis`
--

-- --------------------------------------------------------

--
-- Table structure for table `atmospheric_management`
--

CREATE TABLE IF NOT EXISTS `atmospheric_management` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actuator` varchar(128) NOT NULL,
  `current_value` varchar(128) NOT NULL,
  `previous_value` varchar(128) NOT NULL,
  `current_time_stamp` datetime NOT NULL,
  `previous_time_stamp` datetime NOT NULL,
  `current_user_id` varchar(160) NOT NULL,
  `previous_user_id` varchar(160) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sensor` (`actuator`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `atmospheric_management`
--

INSERT INTO `atmospheric_management` (`id`, `actuator`, `current_value`, `previous_value`, `current_time_stamp`, `previous_time_stamp`, `current_user_id`, `previous_user_id`) VALUES
(1, 'm8', '0', '1', '2016-01-16 21:19:18', '2016-01-18 01:03:09', 'samu9197@colorado.edu', 'example.2119@gmail.com'),
(2, 'p10', '0', '1', '2016-01-10 13:26:55', '2016-01-10 13:26:52', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(3, 'p12', '0', '1', '2016-01-10 13:27:01', '2016-01-10 13:26:58', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(4, 'v3', '0', '1', '2016-01-10 13:27:12', '2016-01-10 13:27:09', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(5, 'v4', '0', '1', '2016-01-16 21:19:22', '2016-01-18 01:03:14', 'samu9197@colorado.edu', 'example.2119@gmail.com'),
(6, 'm6', '100', '1', '2016-01-18 01:03:18', '2016-01-10 13:56:47', 'example.2119@gmail.com', 'samu9197@colorado.edu'),
(7, 'm7', '100', '62', '2016-01-10 13:56:51', '2016-01-10 13:56:23', 'samu9197@colorado.edu', 'samu9197@colorado.edu');

-- --------------------------------------------------------

--
-- Table structure for table `image_cache`
--

CREATE TABLE IF NOT EXISTS `image_cache` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `timestamp` varchar(220) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`timestamp`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `image_cache`
--

INSERT INTO `image_cache` (`id`, `name`, `timestamp`) VALUES
(8, 'IMG_Saturday_Jan16_2016_21_16_48.jpg', 'Saturday, Jan 16, 2016, 21:16:48'),
(9, 'IMG_Saturday_Jan16_2016_21_17_24.jpg', 'Saturday, Jan 16, 2016, 21:17:24'),
(10, 'IMG_Saturday_Jan16_2016_21_17_47.jpg', 'Saturday, Jan 16, 2016, 21:17:47'),
(11, 'IMG_Saturday_Jan16_2016_21_32_01.jpg', 'Saturday, Jan 16, 2016, 21:32:01'),
(1, 'IMG_Sunday_Jan10_2016_11_07_47.jpg', 'Sunday, Jan 10, 2016, 11:07:47'),
(2, 'IMG_Sunday_Jan10_2016_13_16_06.jpg', 'Sunday, Jan 10, 2016, 13:16:06'),
(3, 'IMG_Sunday_Jan10_2016_13_34_06.jpg', 'Sunday, Jan 10, 2016, 13:34:06'),
(4, 'IMG_Thursday_Jan14_2016_08_39_44.jpg', 'Thursday, Jan 14, 2016, 08:39:44'),
(5, 'IMG_Thursday_Jan14_2016_08_43_19.jpg', 'Thursday, Jan 14, 2016, 08:43:19'),
(6, 'IMG_Thursday_Jan14_2016_09_57_16.jpg', 'Thursday, Jan 14, 2016, 09:57:16'),
(7, 'IMG_Thursday_Jan14_2016_09_57_41.jpg', 'Thursday, Jan 14, 2016, 09:57:41');

-- --------------------------------------------------------

--
-- Table structure for table `lighting_and_imagery`
--

CREATE TABLE IF NOT EXISTS `lighting_and_imagery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actuator` varchar(128) NOT NULL,
  `current_value` varchar(128) NOT NULL,
  `previous_value` varchar(128) NOT NULL,
  `current_time_stamp` datetime NOT NULL,
  `previous_time_stamp` datetime NOT NULL,
  `current_user_id` varchar(160) NOT NULL,
  `previous_user_id` varchar(160) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sensor` (`actuator`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `lighting_and_imagery`
--

INSERT INTO `lighting_and_imagery` (`id`, `actuator`, `current_value`, `previous_value`, `current_time_stamp`, `previous_time_stamp`, `current_user_id`, `previous_user_id`) VALUES
(1, 'la', '100', '0', '2016-01-16 21:34:14', '2016-01-18 01:02:41', 'samu9197@colorado.edu', 'example.2119@gmail.com'),
(2, 'st', '0', '100', '2016-01-15 11:12:47', '2016-01-15 11:12:44', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(3, 'm18', '100', '0', '2016-01-16 21:17:42', '2016-01-16 21:17:18', 'samu9197@colorado.edu', 'samu9197@colorado.edu');

-- --------------------------------------------------------

--
-- Table structure for table `mars`
--

CREATE TABLE IF NOT EXISTS `mars` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start` tinyint(1) NOT NULL,
  `stop` tinyint(1) NOT NULL,
  `time_stamp` datetime NOT NULL,
  `user_id` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `timestamp` (`time_stamp`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `sensors`
--

CREATE TABLE IF NOT EXISTS `sensors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `value` varchar(80) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=94 ;

--
-- Dumping data for table `sensors`
--

INSERT INTO `sensors` (`id`, `name`, `value`, `timestamp`) VALUES
(1, 'gm_mo1', '1.393%', '2016-01-02 09:28:19'),
(2, 'ie_co', '0.041%', '2016-01-02 09:28:35'),
(3, 'gm_mo2', '26.001%', '2016-01-02 09:29:46'),
(4, 'gm_mo3', '25.613%', '2016-01-02 09:29:52'),
(5, 'gm_mo4', '26.233%', '2016-01-02 09:29:57'),
(6, 'gm_pH', '8.082', '2016-01-02 09:30:12'),
(7, 'gm_temp2', '18.437*C', '2016-01-02 09:30:18'),
(8, 'gm_temp3', '18.25*C', '2016-01-02 09:30:24'),
(9, 'gm_temp4', '19.312*C', '2016-01-02 09:30:29'),
(10, 'ie_light', '448.864 micro-mol m^-2 s^-1', '2016-01-02 09:30:38'),
(11, 'ie_oxy', '20.674%', '2016-01-02 09:31:17'),
(12, 'ie_rh_t2', 'Temp = 21.0*C, Humidity = 12.1%', '2016-01-02 09:31:25'),
(13, 'ie_rh_t3', 'Temp = 20.0*C, Humidity = 8.3%', '2016-01-02 09:31:32'),
(14, 'ie_tp', 'Temp = 22.2*C, Pressure = 84223.0Pa', '2016-01-02 09:31:37'),
(15, 'ltp_temp', '19.25 *C', '2016-01-02 09:31:47'),
(16, 'ltp_dop', '0.00', '2016-01-02 09:32:18'),
(17, 'ltp_ec', '0.00', '2016-01-02 09:32:27'),
(18, 'ltp_fm1', 'Flow rate [total vol] [LPM] [LPH]:0.000,0.000,0.000\r', '2016-01-02 09:32:35'),
(19, 'ltp_fm2', 'Flow rate [total vol] [LPM] [LPH]:0.000,0.000,0.000\r', '2016-01-02 09:32:59'),
(20, 'ltp_ll1', '9.994 inches', '2016-01-02 09:33:06'),
(21, 'ltp_ll2', '9.629 inches', '2016-01-02 09:33:12'),
(22, 'ltp_ll3', '9.654 inches', '2016-01-02 09:33:19'),
(23, 'ltp_ll4', '9.994 inches', '2016-01-02 09:33:23'),
(24, 'ltp_ll5', '9.994 inches', '2016-01-02 09:33:27'),
(25, 'ltp_ll6', '9.994 inches', '2016-01-02 09:33:34'),
(26, 'ltp_pH', '14.000', '2016-01-02 09:33:47'),
(31, 'ee_light', '120.879 micro-mol m^-2 s^-1', '2016-01-10 10:13:36'),
(32, 'ie_tp', 'Temp = 22.5 *C, Pressure = 83534.0 Pa', '2016-01-10 10:13:56'),
(33, 'ee_light', '125.714 micro-mol m^-2 s^-1', '2016-01-10 13:15:55'),
(34, 'ee_light', '125.311 micro-mol m^-2 s^-1', '2016-01-10 13:29:36'),
(35, 'gm_ec', '0.00', '2016-01-10 13:29:59'),
(36, 'gm_mo1', '1.53%', '2016-01-10 13:30:05'),
(37, 'gm_mo2', '15.036%', '2016-01-10 13:30:12'),
(38, 'gm_mo3', '14.896%', '2016-01-10 13:30:17'),
(39, 'gm_mo4', '15.036%', '2016-01-10 13:30:24'),
(40, 'gm_pH', '8.109', '2016-01-10 13:30:39'),
(41, 'gm_temp2', '18.562 *C', '2016-01-10 13:30:48'),
(42, 'gm_temp3', '19.0 *C', '2016-01-10 13:30:54'),
(43, 'gm_temp4', '19.625 *C', '2016-01-10 13:31:08'),
(44, 'ie_co', '0.046%', '2016-01-10 13:31:22'),
(45, 'ie_light', '391.245 micro-mol m^-2 s^-1', '2016-01-10 13:31:27'),
(46, 'ie_oxy', '7.304%', '2016-01-10 13:31:34'),
(47, 'ie_rh_t2', 'Temp = 20.4 *C, Humidity = 21.3%', '2016-01-10 13:31:40'),
(48, 'ie_rh_t3', 'Temp = 20.0 *C, Humidity = 11.7%', '2016-01-10 13:31:49'),
(49, 'ie_tp', 'Temp = 22.4 *C, Pressure = 83583.0 Pa', '2016-01-10 13:31:55'),
(50, 'ltp_ec', '0.00', '2016-01-10 13:32:06'),
(51, 'ltp_dop', '0.00', '2016-01-10 13:32:20'),
(52, 'ltp_fm1', 'Flow rate [total vol] [LPM] [LPH]:0.000,0.000,0.000\r0.000,0.000,0.000\r', '2016-01-10 13:32:30'),
(53, 'ltp_fm2', 'Flow rate [total vol] [LPM] [LPH]:0.000,0.000,0.000\r0.000,0.000,0.000\r', '2016-01-10 13:32:39'),
(54, 'ltp_ll1', '9.994 inches', '2016-01-10 13:32:52'),
(55, 'ltp_ll2', '9.629 inches', '2016-01-10 13:32:58'),
(56, 'ltp_ll3', '9.629 inches', '2016-01-10 13:33:04'),
(57, 'ltp_ll4', '9.994 inches', '2016-01-10 13:33:10'),
(58, 'ltp_ll5', '9.994 inches', '2016-01-10 13:33:22'),
(59, 'ltp_ll6', '9.994 inches', '2016-01-10 13:33:27'),
(60, 'ltp_pH', '14.000', '2016-01-10 13:33:42'),
(61, 'ltp_temp', '18.625 *C', '2016-01-10 13:33:48'),
(62, 'ie_co', '0.043%', '2016-01-14 08:41:40'),
(63, 'ie_oxy', '27.489%', '2016-01-14 08:41:47'),
(64, 'ie_tp', 'Temp = 23.8 *C, Pressure = 82755.0 Pa', '2016-01-14 08:41:56'),
(65, 'ltp_temp', '19.875 *C', '2016-01-14 08:42:05'),
(66, 'ee_light', '403.132 micro-mol m^-2 s^-1', '2016-01-16 21:20:03'),
(67, 'gm_ec', '0.00', '2016-01-16 21:27:59'),
(68, 'gm_mo1', '6.97%', '2016-01-16 21:28:07'),
(69, 'gm_mo2', '9.363%', '2016-01-16 21:28:11'),
(70, 'gm_mo3', '9.404%', '2016-01-16 21:28:17'),
(71, 'gm_mo4', '9.367%', '2016-01-16 21:28:23'),
(72, 'gm_pH', '8.248', '2016-01-16 21:28:37'),
(73, 'gm_temp2', '20.625 *C', '2016-01-16 21:28:37'),
(74, 'gm_temp3', '20.687 *C', '2016-01-16 21:28:49'),
(75, 'gm_temp4', '21.375 *C', '2016-01-16 21:28:51'),
(76, 'ie_co', '0.043%', '2016-01-16 21:29:10'),
(77, 'ie_light', '460.952 micro-mol m^-2 s^-1', '2016-01-16 21:29:16'),
(78, 'ie_oxy', '27.519%', '2016-01-16 21:29:21'),
(79, 'ie_tp', 'Temp = 24.2 *C, Pressure = 83416.0 Pa', '2016-01-16 21:29:31'),
(80, 'ie_rh_t3', 'Temp = 20.5 *C, Humidity = 14.0%', '2016-01-16 21:29:37'),
(81, 'ie_rh_t2', 'Temp = 22.1 *C, Humidity = 16.0%', '2016-01-16 21:29:38'),
(82, 'ltp_dop', '0.00', '2016-01-16 21:29:57'),
(83, 'ltp_ec', '0.00', '2016-01-16 21:30:08'),
(84, 'ltp_fm1', 'Flow rate [total vol] [LPM] [LPH]:0.000,0.000,0.000\r', '2016-01-16 21:30:18'),
(85, 'ltp_fm2', 'Flow rate [total vol] [LPM] [LPH]:0.000,0.000,0.000\r', '2016-01-16 21:30:22'),
(86, 'ltp_ll1', '9.994 inches', '2016-01-16 21:30:28'),
(87, 'ltp_ll2', '9.612 inches', '2016-01-16 21:30:30'),
(88, 'ltp_ll3', '9.654 inches', '2016-01-16 21:30:36'),
(89, 'ltp_ll4', '9.994 inches', '2016-01-16 21:30:41'),
(90, 'ltp_ll5', '9.994 inches', '2016-01-16 21:30:48'),
(91, 'ltp_ll6', '9.994 inches', '2016-01-16 21:30:53'),
(92, 'ltp_pH', '14.000', '2016-01-16 21:31:07'),
(93, 'ltp_temp', '19.687 *C', '2016-01-16 21:31:10');

-- --------------------------------------------------------

--
-- Table structure for table `system_maintenance`
--

CREATE TABLE IF NOT EXISTS `system_maintenance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actuator` varchar(128) NOT NULL,
  `current_value` varchar(128) NOT NULL,
  `previous_value` varchar(128) NOT NULL,
  `current_time_stamp` datetime NOT NULL,
  `previous_time_stamp` datetime NOT NULL,
  `current_user_id` varchar(160) NOT NULL,
  `previous_user_id` varchar(160) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sensor` (`actuator`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `system_maintenance`
--

INSERT INTO `system_maintenance` (`id`, `actuator`, `current_value`, `previous_value`, `current_time_stamp`, `previous_time_stamp`, `current_user_id`, `previous_user_id`) VALUES
(1, 'p9', '0', '1', '2016-01-10 13:28:34', '2016-01-10 13:28:31', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(2, 'p7', '0', '1', '2016-01-16 21:19:01', '2016-01-10 18:10:17', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(3, 'p11', '0', '1', '2016-01-10 13:28:01', '2016-01-10 13:27:27', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(4, 'p6', '0', '1', '2016-01-10 18:10:20', '2016-01-10 18:10:20', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(5, 'f1', '0', '1', '2016-01-10 13:28:43', '2016-01-10 13:28:37', 'samu9197@colorado.edu', 'samu9197@colorado.edu');

-- --------------------------------------------------------

--
-- Table structure for table `userdetails`
--

CREATE TABLE IF NOT EXISTS `userdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(256) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `department` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`,`phone`),
  UNIQUE KEY `email_2` (`email`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `phone_2` (`phone`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `userdetails`
--

INSERT INTO `userdetails` (`id`, `name`, `email`, `password`, `phone`, `department`) VALUES
(7, 'Sairam U J Muttavarapu', 'samu9197@colorado.edu', 'Vz9BXClXCFHLqIAQhpNBWg==', '7208768158', 'MarsOASIS'),
(8, 'Sairam', 'sai.ray30@gmail.com', 'Vz9BXClXCFHLqIAQhpNBWg==', '45455454554', 'CU');

-- --------------------------------------------------------

--
-- Table structure for table `water_conditioning`
--

CREATE TABLE IF NOT EXISTS `water_conditioning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actuator` varchar(128) NOT NULL,
  `current_value` varchar(128) NOT NULL,
  `previous_value` varchar(128) NOT NULL,
  `current_time_stamp` datetime NOT NULL,
  `previous_time_stamp` datetime NOT NULL,
  `current_user_id` varchar(160) NOT NULL,
  `previous_user_id` varchar(160) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sensor` (`actuator`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `water_conditioning`
--

INSERT INTO `water_conditioning` (`id`, `actuator`, `current_value`, `previous_value`, `current_time_stamp`, `previous_time_stamp`, `current_user_id`, `previous_user_id`) VALUES
(1, 'p4', '0', '1', '2016-01-10 13:26:40', '2016-01-10 13:26:37', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(2, 'm2', '0', '1', '2016-01-10 13:26:27', '2016-01-10 13:26:24', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(3, 'm1', '0', '1', '2016-01-10 13:26:20', '2016-01-10 13:26:17', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(4, 'p3', '0', '1', '2016-01-10 13:26:34', '2016-01-10 13:26:29', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(5, 'p5', '0', '1', '2016-01-10 13:26:46', '2016-01-10 13:26:43', 'samu9197@colorado.edu', 'samu9197@colorado.edu');

-- --------------------------------------------------------

--
-- Table structure for table `water_flow_control`
--

CREATE TABLE IF NOT EXISTS `water_flow_control` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actuator` varchar(128) NOT NULL,
  `current_value` varchar(128) NOT NULL,
  `previous_value` varchar(128) NOT NULL,
  `current_time_stamp` datetime NOT NULL,
  `previous_time_stamp` datetime NOT NULL,
  `current_user_id` varchar(160) NOT NULL,
  `previous_user_id` varchar(160) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sensor` (`actuator`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `water_flow_control`
--

INSERT INTO `water_flow_control` (`id`, `actuator`, `current_value`, `previous_value`, `current_time_stamp`, `previous_time_stamp`, `current_user_id`, `previous_user_id`) VALUES
(1, 'p1', '0', '1', '2016-01-10 13:25:59', '2016-01-10 13:25:56', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(2, 'p8', '0', '1', '2016-01-10 13:26:10', '2016-01-10 13:26:06', 'samu9197@colorado.edu', 'samu9197@colorado.edu'),
(3, 'p2', '0', '1', '2016-01-10 13:26:03', '2016-01-10 13:26:01', 'samu9197@colorado.edu', 'samu9197@colorado.edu');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
