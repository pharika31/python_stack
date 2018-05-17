CREATE DATABASE  IF NOT EXISTS `shoppingcart` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `shoppingcart`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: shoppingcart
-- ------------------------------------------------------
-- Server version	5.7.14

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
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` varchar(30) DEFAULT NULL,
  `shipping_address` varchar(5000) DEFAULT NULL,
  `order_date` timestamp NULL DEFAULT NULL,
  `order_summary` varchar(10000) DEFAULT NULL,
  `order_total` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'3','langdale hall','2016-12-04 05:00:00','iphone 7',NULL);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `product_id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `product_name` varchar(30) DEFAULT NULL,
  `product_desc` varchar(50000) DEFAULT NULL,
  `product_price` int(65) DEFAULT NULL,
  `product_avail` int(65) DEFAULT NULL,
  `product_category` varchar(500) DEFAULT NULL,
  `product_image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Iphone 7 Rose Gold','Product description is here',100,50,'Mobile','images/i7.jpg'),(2,'Web Programming text','Product Description is here',100,50,'Books','images/wp.jpg'),(3,'Galaxy s6 edge','Product Description is here',100,50,'Mobile','images/s6.jpg'),(4,'Product Name','Product Description is here',100,50,'Mobile','images/htc626.jpg'),(5,'Product Name','Product Description is here',100,50,'Books','images/head.jpg'),(6,'Product Name','Product Description is here',100,50,'Mobile','images/lenovo.jpg'),(7,'Product Name','Product Description is here',100,50,'Books','images/alg.jpg'),(8,'Product Name','Product Description is here',100,50,'Mobile','images/motog.jpg'),(9,'Product Name','Product Description is here',100,50,'Mobile','images/i6.jpg'),(10,'Product Name','Product Description is here',100,50,'Books','images/code.jpg'),(11,'Oracle 10g Programming','Product Description is here',100,50,'Books','images/oracle.jpg'),(12,'Machine Learning','Product Description goes here',100,50,'Books','images/ml.jpg'),(19,'sitar','Traditional indian classical sitar',300,50,'music','images/sitar.jpg'),(20,'drums','modern drums',300,50,'music','images/drum.jpg');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `useraccounts`
--

DROP TABLE IF EXISTS `useraccounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `useraccounts` (
  `user_id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `password` varchar(30) DEFAULT NULL,
  `fullname` varchar(30) DEFAULT NULL,
  `mobile` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `user_role` varchar(30) DEFAULT NULL,
  `address` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `useraccounts`
--

LOCK TABLES `useraccounts` WRITE;
/*!40000 ALTER TABLE `useraccounts` DISABLE KEYS */;
INSERT INTO `useraccounts` VALUES (1,'demo','Jay Mehta','4702866918','abc@xyz.com','user',NULL),(2,'demo','James','1234561234','harika31.p@gmail.com','user','abcd apartments, GA'),(3,'demo','Sai Harika Punyamurthula','1234567892','harika31.p@gmail.com','admin','georgia state university, langdale hall'),(4,'demo','','','',NULL,NULL),(5,'demo','','Sony','',NULL,NULL),(6,'demo','harika','3456789101','abc@abc.com',NULL,NULL),(7,'demo','abc','1234218901','abc@abc.com',NULL,NULL),(8,'demo','','3456789123','',NULL,NULL),(9,'demo','this','345','tom@gmail.com',NULL,NULL),(10,'demo','this','3456789123','tom@gmail.com',NULL,NULL),(11,'demo','this','3456789123','tom@gmail.com',NULL,NULL),(12,'abc','harika','2456378910','tom@example.com',NULL,NULL),(13,'demo','honey','6786786789','honey@abc.com',NULL,NULL),(14,'demo','honey','6786786789','h@h.com',NULL,NULL),(15,'demo','abc','5675675678','abc@xyz.com',NULL,NULL),(16,'demo','honey','5675678910','abc@xyz.com',NULL,NULL),(17,'demo','harika','234','abc@yrs.com',NULL,NULL),(18,'demo','honey','7777777777','harika31.p@gmail.com',NULL,NULL),(19,'demo','redo','4444444444','redo@abc.com',NULL,NULL);
/*!40000 ALTER TABLE `useraccounts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-15 19:47:39
