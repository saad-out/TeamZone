-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: tz_dev_db
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.20.04.2

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
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` varchar(128) NOT NULL,
  `country_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES ('0af60e66-e6dd-4151-be49-c30ce07c1aab','2023-03-11 20:22:33','2023-03-11 20:22:33','Marrakech','bdbe7ed1-2a28-4dc1-b34e-cf33a90650c3'),('3dc0bdf6-3822-4872-af0d-d1178027b3c3','2023-03-11 20:22:33','2023-03-11 20:22:33','Fes','bdbe7ed1-2a28-4dc1-b34e-cf33a90650c3'),('a1b61da9-7ede-4642-81df-b5a48b4cf46a','2023-03-11 20:22:33','2023-03-11 20:22:33','Abuja','8631e9a1-3b9e-4e42-a707-1ce312e01ffe'),('f7d2092f-00f1-4196-ad7f-a5e7a814349e','2023-03-11 20:22:33','2023-03-11 20:22:33','Lagos','8631e9a1-3b9e-4e42-a707-1ce312e01ffe');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES ('8631e9a1-3b9e-4e42-a707-1ce312e01ffe','2023-03-11 20:22:33','2023-03-11 20:22:33','Nigeria'),('bdbe7ed1-2a28-4dc1-b34e-cf33a90650c3','2023-03-11 20:22:33','2023-03-11 20:22:33','Morocco');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notification` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `sender_id` varchar(60) NOT NULL,
  `receiver_id` varchar(60) NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `message` text,
  PRIMARY KEY (`id`),
  KEY `sender_id` (`sender_id`),
  KEY `receiver_id` (`receiver_id`),
  CONSTRAINT `notification_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `teams` (`id`),
  CONSTRAINT `notification_ibfk_2` FOREIGN KEY (`receiver_id`) REFERENCES `teams` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sports`
--

DROP TABLE IF EXISTS `sports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sports` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sports`
--

