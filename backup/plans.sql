-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: it_plan
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `plan_north`
--

DROP TABLE IF EXISTS `plan_north`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plan_north` (
  `id` varchar(50) NOT NULL,
  `site` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `item` varchar(500) NOT NULL,
  `progress` varchar(50) NOT NULL,
  `details` text NOT NULL,
  `ttcm` varchar(500) DEFAULT ' ',
  `owner` varchar(50) NOT NULL,
  `week` varchar(50) NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_north`
--

LOCK TABLES `plan_north` WRITE;
/*!40000 ALTER TABLE `plan_north` DISABLE KEYS */;
INSERT INTO `plan_north` VALUES ('001409802371098b88ecda6f747492183c13dd44501a557000','SHA2','项目','test','10%','test','fsa','test','2014WW36',1409802371.1),('0014137764881832259406ee4d8480a8e0e7440b3e40719000','NNG1','项目','fsa','50%','fdsa','fsa','fsa','2014WW33',1413776488.18),('001413776558694104749727257470f93d6886c8bfb3467000','CTU4','运维','fsa','10%','fsa','fsa','fsa','2014WW38',1413776558.69),('001413778036010bc795158340b4ed0a1840f9ad9b2ce34000','NNG1','项目','fdsa','100%','fdsa','fsa','fsa','2014WW37',1413778036.01),('0014137781323944b3c881f08594b9c96371253c26a41f6000','CAN4','项目','fsa','100%','fsa','fas','fas','2014WW35',1413778132.39),('001413778507464171a366c556c4bc59b313dacbb2fd348000','PEK3','运维','asfas','100%','fdsa','fsa','fas','2014WW43',1413778507.46),('001413779171651b36a44c2f00c4db798c9ab11ecea4494000','PEK8','运维','fdsa','30%','fsa','fsa','fsa','2014WW43',1413779171.65),('001413783491818a739cc7f824e49208f8a124a301fa8ca000','HRB1','项目','afsf','50%','fsa','fsa','fsa','2014WW43',1413783491.82);
/*!40000 ALTER TABLE `plan_north` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plan_south`
--

DROP TABLE IF EXISTS `plan_south`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plan_south` (
  `id` varchar(50) NOT NULL,
  `site` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `item` varchar(500) NOT NULL,
  `progress` varchar(50) NOT NULL,
  `details` text NOT NULL,
  `ttcm` varchar(500) DEFAULT ' ',
  `owner` varchar(50) NOT NULL,
  `week` varchar(50) NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_south`
--

LOCK TABLES `plan_south` WRITE;
/*!40000 ALTER TABLE `plan_south` DISABLE KEYS */;
INSERT INTO `plan_south` VALUES ('00140981629982952fb4c71dcd749cfb6997a2b6738b761000','WUH2','项目','mdf','100%','test','','xuchao','2014WW31',1409816299.83),('0014099296399380187cd12ab6545348244a0b4d11c3d4c000','CTU4','项目','www','90%','ttt','fdsa','xuchao','2014WW32',1409929639.94),('0014099320287997a7018c7de8f4513b3336f840cec0a09000','NNG1','项目','hhh','70%','jjj','ff','xuchao','2014WW33',1409932028.8),('001413726163685487c19fd91b54b728f3452ecbc705372000','CAN4','运维','fdsaf','30%','fsaf','fsaf','fsaf','2014WW42',1413726163.69),('001413729506064d465b944817241c7b5410819a74285bf000','WUH2','项目','asfs','100%','fdsa','fsaf','fasf','2014WW42',1413729506.06),('001413729737735cdfc359602dd4482be435a32b01b4d5a000','XMN2','项目','fsaf','30%','fdsa','fsa','fsad','2014WW42',1413729737.74),('0014137298159346baa75cbc83a4932a4cf7a9ebffd6213000','CTU4','运维','afas','100%','fsaf','sadf','fsaf','2014WW42',1413729815.93),('001413730386748fde30be5d0964d5ba5a1e2aad159097f000','CAN4','项目','fsa','30%','fsaf','fsa','fsa','2014WW34',1413730386.75),('00141377743969596728166478340e4896b29b6369a3790000','CTU4','运维','safsa','10%','fsadf','fdsa','fsad','2014WW43',1413777439.7),('00141377897412508896b3214654d4d80716b55998e1862000','XIY2','项目','fdsa','100%','fdsa','fdsa','fsa','2014WW43',1413778974.13),('001413783474004849c1d48dd9a469394358d05cfa75c75000','WUH2','运维','fa','50%','fsa','fsa','fsa','2014WW43',1413783474),('001413788896100e1b3fed4d55547389293652b74a8dd13000','CTU4','运维','daf','100%','fda','fas','fdsa','2014WW43',1413788896.1),('0014137889164612859d5233807438d87e78c957c342801000','CTU4','项目','fsf','50%','dfa','fda','fdas','2014WW43',1413788916.46);
/*!40000 ALTER TABLE `plan_south` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `name` varchar(50) NOT NULL,
  `image` varchar(500) NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_email` (`email`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('0010018336417540987fff4508f43fbaed718e263442526000','admin@example.com','e10adc3949ba59abbe56e057f20f883e',1,'admin','',1402909113.628);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-10-22  9:37:44
