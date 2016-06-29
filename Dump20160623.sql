-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: spoca
-- ------------------------------------------------------
-- Server version	5.5.42

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
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `channel` (
  `channel_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `channel_title` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_count` int(10) unsigned DEFAULT NULL,
  `created_at` int(10) unsigned NOT NULL,
  PRIMARY KEY (`channel_id`),
  UNIQUE KEY `channel_title_UNIQUE` (`channel_title`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel`
--

LOCK TABLES `channel` WRITE;
/*!40000 ALTER TABLE `channel` DISABLE KEYS */;
INSERT INTO `channel` VALUES (4,'spoqa',NULL,NULL,0),(5,'spoqa2',NULL,NULL,0),(6,'spoqa3',NULL,NULL,0),(10,'spoqa0',NULL,NULL,0),(11,'s',NULL,NULL,0);
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `channel_active_user`
--

DROP TABLE IF EXISTS `channel_active_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `channel_active_user` (
  `channel_active_user_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `channel_id` bigint(20) unsigned NOT NULL,
  `created_at` int(10) NOT NULL,
  PRIMARY KEY (`channel_active_user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel_active_user`
--

LOCK TABLES `channel_active_user` WRITE;
/*!40000 ALTER TABLE `channel_active_user` DISABLE KEYS */;
INSERT INTO `channel_active_user` VALUES (5,2,10,1466582881),(6,4,10,1466584284),(7,1,10,1466660843),(8,1,11,1466663806),(9,1,6,1466674368),(10,1,5,1466674660),(11,1,4,1466675206);
/*!40000 ALTER TABLE `channel_active_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chatting`
--

DROP TABLE IF EXISTS `chatting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chatting` (
  `chatting_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `comment` longtext NOT NULL,
  `user_id` int(10) unsigned DEFAULT NULL,
  `channel_id` bigint(20) unsigned DEFAULT NULL,
  `file_id` bigint(20) unsigned DEFAULT NULL,
  `type` varchar(45) NOT NULL,
  `permalink` varchar(200) DEFAULT NULL,
  `created_at` int(10) unsigned NOT NULL,
  PRIMARY KEY (`chatting_id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chatting`
--

LOCK TABLES `chatting` WRITE;
/*!40000 ALTER TABLE `chatting` DISABLE KEYS */;
INSERT INTO `chatting` VALUES (1,'aaa',2,7,NULL,'text',NULL,1466569825),(2,'qqq',2,7,NULL,'text',NULL,1466569825),(3,'한글 테스트',2,7,NULL,'text',NULL,1466570205),(4,'유저 아이디 테스트',2,7,NULL,'text',NULL,1466579021),(5,'나도 유저 아이디 테스트',4,7,NULL,'text',NULL,1466579066),(6,'zzz',2,10,NULL,'text',NULL,1466582886),(7,'xxxxx',2,10,NULL,'text',NULL,1466583405),(8,'호우~',2,10,NULL,'text',NULL,1466583968),(9,'비온다',2,10,NULL,'text',NULL,1466584163),(10,'계속 온다',2,10,NULL,'text',NULL,1466584207),(11,'나도 유저 아이디 테스트',4,10,NULL,'text',NULL,1466584286),(12,'zxcvxzcv',2,10,NULL,'text',NULL,1466585599),(13,'흠냐',2,10,NULL,'text',NULL,1466585672),(14,'하나만 주세요',2,10,NULL,'text',NULL,1466585839),(15,'안아',2,10,NULL,'text',NULL,1466585872),(16,'z',2,10,NULL,'text',NULL,1466585895),(17,'드럽게 힘드네',4,10,NULL,'text',NULL,1466585906),(25,'눈 아프다..',2,10,NULL,'text',NULL,1466587378),(26,'배고프다',2,10,NULL,'text',NULL,1466590162),(27,'세션이 죽는건가?',4,10,NULL,'text',NULL,1466590195),(28,'하악하악',2,10,NULL,'text',NULL,1466591547),(29,'하나',2,10,NULL,'text',NULL,1466600942),(30,'둘',2,10,NULL,'text',NULL,1466600946),(31,'셋',2,10,NULL,'text',NULL,1466600948),(32,'넷',2,10,NULL,'text',NULL,1466600951),(33,'다섯',2,10,NULL,'text',NULL,1466601047),(34,'여섯',2,10,NULL,'text',NULL,1466601052),(35,'일곱',2,10,NULL,'text',NULL,1466601081),(38,'asdf',2,10,NULL,'text',NULL,1466654896),(39,'asdf',2,10,NULL,'text','356a192b7913b04c54574d18c28d46e6395428ab',1466655063),(50,'ㅁㄴㅇㄹㅁㄴㄹㅇ',1,10,NULL,'text','e1822db470e60d090affd0956d743cb0e7cdf113',1466666686),(52,'ㅁㄴㅇㄹㄴㅁㄹㅇㅁㄴㅇㄹㅁㄴㄹㅇㅁㄴㅇㄹㅁㄴㅇㄹ',1,10,NULL,'text','a9334987ece78b6fe8bf130ef00b74847c1d3da6',1466666694),(57,'한글한글\n',1,10,NULL,'text','9109c85a45b703f87f1413a405549a2cea9ab556',1466667032),(58,'다시 수정',1,10,NULL,'text','667be543b02294b7624119adc3a725473df39885',1466667035),(59,'파머링크 확인',1,10,NULL,'text','5a5b0f9b7d3f8fc84c3cef8fd8efaaa6c70d75ab',1466677964),(62,'선풍기',1,10,NULL,'text','511a418e72591eb7e33f703f04c3fa16df6c90bd',1466678083),(64,'뭐지?\n',1,10,NULL,'text','c66c65175fecc3103b3b587be9b5b230889c8628',1466678089),(65,'빈칸은 왜 올라가지?\n',1,10,NULL,'text','2a459380709e2fe4ac2dae5733c73225ff6cfee1',1466678095),(66,'배고프다',1,10,NULL,'text','59129aacfb6cebbe2c52f30ef3424209f7252e82',1466678163),(68,'ㅁㄴㅇㄹㄴㅁㅇㄹㄴㅁㅇㄹ',1,10,NULL,'text','b4c96d80854dd27e76d8cc9e21960eebda52e962',1466678171),(70,'ㅁㄴㅇㄹㅁㄴㅇㄹㅁㄴㄹ',1,10,NULL,'text','b7103ca278a75cad8f7d065acda0c2e80da0b7dc',1466678174),(72,'확인',1,10,NULL,'text','c097638f92de80ba8d6c696b26e6e601a5f61eb7',1466678211),(74,'ㅁㅇㄴㄹㅁㄴㅇㄹ',1,10,NULL,'text','1f1362ea41d1bc65be321c0a378a20159f9a26d0',1466678214),(76,'asdf\n',1,10,NULL,'text','d54ad009d179ae346683cfc3603979bc99339ef7',1466678230),(77,'asdf\n',1,10,NULL,'text','d321d6f7ccf98b51540ec9d933f20898af3bd71e',1466678234),(78,'asdf\n',1,10,NULL,'text','eb4ac3033e8ab3591e0fcefa8c26ce3fd36d5a0f',1466678235),(79,'sa\ndf',1,10,NULL,'text','b74f5ee9461495ba5ca4c72a7108a23904c27a05',1466678235),(80,'s\na',1,10,NULL,'text','b888b29826bb53dc531437e723738383d8339b56',1466678235),(81,'df\n',1,10,NULL,'text','1d513c0bcbe33b2e7440e5e14d0b22ef95c9d673',1466678235),(82,'a\n',1,10,NULL,'text','76546f9a641ede2beab506b96df1688d889e629a',1466678241),(83,'asdf\n',1,10,NULL,'text','7d7116e23efef7292cad5e6f033d9a962708228c',1466678244),(84,'ㅁㄴㅇㄹㄴㅇㄹ',1,10,NULL,'text','be461a0cd1fda052a69c3fd94f8cf5f6f86afa34',1466678247),(86,'한글은 왜 두번이지?\n',1,10,NULL,'text','3c26dffc8a2e8804dfe2c8a1195cfaa5ef6d0014',1466678362),(87,'이번엔 걸리는건가?!',1,10,NULL,'text','e62d7f1eb43d87c202d2f164ba61297e71be80f4',1466678368),(94,'개행문자인거냐?\n',1,10,NULL,'text','215bb47da8fac3342b858ac3db09b033c6c46e0b',1466678502),(95,'진짜인듯;;왜 한글만?\n',1,10,NULL,'text','8e63fd3e77796b102589b1ba1e4441c7982e4132',1466678509),(96,'두줄이 나오도록 길게 써보자두줄이 나오도록 길게 써보자두줄이 나오도록 길게 써보자두줄이 나오도록 길게 써보자두줄이 나오도록 길게 써보자두줄이 나오도록 길게 써보자두줄이 나오도록 길게 써보자두줄이 나오도록 길게 써보자두줄이 나오도록 길게 써보자\n',1,10,NULL,'text','6fb84aed32facd1299ee1e77c8fd2b1a6352669e',1466682040);
/*!40000 ALTER TABLE `chatting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `file`
--

DROP TABLE IF EXISTS `file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `file` (
  `file_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned DEFAULT NULL,
  `channel_id` bigint(20) unsigned NOT NULL,
  `file_name` varchar(200) NOT NULL,
  `path` varchar(100) NOT NULL,
  `created_at` int(10) unsigned NOT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file`
--

LOCK TABLES `file` WRITE;
/*!40000 ALTER TABLE `file` DISABLE KEYS */;
/*!40000 ALTER TABLE `file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `ouath` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'hare','uiandwe@gmail.com','123qwe',NULL),(2,'222','222','222',NULL),(3,'2223','2223','222',NULL),(4,'123123','123123','123123',NULL),(5,'test','test1000@test.com','123qwe',NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-23 20:44:48
