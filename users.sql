-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: users
-- ------------------------------------------------------
-- Server version	5.6.28

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
-- Table structure for table `lists`
--

DROP TABLE IF EXISTS `lists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lists` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `add_id` varchar(255) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL,
  `updated_at` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lists`
--

LOCK TABLES `lists` WRITE;
/*!40000 ALTER TABLE `lists` DISABLE KEYS */;
INSERT INTO `lists` VALUES (1,'iPhone','44','44',NULL,NULL),(2,'Moutain Bike','47','48',NULL,NULL),(3,'Mac Pro','45','45',NULL,NULL),(4,'Deuter Hiking Bag','48','47',NULL,NULL),(5,'Rolex Watch','48','48',NULL,NULL),(6,'1-night stay at Boracay','44','44',NULL,NULL),(7,'Bbq Grill','47','45',NULL,NULL),(8,'Zumba DVD','48','46',NULL,NULL);
/*!40000 ALTER TABLE `lists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (44,'Devan','Wong','devan.wong@yahoo.com','$2b$12$CpzzHa9RcMnL.Kw3iEIls.2X.cf1BWqc7vgoOGy68tQ5qOWt9kZIG','2016-09-25 19:05:49','2016-09-25 19:05:49'),(45,'jill','jill','jill@apple.com','$2b$12$VRfRCkjZR0Tyx0Gj1URl6OeTOkdOaAPVtdTs1YcjrVcPwuH.UgoOq','2016-09-26 09:17:49','2016-09-26 09:17:49'),(46,'Marloon Cantigo','Marmar','mar@apple.com','$2b$12$fABMSISOgcQHh.1VKnrMB.IJNY8GBQjq3nRFpfMhP54jgBitFuVfu','2016-09-26 10:13:03','2016-09-26 10:13:03'),(47,'kennyko','kennyko','kenny@gmail.com','$2b$12$cOWG157KyJRWn5OddPoCrOLLkubwIurvwpFTO/Q9CvhqStVLVOjb2','2016-10-06 22:56:49','2016-10-06 22:56:49'),(48,'HarveyHarv','HarvAYYYYY','harvey@apple.com','$2b$12$Hda4JqE45UMUeNYu/EkQ.u361eYQ75iETLrFOrDN90P6pt664iply','2016-10-07 15:33:23','2016-10-07 15:33:23'),(49,'bob','bobb','bob@apple.com','$2b$12$a41MVW9edCCDTvkJ9d7q1uC7aKwbROlAy1ghcOw7o/69dif3BHn2e','2016-10-08 12:07:03','2016-10-08 12:07:03');
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

-- Dump completed on 2016-10-08 12:23:04