LOCK TABLES `sports` WRITE;
/*!40000 ALTER TABLE `sports` DISABLE KEYS */;
INSERT INTO `sports` VALUES ('6c078938-8e81-4a11-8356-68ffde2e2c6e','2023-03-11 20:22:33','2023-03-11 20:22:33','Football'),('ef7c02ae-2ac2-419f-83ca-d3e62fd0dcbc','2023-03-11 20:22:33','2023-03-11 20:22:33','Basketball');
/*!40000 ALTER TABLE `sports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_connection`
--

DROP TABLE IF EXISTS `team_connection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team_connection` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `team_one_id` varchar(60) NOT NULL,
  `team_two_id` varchar(60) NOT NULL,
  `game_date` datetime DEFAULT NULL,
  `is_completed` tinyint(1) DEFAULT NULL,
  `team_one_score` int DEFAULT NULL,
  `team_two_score` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `team_one_id` (`team_one_id`),
  KEY `team_two_id` (`team_two_id`),
  CONSTRAINT `team_connection_ibfk_1` FOREIGN KEY (`team_one_id`) REFERENCES `teams` (`id`),
  CONSTRAINT `team_connection_ibfk_2` FOREIGN KEY (`team_two_id`) REFERENCES `teams` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_connection`
--

LOCK TABLES `team_connection` WRITE;
/*!40000 ALTER TABLE `team_connection` DISABLE KEYS */;
/*!40000 ALTER TABLE `team_connection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_membership`
--

DROP TABLE IF EXISTS `team_membership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team_membership` (
  `team_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  PRIMARY KEY (`team_id`,`user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `team_membership_ibfk_1` FOREIGN KEY (`team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `team_membership_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_membership`
--

LOCK TABLES `team_membership` WRITE;
/*!40000 ALTER TABLE `team_membership` DISABLE KEYS */;
INSERT INTO `team_membership` VALUES ('3b95c869-6d12-44dc-b6ed-0f76cd7cdbd4','04995a4b-82c7-4edb-b4c1-c777335e643b'),('da015206-1fd2-4281-a629-ca044aebbe5a','1201860e-71c7-41fe-abea-c6ab2d92f368'),('fa0a3d6e-ba63-4ad5-83dd-d594823f8d30','1272a106-3159-4315-aa13-df357dd93310'),('66639913-429b-4a16-9b45-44771610d386','1468bc63-178d-4269-909d-8d416ea71710'),('66639913-429b-4a16-9b45-44771610d386','1906eb12-d5d0-4946-8e5f-07a3f3b369da'),('da015206-1fd2-4281-a629-ca044aebbe5a','19755c79-d9ea-4e61-836f-f238a030fd79'),('66639913-429b-4a16-9b45-44771610d386','308f29bc-bd75-45c5-9f85-1a615f19f48b'),('fa0a3d6e-ba63-4ad5-83dd-d594823f8d30','308f29bc-bd75-45c5-9f85-1a615f19f48b'),('fa0a3d6e-ba63-4ad5-83dd-d594823f8d30','3f16922f-e3f5-44c3-a626-1a80c959397b'),('3b95c869-6d12-44dc-b6ed-0f76cd7cdbd4','436cde70-9e13-4459-bb36-32a550136d94'),('da015206-1fd2-4281-a629-ca044aebbe5a','568acaf0-bdc6-4334-b2fb-80642cf2233d'),('da015206-1fd2-4281-a629-ca044aebbe5a','582652af-f9ed-4ebb-a598-4592cb7b6a81'),('66639913-429b-4a16-9b45-44771610d386','58641f75-ecc8-4ea2-b6cd-687a3076b157'),('66639913-429b-4a16-9b45-44771610d386','6b7f40da-b26f-4591-9977-d3084192bd5a'),('fa0a3d6e-ba63-4ad5-83dd-d594823f8d30','6b7f40da-b26f-4591-9977-d3084192bd5a'),('66639913-429b-4a16-9b45-44771610d386','73665190-392f-4b10-949c-e3e8e1d19996'),('da015206-1fd2-4281-a629-ca044aebbe5a','7e905024-3ad2-404a-be8c-87ef377ca7ad'),('66639913-429b-4a16-9b45-44771610d386','7ff7f02d-d512-4106-af64-133cf83d48ea'),('3b95c869-6d12-44dc-b6ed-0f76cd7cdbd4','85d75ecf-d23f-4ce5-b1e4-ffba3ef0092d'),('da015206-1fd2-4281-a629-ca044aebbe5a','8671ce69-6985-4d04-93f6-5b158be3623f'),('3b95c869-6d12-44dc-b6ed-0f76cd7cdbd4','8dd6d588-ccf9-49a2-ae32-ab346efec2cd'),('66639913-429b-4a16-9b45-44771610d386','8ebce142-909a-4e08-9ac6-c9327a555513'),('fa0a3d6e-ba63-4ad5-83dd-d594823f8d30','929d4fa9-52ec-458f-9657-2084a8890e7b'),('66639913-429b-4a16-9b45-44771610d386','9f04fe6e-76b7-438b-9cd9-2775bdcee585'),('fa0a3d6e-ba63-4ad5-83dd-d594823f8d30','9f04fe6e-76b7-438b-9cd9-2775bdcee585'),('3b95c869-6d12-44dc-b6ed-0f76cd7cdbd4','a78e75aa-a398-42f5-aa25-7455694cdd6a'),('da015206-1fd2-4281-a629-ca044aebbe5a','a78e75aa-a398-42f5-aa25-7455694cdd6a'),('3b95c869-6d12-44dc-b6ed-0f76cd7cdbd4','af38cbc2-47f4-44ac-beea-b25c336fbf23'),('da015206-1fd2-4281-a629-ca044aebbe5a','af38cbc2-47f4-44ac-beea-b25c336fbf23'),('66639913-429b-4a16-9b45-44771610d386','b9751846-fd18-475d-a4fa-8f676d4e1389'),('3b95c869-6d12-44dc-b6ed-0f76cd7cdbd4','c4f3b6c9-1457-4a4a-88da-eacbd8a8217f'),('da015206-1fd2-4281-a629-ca044aebbe5a','c4f3b6c9-1457-4a4a-88da-eacbd8a8217f'),('66639913-429b-4a16-9b45-44771610d386','eaaf9050-9131-4538-ae90-abc0ddc5d499'),('fa0a3d6e-ba63-4ad5-83dd-d594823f8d30','ed040eb5-bab3-4ad8-889a-f7ccf74b14fd'),('da015206-1fd2-4281-a629-ca044aebbe5a','f3a97880-c6af-42e2-b741-6a744d84c3d7'),('da015206-1fd2-4281-a629-ca044aebbe5a','fd1ef163-9090-47a8-83ff-ef4b1ecb79c0');
/*!40000 ALTER TABLE `team_membership` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teams` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` varchar(128) NOT NULL,
  `bio` text,
  `image` varchar(128) DEFAULT NULL,
  `sport_id` varchar(60) NOT NULL,
  `city_id` varchar(60) NOT NULL,
  `leader_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sport_id` (`sport_id`),
  KEY `city_id` (`city_id`),
  KEY `leader_id` (`leader_id`),
  CONSTRAINT `teams_ibfk_1` FOREIGN KEY (`sport_id`) REFERENCES `sports` (`id`),
  CONSTRAINT `teams_ibfk_2` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`),
  CONSTRAINT `teams_ibfk_3` FOREIGN KEY (`leader_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES ('3b95c869-6d12-44dc-b6ed-0f76cd7cdbd4','2023-03-11 20:22:33','2023-03-11 20:22:33','Atlas Lions Basketball','It\'s the Atlas Lions Basketball team','team_default.jpg','ef7c02ae-2ac2-419f-83ca-d3e62fd0dcbc','3dc0bdf6-3822-4872-af0d-d1178027b3c3','582652af-f9ed-4ebb-a598-4592cb7b6a81'),('66639913-429b-4a16-9b45-44771610d386','2023-03-11 20:22:33','2023-03-11 20:22:33','Super Eagles','It\'s the Super Eagles team','team_default.jpg','6c078938-8e81-4a11-8356-68ffde2e2c6e','f7d2092f-00f1-4196-ad7f-a5e7a814349e','8ebce142-909a-4e08-9ac6-c9327a555513'),('da015206-1fd2-4281-a629-ca044aebbe5a','2023-03-11 20:22:33','2023-03-11 20:22:33','Atlas Lions Football','It\'s the Atlas Lions Football team','team_default.jpg','6c078938-8e81-4a11-8356-68ffde2e2c6e','0af60e66-e6dd-4151-be49-c30ce07c1aab','582652af-f9ed-4ebb-a598-4592cb7b6a81'),('fa0a3d6e-ba63-4ad5-83dd-d594823f8d30','2023-03-11 20:22:33','2023-03-11 20:22:33','D\'Tigers','It\'s the D\'Tigers team','team_default.jpg','ef7c02ae-2ac2-419f-83ca-d3e62fd0dcbc','a1b61da9-7ede-4642-81df-b5a48b4cf46a','6b7f40da-b26f-4591-9977-d3084192bd5a');
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` varchar(128) NOT NULL,
  `username` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `image` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('04995a4b-82c7-4edb-b4c1-c777335e643b','2023-03-11 20:22:33','2023-03-11 20:22:33','Sanaa Khairi','skhairi','skhairi@example.com','skhairi.46695','user_default.jpg'),('1201860e-71c7-41fe-abea-c6ab2d92f368','2023-03-11 20:22:33','2023-03-11 20:22:33','Hassan El Kaddouri','hel','helkaddouri@example.com','hel-38811','user_default.jpg'),('1272a106-3159-4315-aa13-df357dd93310','2023-03-11 20:22:33','2023-03-11 20:22:33','Bola Adeyemo','badeyemo','bola@example.com','badeyemo.80996','user_default.jpg'),('1468bc63-178d-4269-909d-8d416ea71710','2023-03-11 20:22:33','2023-03-11 20:22:33','Oluwaseun Adeyemi','oadeyemi','oluwaseun@example.com','oadeyemi%90907','user_default.jpg'),('1906eb12-d5d0-4946-8e5f-07a3f3b369da','2023-03-11 20:22:33','2023-03-11 20:22:33','Abdullahi Musa','amusa','abdullahi@example.com','amusa$42646','user_default.jpg'),('19755c79-d9ea-4e61-836f-f238a030fd79','2023-03-11 20:22:33','2023-03-11 20:22:33','Karim Bouzid','kbouzid','kbouzid@example.com','kbouzid$91070','user_default.jpg'),('308f29bc-bd75-45c5-9f85-1a615f19f48b','2023-03-11 20:22:33','2023-03-11 20:22:33','Chidi Obi','cobi','chidi@example.com','cobi%25805','user_default.jpg'),('3f16922f-e3f5-44c3-a626-1a80c959397b','2023-03-11 20:22:33','2023-03-11 20:22:33','Tayo Oyekan','toyekan','tayo@example.com','toyekan.35563','user_default.jpg'),('436cde70-9e13-4459-bb36-32a550136d94','2023-03-11 20:22:33','2023-03-11 20:22:33','Ibtissam El Bakkali','iel','ielbakkali@example.com','iel.46999','user_default.jpg'),('568acaf0-bdc6-4334-b2fb-80642cf2233d','2023-03-11 20:22:33','2023-03-11 20:22:33','Omar El Khattabi','oel','oelkhattabi@example.com','oel=59069','user_default.jpg'),('582652af-f9ed-4ebb-a598-4592cb7b6a81','2023-03-11 20:22:33','2023-03-11 20:22:33','Youssef El Alaoui','yel','yelalaoui@example.com','yel-18301','user_default.jpg'),('58641f75-ecc8-4ea2-b6cd-687a3076b157','2023-03-11 20:22:33','2023-03-11 20:22:33','Adetola Oladele','aoladele','adetola@example.com','aoladele%29544','user_default.jpg'),('6b7f40da-b26f-4591-9977-d3084192bd5a','2023-03-11 20:22:33','2023-03-11 20:22:33','Tunde Bakare','tbakare','tunde@example.com','tbakare%55014','user_default.jpg'),('73665190-392f-4b10-949c-e3e8e1d19996','2023-03-11 20:22:33','2023-03-11 20:22:33','Fatima Ibrahim','fibrahim','fatima@example.com','fibrahim.91266','user_default.jpg'),('7e905024-3ad2-404a-be8c-87ef377ca7ad','2023-03-11 20:22:33','2023-03-11 20:22:33','Lina Benali','lbenali','lbenali@example.com','lbenali=32954','user_default.jpg'),('7ff7f02d-d512-4106-af64-133cf83d48ea','2023-03-11 20:22:33','2023-03-11 20:22:33','Ifeoma Okafor','iokafor','ifeoma@example.com','iokafor=95370','user_default.jpg'),('85d75ecf-d23f-4ce5-b1e4-ffba3ef0092d','2023-03-11 20:22:33','2023-03-11 20:22:33','Brahim Cherif','bcherif','bcherif@example.com','bcherif%44203','user_default.jpg'),('8671ce69-6985-4d04-93f6-5b158be3623f','2023-03-11 20:22:33','2023-03-11 20:22:33','Fatima Ahmed','fahmed','fahmed@example.com','fahmed-17682','user_default.jpg'),('8dd6d588-ccf9-49a2-ae32-ab346efec2cd','2023-03-11 20:22:33','2023-03-11 20:22:33','Anas Amrani','aamrani','aamrani@example.com','aamrani$59178','user_default.jpg'),('8ebce142-909a-4e08-9ac6-c9327a555513','2023-03-11 20:22:33','2023-03-11 20:22:33','Chinonso Okoli','cokoli','chinonso@example.com','cokoli=39817','user_default.jpg'),('929d4fa9-52ec-458f-9657-2084a8890e7b','2023-03-11 20:22:33','2023-03-11 20:22:33','Femi Ogun','fogun','femi@example.com','fogun.33932','user_default.jpg'),('9f04fe6e-76b7-438b-9cd9-2775bdcee585','2023-03-11 20:22:33','2023-03-11 20:22:33','Yemi Oluwafemi','yoluwafemi','yemi@example.com','yoluwafemi$27632','user_default.jpg'),('a78e75aa-a398-42f5-aa25-7455694cdd6a','2023-03-11 20:22:33','2023-03-11 20:22:33','Mohammed Chaouki','mchaouki','mchaouki@example.com','mchaouki%42402','user_default.jpg'),('af38cbc2-47f4-44ac-beea-b25c336fbf23','2023-03-11 20:22:33','2023-03-11 20:22:33','Ayoub El Moutawakil','ael','aelmoutawakil@example.com','ael.87444','user_default.jpg'),('b9751846-fd18-475d-a4fa-8f676d4e1389','2023-03-11 20:22:33','2023-03-11 20:22:33','Ngozi Madu','nmadu','ngozi@example.com','nmadu.32494','user_default.jpg'),('c4f3b6c9-1457-4a4a-88da-eacbd8a8217f','2023-03-11 20:22:33','2023-03-11 20:22:33','Soukaina Ouazzani','souazzani','souazzani@example.com','souazzani%30734','user_default.jpg'),('eaaf9050-9131-4538-ae90-abc0ddc5d499','2023-03-11 20:22:33','2023-03-11 20:22:33','Emeka Nwosu','enwosu','emeka@example.com','enwosu$68432','user_default.jpg'),('ed040eb5-bab3-4ad8-889a-f7ccf74b14fd','2023-03-11 20:22:33','2023-03-11 20:22:33','Adanna Chukwu','achukwu','adanna@example.com','achukwu.50708','user_default.jpg'),('f3a97880-c6af-42e2-b741-6a744d84c3d7','2023-03-11 20:22:33','2023-03-11 20:22:33','Nora El Fassi','nel','nelfassi@example.com','nel$50566','user_default.jpg'),('fd1ef163-9090-47a8-83ff-ef4b1ecb79c0','2023-03-11 20:22:33','2023-03-11 20:22:33','Amina Berrada','aberrada','aberrada@example.com','aberrada%75661','user_default.jpg');
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

-- Dump completed on 2023-03-11 20:24:15
