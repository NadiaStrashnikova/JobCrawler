-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: jobdb
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `jobadv`
--

DROP TABLE IF EXISTS `jobadv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobadv` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `post_date` date NOT NULL,
  `skills` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_date` (`name`,`post_date`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobadv`
--

LOCK TABLES `jobadv` WRITE;
/*!40000 ALTER TABLE `jobadv` DISABLE KEYS */;
INSERT INTO `jobadv` VALUES (1,'Senior Python Developer','2024-06-22','Python; C/C++; Matlab; '),(2,'PYTHON DEVELOPER','2022-06-22','Python; MySQL; SQL; Redis; NoSQL; Docker; Kubernetes; '),(3,'Python Developer with Cloud','2022-06-22','Английски; Python; SQL; Spark; Hadoop; AWS; Azure; Scala; Java; '),(4,'SQL & Python Data Engineer','2022-06-22','Английски; SQL; Python; Spark; Azure; Azure; Azure; '),(5,'QA Engineer (Python) - FinTech','2021-06-22','Английски; Python; Linux; C/C++; Kubernetes; SQL; Jira; Jenkins; Jenkins; '),(6,'Senior Python Developer','2020-06-22','Python; C/C++; '),(7,'Data scientist','2022-06-29','Английски; Немски; Hadoop; SQL; Python; '),(8,'Technology Consultant','2022-06-29','Tomcat; Python; Java; JavaScript; C#; VBA; Excel; Windows; SQL; PostgreSQL; HTML/CSS; HTML/CSS; HTML/CSS; '),(9,'Machine Learning Engineer','2022-06-28','Английски; Python; SQL; Docker; '),(10,'Risk Data Scientist, CEE Ancillary Modelling Team','2022-06-28','Excel; Python; Matlab; '),(11,'Data Operations Specialist','2022-06-28','SQL; MS SQL; MySQL; PostgreSQL; Azure; AWS; Python; JavaScript; JavaScript; JavaScript; '),(12,'SITE RELIABILITY ENGINEER','2022-06-28','Ansible; Golang; Python; Kubernetes; OpenStack; VMware; VMware; '),(13,'SENIOR SOFTWARE ENGINEER (ANGULARjs)','2022-06-28','Angular; JavaScript; Java; Python; Linux; Jenkins; '),(14,'QA Engineer','2022-06-28','Selenium; SoapUI; JMeter; Jira; Confluence; Android; iOS; JavaScript; Python; '),(15,'Software DevOps Engineer','2022-06-28','Azure; Kubernetes; Grafana; Python; Linux; SQL; NoSQL; Jenkins; Jenkins; '),(16,'C# DEVELOPER FOR AUTOMOTIVE','2022-06-28','Английски; C#; .NET; C/C++; Python; Jenkins; Jenkins; '),(17,'Junior Google Cloud Data Engineer with SQL ( GCP Data Intern)','2027-06-22','GCP; SQL; Python; Python; '),(18,'MONITORING SOLUTIONS EXPERT','2027-06-22','Grafana; Windows; Linux; Ansible; Python; '),(19,'Senior Automation QA Engineer','2027-06-22','Java; C#; JavaScript; Python; NUnit; Selenium; SoapUI; Cucumber; Docker; Jira; Jenkins; Jenkins; Jenkins; '),(20,'Business Consultant – Risk and Quant','2027-06-22',''),(21,'IT Senior Operations Engineer','2027-06-22','MySQL; SQL; Python; Perl; Linux; Windows; AWS; AWS; AWS; '),(22,'Embedded Software Test Engineer','2027-06-22','C/C++; Python; Jira; '),(23,'Data Management Coordinator','2027-06-22',''),(24,'Senior Data Engineer','2027-06-22','Power BI; Tableau; SQL; Python; Python; Python; Python; Python; ');
/*!40000 ALTER TABLE `jobadv` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-29 13:24:48
