/*
SQLyog Ultimate v12.08 (64 bit)
MySQL - 5.6.37 : Database - polls
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`polls` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `polls`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add choice',7,'add_choice'),(20,'Can change choice',7,'change_choice'),(21,'Can delete choice',7,'delete_choice'),(22,'Can add question',8,'add_question'),(23,'Can change question',8,'change_question'),(24,'Can delete question',8,'delete_question'),(25,'Can add picture',9,'add_picture'),(26,'Can change picture',9,'change_picture'),(27,'Can delete picture',9,'delete_picture'),(28,'Can add zixun',10,'add_zixun'),(29,'Can change zixun',10,'change_zixun'),(30,'Can delete zixun',10,'delete_zixun'),(31,'Can add snippet',11,'add_snippet'),(32,'Can change snippet',11,'change_snippet'),(33,'Can delete snippet',11,'delete_snippet'),(34,'Can add ss',12,'add_ss'),(35,'Can change ss',12,'change_ss'),(36,'Can delete ss',12,'delete_ss'),(37,'Can view log entry',1,'view_logentry'),(38,'Can view permission',3,'view_permission'),(39,'Can view group',2,'view_group'),(40,'Can view user',4,'view_user'),(41,'Can view content type',5,'view_contenttype'),(42,'Can view session',6,'view_session'),(43,'Can view picture',9,'view_picture'),(44,'Can add stock data',13,'add_stockdata'),(45,'Can change stock data',13,'change_stockdata'),(46,'Can delete stock data',13,'delete_stockdata'),(47,'Can view stock data',13,'view_stockdata'),(48,'Can add stock',14,'add_stock'),(49,'Can change stock',14,'change_stock'),(50,'Can delete stock',14,'delete_stock'),(51,'Can view stock',14,'view_stock'),(52,'Can view ss',12,'view_ss'),(53,'Can view zixun',10,'view_zixun'),(54,'Can view snippet',11,'view_snippet'),(55,'Can add model a',15,'add_modela'),(56,'Can change model a',15,'change_modela'),(57,'Can delete model a',15,'delete_modela'),(58,'Can view model a',15,'view_modela'),(59,'Can add algorithm',16,'add_algorithm'),(60,'Can change algorithm',16,'change_algorithm'),(61,'Can delete algorithm',16,'delete_algorithm'),(62,'Can view algorithm',16,'view_algorithm'),(63,'Can add technical list',17,'add_technicallist'),(64,'Can change technical list',17,'change_technicallist'),(65,'Can delete technical list',17,'delete_technicallist'),(66,'Can view technical list',17,'view_technicallist'),(67,'Can add strategy pre',18,'add_strategypre'),(68,'Can change strategy pre',18,'change_strategypre'),(69,'Can delete strategy pre',18,'delete_strategypre'),(70,'Can view strategy pre',18,'view_strategypre'),(71,'Can add strategy',19,'add_strategy'),(72,'Can change strategy',19,'change_strategy'),(73,'Can delete strategy',19,'delete_strategy'),(74,'Can view strategy',19,'view_strategy'),(75,'Can add technical data',20,'add_technicaldata'),(76,'Can change technical data',20,'change_technicaldata'),(77,'Can delete technical data',20,'delete_technicaldata'),(78,'Can view technical data',20,'view_technicaldata'),(79,'Can add stock cw data',21,'add_stockcwdata'),(80,'Can change stock cw data',21,'change_stockcwdata'),(81,'Can delete stock cw data',21,'delete_stockcwdata'),(82,'Can view stock cw data',21,'view_stockcwdata'),(83,'Can add model pre',22,'add_modelpre'),(84,'Can change model pre',22,'change_modelpre'),(85,'Can delete model pre',22,'delete_modelpre'),(86,'Can view model pre',22,'view_modelpre');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values (1,'pbkdf2_sha256$36000$bcQ9w77u6CAm$t06HZWV/AQiBOvUWrymHTkNfwAp2lxzQ3uKKBUOe+Fs=','2017-07-13 06:28:47.738180',1,'admin','18218218211','','test@email.com',1,1,'2017-06-19 07:34:22.072060'),(2,'pbkdf2_sha256$120000$fRFXaHVzaCXH$0YVtmKetILWvdVCFaffuq5BymXe11Vzw+pYUiB6/LTc=','2019-05-16 14:21:21.082923',1,'liyong','15015015015','','123456',0,1,'2018-12-08 06:53:32.648222'),(3,'pbkdf2_sha256$120000$IKmTrFRe5ONe$nlmD9743dRRjj7v0EBYs1mtqQAMWzXOEa3NWm80Nxpo=','2019-04-22 09:46:43.474385',0,'liyong1','13813881388','','1111111111@qq.com',0,1,'2019-04-22 08:20:26.750566'),(4,'pbkdf2_sha256$120000$2A7YZzHUWY2S$O0PBOWnI3PWpP6Crelh98tAk6r8YfOLpQTjJXq1vlY4=',NULL,0,'liyong2','14514514555','','122112321@qq.com',0,1,'2019-04-22 08:22:03.784655'),(5,'pbkdf2_sha256$120000$2CRiBE7s6Eod$SrnSXC6iyUYsCAQjzn7GFmUd7wIyw2IymE8rIzvbYrA=',NULL,0,'liyong3','15215215222','','2222222222@qq.com',0,1,'2019-04-22 08:37:32.288651');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'polls','choice'),(8,'polls','question'),(6,'sessions','session'),(16,'snippets','algorithm'),(15,'snippets','modela'),(22,'snippets','modelpre'),(9,'snippets','picture'),(11,'snippets','snippet'),(12,'snippets','ss'),(14,'snippets','stock'),(21,'snippets','stockcwdata'),(13,'snippets','stockdata'),(19,'snippets','strategy'),(18,'snippets','strategypre'),(20,'snippets','technicaldata'),(17,'snippets','technicallist'),(10,'snippets','zixun');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2017-06-16 04:13:27.651253'),(2,'auth','0001_initial','2017-06-16 04:13:41.713188'),(3,'admin','0001_initial','2017-06-16 04:13:44.963247'),(4,'admin','0002_logentry_remove_auto_add','2017-06-16 04:13:47.599392'),(5,'contenttypes','0002_remove_content_type_name','2017-06-16 04:13:49.655879'),(6,'auth','0002_alter_permission_name_max_length','2017-06-16 04:13:50.884250'),(7,'auth','0003_alter_user_email_max_length','2017-06-16 04:13:52.539022'),(8,'auth','0004_alter_user_username_opts','2017-06-16 04:13:55.596097'),(9,'auth','0005_alter_user_last_login_null','2017-06-16 04:13:57.208660'),(10,'auth','0006_require_contenttypes_0002','2017-06-16 04:13:58.184922'),(11,'auth','0007_alter_validators_add_error_messages','2017-06-16 04:13:59.174097'),(12,'auth','0008_alter_user_username_max_length','2017-06-16 04:14:00.404352'),(13,'polls','0001_initial','2017-06-16 04:14:04.176210'),(14,'sessions','0001_initial','2017-06-16 04:14:06.179203'),(15,'snippets','0001_initial','2017-06-19 07:35:59.523283'),(16,'snippets','0002_zixun','2017-06-19 07:36:03.992347'),(17,'snippets','0003_zixun_publish_status','2017-06-19 07:36:07.039829'),(18,'snippets','0004_picture','2017-06-19 07:36:15.876862'),(19,'snippets','0005_ss','2017-06-28 07:42:53.371599'),(20,'admin','0003_logentry_add_action_flag_choices','2018-12-19 02:49:36.205103'),(21,'auth','0009_alter_user_last_name_max_length','2018-12-19 02:49:36.957146'),(22,'snippets','0006_auto_20181219_1049','2018-12-19 02:49:37.716190'),(23,'snippets','0006_auto_20181219_1606','2018-12-19 08:07:35.986404'),(24,'snippets','0006_auto_20181219_1716','2018-12-19 09:16:23.479484'),(25,'snippets','0006_auto_20181219_1720','2018-12-19 09:20:33.172765'),(26,'snippets','0007_auto_20181220_1217','2018-12-20 04:17:51.713787'),(27,'snippets','0008_auto_20190103_2236','2019-01-03 14:37:17.742398'),(28,'snippets','0008_auto_20190104_1130','2019-01-04 03:30:38.900902'),(29,'snippets','0009_technicallist','2019-01-04 05:25:51.338271');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('1jzk1gern9mf6cg48ay5o9kipfjax018','MmFiNGM4YWIxOGQwNjNhYjljMmRhYTg1NzgxNDQ3NTc0Y2JmZjAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4YmFjOTA1Yzg1MzA3ZWViMTNiNGQ1YTE1ODE0ODk5ODllOGM1MzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-07-03 18:16:56.449610'),('5ngv0kuwtg0i2vc12iy242tex200octe','M2JmZWM5YjIyYTNjYTI2NmI3N2Q1M2FhMmY3MThiNzVjMWYyYjE1NTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NDFiZjFjZTU4NzZlZjBjZDlhYzhmMTA0YWNmZDMxYmRkNDNkYzdmIn0=','2019-04-07 01:14:00.761241'),('66yq5il31ih26cm6mc6o0sljk6u6flqh','YzgxMjY3MDkxNjMwNjJmZWNmYTg0ZTAwNWI0ZGYzZjIzMmNkZWJlZjp7fQ==','2019-01-02 13:34:21.953802'),('6evpaudrk9m2dczdyldmg9gydxkoagfb','Y2M1YjUzZTIxNDJkOTE1NzAyMzRjMmQ5MjliM2YzODk2MDU4NTQ5Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY0MWJmMWNlNTg3NmVmMGNkOWFjOGYxMDRhY2ZkMzFiZGQ0M2RjN2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2019-04-27 08:00:52.497977'),('fej8pp8i7t0f9dmfb2acr820kedext8o','MTU1MjVjZmVlNzU5NWYwOWFiYjU4OTU4NTE3MzU1MDVmNDczODMwNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY0MWJmMWNlNTg3NmVmMGNkOWFjOGYxMDRhY2ZkMzFiZGQ0M2RjN2YiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-12-28 07:46:56.861642'),('h4c923o4w3w7vhxqrzm3f7hg0259ithw','MTU1MjVjZmVlNzU5NWYwOWFiYjU4OTU4NTE3MzU1MDVmNDczODMwNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY0MWJmMWNlNTg3NmVmMGNkOWFjOGYxMDRhY2ZkMzFiZGQ0M2RjN2YiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2019-05-30 14:21:21.220930'),('jdmzg0r6cdanqo4l0pts4tl3kyzhv0k8','MmFiNGM4YWIxOGQwNjNhYjljMmRhYTg1NzgxNDQ3NTc0Y2JmZjAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4YmFjOTA1Yzg1MzA3ZWViMTNiNGQ1YTE1ODE0ODk5ODllOGM1MzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-07-27 06:28:48.261500'),('jg9balhyj02fuy0s542mqtmgiot8k8o6','MmFiNGM4YWIxOGQwNjNhYjljMmRhYTg1NzgxNDQ3NTc0Y2JmZjAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4YmFjOTA1Yzg1MzA3ZWViMTNiNGQ1YTE1ODE0ODk5ODllOGM1MzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-07-22 05:59:37.431350'),('k6xlaa4m5l5np66ds73igdmzft8knm1n','NGRkNmY2NTc2OTY3NjI2NmYwOTNlOTc4OTlkNGQ0ZmY1ODU1NGU1Mjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjQxYmYxY2U1ODc2ZWYwY2Q5YWM4ZjEwNGFjZmQzMWJkZDQzZGM3ZiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2019-02-09 14:18:04.217568'),('kdmf6v2t3d96jrs4u2wjkqd1zn91breu','MmFiNGM4YWIxOGQwNjNhYjljMmRhYTg1NzgxNDQ3NTc0Y2JmZjAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4YmFjOTA1Yzg1MzA3ZWViMTNiNGQ1YTE1ODE0ODk5ODllOGM1MzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-07-12 07:45:02.407541'),('knwippbssftqlbylf6iia2121lec3378','MmFiNGM4YWIxOGQwNjNhYjljMmRhYTg1NzgxNDQ3NTc0Y2JmZjAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4YmFjOTA1Yzg1MzA3ZWViMTNiNGQ1YTE1ODE0ODk5ODllOGM1MzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-07-13 02:26:00.149610'),('pr2yynk62q5xahepa4oyc41vk11miqjq','Zjg3OTUwYmE1MDg0MDAxNTA1ODM1ZjQwNWM1MzE3OWVhOWQ1MDExMjp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2Y4NmFiYjUyYjY5ZTZhYTQyYzI4M2Y4N2EyODlhMDM2YTFkMThhZSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2019-05-06 09:46:43.524385'),('pwz3wed9l0maf3z3ngjyboaxahnv3unw','MmFiNGM4YWIxOGQwNjNhYjljMmRhYTg1NzgxNDQ3NTc0Y2JmZjAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4YmFjOTA1Yzg1MzA3ZWViMTNiNGQ1YTE1ODE0ODk5ODllOGM1MzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-07-12 08:18:17.800032'),('tgjhqn2pmc0e19aeods1avfjh6xnisum','MmFiNGM4YWIxOGQwNjNhYjljMmRhYTg1NzgxNDQ3NTc0Y2JmZjAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4YmFjOTA1Yzg1MzA3ZWViMTNiNGQ1YTE1ODE0ODk5ODllOGM1MzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-07-12 07:11:59.749030'),('uvwg9a4iaorxbwdfxnm55s3iojjd848x','YzgxMjY3MDkxNjMwNjJmZWNmYTg0ZTAwNWI0ZGYzZjIzMmNkZWJlZjp7fQ==','2019-01-02 13:35:47.063670');

/*Table structure for table `polls_choice` */

DROP TABLE IF EXISTS `polls_choice`;

CREATE TABLE `polls_choice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `choice_text` varchar(200) NOT NULL,
  `votes` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_choice_question_id_c5b4b260_fk_polls_question_id` (`question_id`),
  CONSTRAINT `polls_choice_question_id_c5b4b260_fk_polls_question_id` FOREIGN KEY (`question_id`) REFERENCES `polls_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `polls_choice` */

/*Table structure for table `polls_question` */

DROP TABLE IF EXISTS `polls_question`;

CREATE TABLE `polls_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_text` varchar(200) NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `polls_question` */

/*Table structure for table `snippets_algorithm` */

DROP TABLE IF EXISTS `snippets_algorithm`;

CREATE TABLE `snippets_algorithm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `name` varchar(100) NOT NULL,
  `a1` varchar(100) NOT NULL,
  `a2` varchar(100) NOT NULL,
  `a3` varchar(100) NOT NULL,
  `a4` varchar(100) NOT NULL,
  `a5` varchar(100) NOT NULL,
  `a6` varchar(100) NOT NULL,
  `a7` varchar(100) NOT NULL,
  `a8` varchar(100) NOT NULL,
  `a9` varchar(100) NOT NULL,
  `a10` varchar(100) NOT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

/*Data for the table `snippets_algorithm` */

insert  into `snippets_algorithm`(`id`,`created`,`name`,`a1`,`a2`,`a3`,`a4`,`a5`,`a6`,`a7`,`a8`,`a9`,`a10`,`isExpired`,`note`) values (3,'2018-12-21 06:46:49.586801','线性回归','序列参数','','','','','','','','','LR',0,''),(6,'2018-12-21 06:48:16.646780','决策树算法','序列参数','特征选择标准','决策树最大深度','','','','','','','DTR',0,''),(7,'2018-12-21 06:48:40.182127','随机森林算法','序列参数','决策树个数','建立子树个数','','','','','','','RFR',0,''),(8,'2018-12-21 06:48:56.973087','AdaBoost算法','序列参数','Adaboost回归算法','','','','','','','','AdaBoost',0,''),(9,'2018-12-21 06:49:35.469289','GBRT算法','序列参数','弱分类器的个数','','','','','','','','GBRT',0,''),(11,'2019-04-14 03:49:30.788150','LSTM深度神经网络','序列参数','隐藏层数','隐藏层节点个数','','','','','','','LSTM',0,'');

/*Table structure for table `snippets_modela` */

DROP TABLE IF EXISTS `snippets_modela`;

CREATE TABLE `snippets_modela` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `name` varchar(100) NOT NULL,
  `m1` varchar(100) NOT NULL,
  `m2` varchar(100) NOT NULL,
  `m3` varchar(100) NOT NULL,
  `m4` varchar(100) NOT NULL,
  `m5` varchar(100) NOT NULL,
  `m6` varchar(100) NOT NULL,
  `m7` varchar(100) NOT NULL,
  `m8` varchar(100) NOT NULL,
  `m9` varchar(100) NOT NULL,
  `m10` varchar(100) NOT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  `modelPath` varchar(250) NOT NULL,
  `result` varchar(100) NOT NULL,
  `r1` varchar(3000) NOT NULL,
  `r2` varchar(3000) NOT NULL,
  `r3` varchar(3000) NOT NULL,
  `r4` varchar(3000) NOT NULL,
  `r5` varchar(3000) NOT NULL,
  `algorithm_id` int(11) NOT NULL,
  `stockData_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `snippets_modela_algorithm_id_09c8c146_fk_snippets_algorithm_id` (`algorithm_id`),
  KEY `snippets_modela_stockData_id_9f994ffc_fk_snippets_stockdata_id` (`stockData_id`),
  CONSTRAINT `snippets_modela_algorithm_id_09c8c146_fk_snippets_algorithm_id` FOREIGN KEY (`algorithm_id`) REFERENCES `snippets_algorithm` (`id`),
  CONSTRAINT `snippets_modela_stockData_id_9f994ffc_fk_snippets_stockdata_id` FOREIGN KEY (`stockData_id`) REFERENCES `snippets_stockdata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

/*Data for the table `snippets_modela` */

insert  into `snippets_modela`(`id`,`created`,`name`,`m1`,`m2`,`m3`,`m4`,`m5`,`m6`,`m7`,`m8`,`m9`,`m10`,`isExpired`,`note`,`modelPath`,`result`,`r1`,`r2`,`r3`,`r4`,`r5`,`algorithm_id`,`stockData_id`) values (9,'2018-12-23 09:54:00.658776','Number1','10','','','','','','','','','创建',0,'','./dataSet/model/Number1_train_model.m','0.8491','[\"6.36\", \"5.51\", \"6.92\", \"7.78\", \"8.3\", \"6.13\", \"6.3\", \"5.86\", \"7.09\", \"14.05\", \"6.79\", \"5.64\", \"5.96\", \"7.11\", \"7.68\", \"15.8\", \"16.18\", \"5.61\", \"18.19\", \"11.41\", \"8.79\", \"7.07\", \"6.94\", \"7.41\", \"7.61\", \"6.87\"]','[\"6.01\", \"5.8\", \"6.96\", \"7.54\", \"7.95\", \"6.36\", \"6.0\", \"5.75\", \"6.96\", \"14.11\", \"6.21\", \"5.66\", \"5.96\", \"7.08\", \"8.18\", \"17.21\", \"16.23\", \"5.77\", \"15.88\", \"13.16\", \"7.86\", \"7.23\", \"7.15\", \"7.39\", \"7.31\", \"7.58\"]','','','',3,7),(11,'2018-12-23 14:08:16.126339','Number2','10','','','','','','','','','创建',0,'','./dataSet/model/Number2_train_model.m','0.8554','[\"5.96\", \"5.78\", \"6.92\", \"7.66\", \"8.3\", \"7.96\", \"9.11\", \"6.13\", \"7.26\", \"6.02\", \"7.06\", \"6.67\", \"7.44\", \"7.88\", \"7.98\", \"7.17\", \"15.67\", \"7.11\", \"7.41\", \"7.78\", \"8.07\", \"7.05\", \"6.3\", \"6.2\", \"7.75\", \"12.68\"]','[\"5.99\", \"5.82\", \"6.82\", \"7.59\", \"7.64\", \"7.2\", \"7.71\", \"6.52\", \"6.95\", \"5.79\", \"7.13\", \"6.86\", \"7.32\", \"7.61\", \"7.78\", \"7.22\", \"15.9\", \"7.03\", \"7.27\", \"7.72\", \"7.71\", \"7.1\", \"5.86\", \"6.29\", \"7.63\", \"15.24\"]','0.8462','0.9615','1.0',3,7),(12,'2019-01-10 13:31:35.751478','600000Number1','10','','','','','','','','','创建',0,'','./dataSet/model/600000Number1_train_model.m','0.8589','[\"9.8\", \"10.03\", \"16.01\", \"10.14\", \"13.08\", \"12.39\", \"16.71\", \"11.72\", \"12.68\", \"12.9\", \"16.26\", \"12.83\", \"16.57\", \"15.96\", \"10.57\", \"12.64\", \"9.79\", \"11.76\", \"16.67\", \"9.91\", \"12.41\", \"16.47\", \"10.76\", \"12.73\", \"13.1\", \"16.22\", \"17.16\", \"12.29\", \"9.66\", \"16.49\", \"15.97\", \"16.18\", \"16.85\", \"16.43\", \"12.89\", \"16.0\", \"16.48\", \"12.78\", \"14.86\", \"10.92\", \"12.78\", \"12.64\", \"10.05\", \"10.41\", \"17.34\", \"10.82\", \"12.62\", \"15.27\", \"16.6\", \"10.37\", \"9.75\", \"16.35\", \"15.16\", \"10.03\", \"12.93\", \"12.77\", \"9.6\", \"11.57\", \"12.85\", \"12.91\", \"11.08\", \"10.41\", \"10.78\", \"13.38\", \"12.6\", \"9.38\", \"10.17\", \"12.78\", \"10.66\", \"9.44\", \"10.11\", \"10.5\", \"12.72\", \"13.69\", \"13.66\", \"12.61\", \"12.91\", \"12.6\", \"12.3\", \"13.62\", \"10.54\", \"16.07\", \"16.3\", \"16.32\", \"13.14\", \"12.84\", \"10.0\", \"10.33\", \"12.54\", \"16.34\", \"10.92\", \"12.68\", \"13.17\", \"12.85\", \"12.49\", \"16.42\", \"12.86\", \"16.36\", \"9.56\", \"12.75\", \"17.3\", \"12.87\", \"10.14\", \"10.95\", \"11.05\", \"9.28\", \"11.92\", \"12.67\", \"15.01\", \"12.76\", \"15.69\", \"16.2\", \"11.0\", \"10.22\", \"10.45\", \"13.02\", \"10.29\", \"15.78\", \"12.88\", \"12.99\"]','[\"10.16\", \"10.7\", \"16.27\", \"9.97\", \"13.45\", \"12.84\", \"16.51\", \"11.51\", \"12.64\", \"12.93\", \"16.15\", \"12.85\", \"16.31\", \"16.25\", \"10.67\", \"12.76\", \"10.36\", \"11.63\", \"16.41\", \"9.64\", \"12.67\", \"16.51\", \"11.17\", \"12.88\", \"12.78\", \"16.37\", \"16.69\", \"12.84\", \"10.54\", \"16.44\", \"15.81\", \"16.21\", \"16.24\", \"16.53\", \"13.99\", \"16.49\", \"16.36\", \"12.36\", \"14.54\", \"10.19\", \"12.76\", \"12.92\", \"10.22\", \"10.38\", \"16.51\", \"11.56\", \"12.29\", \"15.2\", \"16.14\", \"10.16\", \"10.32\", \"16.08\", \"15.77\", \"9.89\", \"13.21\", \"12.36\", \"9.81\", \"12.29\", \"12.29\", \"12.84\", \"10.49\", \"10.36\", \"11.02\", \"12.79\", \"12.76\", \"9.67\", \"10.25\", \"13.34\", \"10.62\", \"9.67\", \"10.39\", \"10.7\", \"12.75\", \"12.98\", \"12.83\", \"12.84\", \"12.51\", \"12.84\", \"12.38\", \"12.89\", \"10.57\", \"16.55\", \"16.48\", \"16.49\", \"12.64\", \"13.74\", \"9.78\", \"10.19\", \"12.88\", \"15.73\", \"11.36\", \"12.81\", \"12.82\", \"14.02\", \"12.58\", \"16.1\", \"12.83\", \"16.7\", \"10.41\", \"12.86\", \"16.53\", \"12.81\", \"9.8\", \"11.4\", \"11.31\", \"10.18\", \"11.73\", \"12.76\", \"14.92\", \"12.29\", \"14.97\", \"16.32\", \"11.33\", \"10.09\", \"10.13\", \"12.87\", \"10.33\", \"15.79\", \"12.84\", \"12.79\"]','0.9667','0.9917','1.0',9,8),(22,'2019-04-14 03:49:30.788150','600000Number2','10','','','','','','','','','上传',0,'','./dataSet/model/600000Number2_train_model.m','0.9074','[\"9.8\", \"10.03\", \"16.01\", \"10.14\", \"13.08\", \"12.39\", \"16.71\", \"11.72\", \"12.68\", \"12.9\", \"16.26\", \"12.83\", \"16.57\", \"15.96\", \"10.57\", \"12.64\", \"9.79\", \"11.76\", \"16.67\", \"9.91\", \"12.41\", \"16.47\", \"10.76\", \"12.73\", \"13.1\", \"16.22\", \"17.16\", \"12.29\", \"9.66\", \"16.49\", \"15.97\", \"16.18\", \"16.85\", \"16.43\", \"12.89\", \"16.0\", \"16.48\", \"12.78\", \"14.86\", \"10.92\", \"12.78\", \"12.64\", \"10.05\", \"10.41\", \"17.34\", \"10.82\", \"12.62\", \"15.27\", \"16.6\", \"10.37\", \"9.75\", \"16.35\", \"15.16\", \"10.03\", \"12.93\", \"12.77\", \"9.6\", \"11.57\", \"12.85\", \"12.91\", \"11.08\", \"10.41\", \"10.78\", \"13.38\", \"12.6\", \"9.38\", \"10.17\", \"12.78\", \"10.66\", \"9.44\", \"10.11\", \"10.5\", \"12.72\", \"13.69\", \"13.66\", \"12.61\", \"12.91\", \"12.6\", \"12.3\", \"13.62\", \"10.54\", \"16.07\", \"16.3\", \"16.32\", \"13.14\", \"12.84\", \"10.0\", \"10.33\", \"12.54\", \"16.34\", \"10.92\", \"12.68\", \"13.17\", \"12.85\", \"12.49\", \"16.42\", \"12.86\", \"16.36\", \"9.56\", \"12.75\", \"17.3\", \"12.87\", \"10.14\", \"10.95\", \"11.05\", \"9.28\", \"11.92\", \"12.67\", \"15.01\", \"12.76\", \"15.69\", \"16.2\", \"11.0\", \"10.22\", \"10.45\", \"13.02\", \"10.29\", \"15.78\", \"12.88\", \"12.99\"]','[\"10.16\", \"10.7\", \"16.27\", \"9.97\", \"13.45\", \"12.84\", \"16.51\", \"11.51\", \"12.64\", \"12.93\", \"16.15\", \"12.85\", \"16.31\", \"16.25\", \"10.67\", \"12.76\", \"10.36\", \"11.63\", \"16.41\", \"9.64\", \"12.67\", \"16.51\", \"11.17\", \"12.88\", \"12.78\", \"16.37\", \"16.69\", \"12.84\", \"10.54\", \"16.44\", \"15.81\", \"16.21\", \"16.24\", \"16.53\", \"13.99\", \"16.49\", \"16.36\", \"12.36\", \"14.54\", \"10.19\", \"12.76\", \"12.92\", \"10.22\", \"10.38\", \"16.51\", \"11.56\", \"12.29\", \"15.2\", \"16.14\", \"10.16\", \"10.32\", \"16.08\", \"15.77\", \"9.89\", \"13.21\", \"12.36\", \"9.81\", \"12.29\", \"12.29\", \"12.84\", \"10.49\", \"10.36\", \"11.02\", \"12.79\", \"12.76\", \"9.67\", \"10.25\", \"13.34\", \"10.62\", \"9.67\", \"10.39\", \"10.7\", \"12.75\", \"12.98\", \"12.83\", \"12.84\", \"12.51\", \"12.84\", \"12.38\", \"12.89\", \"10.57\", \"16.55\", \"16.48\", \"16.49\", \"12.64\", \"13.74\", \"9.78\", \"10.19\", \"12.88\", \"15.73\", \"11.36\", \"12.81\", \"12.82\", \"14.02\", \"12.58\", \"16.1\", \"12.83\", \"16.7\", \"10.41\", \"12.86\", \"16.53\", \"12.81\", \"9.8\", \"11.4\", \"11.31\", \"10.18\", \"11.73\", \"12.76\", \"14.92\", \"12.29\", \"14.97\", \"16.32\", \"11.33\", \"10.09\", \"10.13\", \"12.87\", \"10.33\", \"15.79\", \"12.84\", \"12.79\"]','','','',11,8),(23,'2019-04-14 03:57:00.445869','600000Number3','10','','','','','','','','','上传',0,'','./dataSet/model/LSTM_train_model.m','0.90451','','','','','',11,8);

/*Table structure for table `snippets_modelpre` */

DROP TABLE IF EXISTS `snippets_modelpre`;

CREATE TABLE `snippets_modelpre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `code` varchar(100) NOT NULL,
  `m1` varchar(100) NOT NULL,
  `m2` varchar(100) NOT NULL,
  `m3` varchar(100) NOT NULL,
  `m4` varchar(100) NOT NULL,
  `m5` varchar(100) NOT NULL,
  `result` varchar(100) NOT NULL,
  `dataStr` longtext NOT NULL,
  `result1` varchar(100) NOT NULL,
  `result2` varchar(100) NOT NULL,
  `result3` varchar(100) NOT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  `KY1` varchar(100) NOT NULL,
  `KY2` varchar(100) NOT NULL,
  `KY3` varchar(100) NOT NULL,
  `modelA_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `snippets_modelpre_modelA_id_4235a186_fk_snippets_modela_id` (`modelA_id`),
  CONSTRAINT `snippets_modelpre_modelA_id_4235a186_fk_snippets_modela_id` FOREIGN KEY (`modelA_id`) REFERENCES `snippets_modela` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `snippets_modelpre` */

/*Table structure for table `snippets_picture` */

DROP TABLE IF EXISTS `snippets_picture`;

CREATE TABLE `snippets_picture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `title` varchar(100) NOT NULL,
  `category` longtext NOT NULL,
  `isComment` tinyint(1) NOT NULL,
  `publish_time` longtext NOT NULL,
  `content` longtext NOT NULL,
  `picture_list` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `snippets_picture` */

/*Table structure for table `snippets_snippet` */

DROP TABLE IF EXISTS `snippets_snippet`;

CREATE TABLE `snippets_snippet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `title` varchar(100) NOT NULL,
  `code` longtext NOT NULL,
  `linenos` tinyint(1) NOT NULL,
  `language` varchar(100) NOT NULL,
  `style` varchar(100) NOT NULL,
  `highlighted` longtext NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `snippets_snippet_owner_id_20604299_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `snippets_snippet_owner_id_20604299_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `snippets_snippet` */

/*Table structure for table `snippets_ss` */

DROP TABLE IF EXISTS `snippets_ss`;

CREATE TABLE `snippets_ss` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `name` varchar(100) NOT NULL,
  `qq` longtext NOT NULL,
  `wechat` longtext NOT NULL,
  `alipay` longtext NOT NULL,
  `buy_time` longtext NOT NULL,
  `end_time` longtext NOT NULL,
  `ss_ip` longtext NOT NULL,
  `ss_port` longtext NOT NULL,
  `ss_passwd` longtext NOT NULL,
  `ss_encry` longtext NOT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `snippets_ss` */

insert  into `snippets_ss`(`id`,`created`,`name`,`qq`,`wechat`,`alipay`,`buy_time`,`end_time`,`ss_ip`,`ss_port`,`ss_passwd`,`ss_encry`,`isExpired`,`note`) values (1,'2017-06-28 07:57:02.211866','wangbi','476301176','','','2017-03-20-21-30','2018-03-20-21-30','23.105.219.180','8387','476301176hh2','aes-256-cfb',0,'');

/*Table structure for table `snippets_stock` */

DROP TABLE IF EXISTS `snippets_stock`;

CREATE TABLE `snippets_stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `industry` varchar(100) NOT NULL,
  `area` varchar(100) NOT NULL,
  `timeToMarket` longtext NOT NULL,
  `pe` decimal(25,3) DEFAULT NULL,
  `outstanding` decimal(25,3) DEFAULT NULL,
  `totals` decimal(25,3) DEFAULT NULL,
  `totalsAssets` decimal(25,3) DEFAULT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  `highlighted` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

/*Data for the table `snippets_stock` */

insert  into `snippets_stock`(`id`,`created`,`code`,`name`,`industry`,`area`,`timeToMarket`,`pe`,`outstanding`,`totals`,`totalsAssets`,`isExpired`,`note`,`highlighted`) values (3,'2018-12-19 09:32:42.704492','300165','天瑞仪器','电器仪表','江苏','20110125','33.920','3.150','4.620','218298.950',0,'',''),(6,'2018-12-19 09:36:18.833854','002721','金一文化','服饰','北京','20140127','370.360','5.450','8.350','1875443.250',0,'',''),(9,'2018-12-21 07:59:02.123608','000400','许继电气','电气设备','河南','19970418','44.430','10.080','10.080','1464956.000',0,'',''),(10,'2019-01-04 06:23:25.204820','600000','浦发银行','银行','上海','19991110','5.000','281.040','293.520','608918912.000',0,'',''),(11,'2019-01-09 12:24:43.897215','600004','白云机场','机场','广东','20030428','16.710','20.690','20.690','2793101.500',0,'',''),(12,'2019-01-09 12:25:19.324242','600009','上海机场','机场','上海','19980218','23.330','10.930','19.270','2987108.000',0,'',''),(16,'2019-01-09 12:30:26.296800','600015','华夏银行','银行','北京','20030912','4.940','128.230','128.230','261299104.000',0,'',''),(17,'2019-01-09 12:30:41.561673','600016','民生银行','银行','北京','20001219','4.430','354.620','437.820','596582720.000',0,'',''),(20,'2019-04-13 12:33:54.095951','600018','上港集团','港口','上海','20061026','18.850','231.740','231.740','14436702.000',0,'',''),(21,'2019-04-13 12:34:21.497518','600020','中原高速','路桥','河南','20030808','9.690','22.470','22.470','4889324.000',0,'',''),(22,'2019-04-13 12:36:18.865231','600021','上海电力','火力发电','上海','20031029','26.400','8.560','26.170','8834188.000',0,'','');

/*Table structure for table `snippets_stockcwdata` */

DROP TABLE IF EXISTS `snippets_stockcwdata`;

CREATE TABLE `snippets_stockcwdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `name` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL,
  `quarter` varchar(100) NOT NULL,
  `number` int(11) DEFAULT NULL,
  `dimension` int(11) DEFAULT NULL,
  `filePath` varchar(250) NOT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  `startDate` longtext NOT NULL,
  `endDate` longtext NOT NULL,
  `KY1` varchar(100) NOT NULL,
  `KY2` varchar(100) NOT NULL,
  `KY3` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

/*Data for the table `snippets_stockcwdata` */

insert  into `snippets_stockcwdata`(`id`,`created`,`name`,`year`,`quarter`,`number`,`dimension`,`filePath`,`isExpired`,`note`,`startDate`,`endDate`,`KY1`,`KY2`,`KY3`) values (4,'2019-01-04 04:21:59.554105','2018年第一季度财务数据','2018','1',107,32,'./dataSet/financial/2018年第一季度财务数据.csv',0,'','2018-04-01','2018-06-30','','',''),(5,'2019-01-15 11:21:19.583380','2017年第四季度财务数据','2017','4',244,32,'./dataSet/financial/2017年第四季度财务数据.csv',0,'','2018-01-01','2018-03-31','','',''),(6,'2019-04-14 01:22:52.065892','2017年第三季度财务数据','2017','3',118,32,'./dataSet/financial/2017年第三季度财务数据.csv',0,'','2017-10-02','2017-12-30','','',''),(7,'2019-04-14 01:22:52.065892','2017年第二季度财务数据','2017','2',146,32,'./dataSet/financial/2017年第二季度财务数据.csv',0,'','2017-07-03','2017-09-29','','','');

/*Table structure for table `snippets_stockdata` */

DROP TABLE IF EXISTS `snippets_stockdata`;

CREATE TABLE `snippets_stockdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `buy_time` longtext NOT NULL,
  `end_time` longtext NOT NULL,
  `number` int(11) DEFAULT NULL,
  `filePath` varchar(250) DEFAULT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  `stock_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `snippets_stockdata_stock_id_4daddf97_fk_snippets_stock_id` (`stock_id`),
  CONSTRAINT `snippets_stockdata_stock_id_4daddf97_fk_snippets_stock_id` FOREIGN KEY (`stock_id`) REFERENCES `snippets_stock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Data for the table `snippets_stockdata` */

insert  into `snippets_stockdata`(`id`,`created`,`buy_time`,`end_time`,`number`,`filePath`,`isExpired`,`note`,`stock_id`) values (7,'2018-12-20 03:17:22.211191','2018-01-01','2019-05-16',239,'./dataSet/history/002721.csv',0,'',6),(8,'2019-01-04 06:24:02.694965','2016-07-01','2019-05-16',630,'./dataSet/history/600000.csv',0,'',10),(10,'2019-01-09 12:27:42.285419','2016-07-01','2019-05-16',693,'./dataSet/history/600009.csv',0,'',12),(11,'2019-01-09 12:28:54.329539','2016-07-01','2019-05-16',693,'./dataSet/history/600004.csv',0,'',11),(13,'2019-01-09 12:43:59.034286','2016-07-01','2019-01-01',605,'./dataSet/history/600016.csv',0,'',17);

/*Table structure for table `snippets_strategy` */

DROP TABLE IF EXISTS `snippets_strategy`;

CREATE TABLE `snippets_strategy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `name` varchar(100) NOT NULL,
  `algorithm` varchar(100) NOT NULL,
  `modelPath` varchar(250) NOT NULL,
  `evaResult` varchar(100) NOT NULL,
  `dataNote` longtext NOT NULL,
  `inputNote` longtext NOT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  `KY1` varchar(100) NOT NULL,
  `KY2` varchar(100) NOT NULL,
  `KY3` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `snippets_strategy` */

insert  into `snippets_strategy`(`id`,`created`,`name`,`algorithm`,`modelPath`,`evaResult`,`dataNote`,`inputNote`,`isExpired`,`note`,`KY1`,`KY2`,`KY3`) values (1,'2019-01-10 13:29:24.332961','基于BP神经网络的选股策略_2017','BP神经网络','./dataSet/strategy/CW2017Frist_BP_train_model.m','0.86','训练数据集使用了2017年沪深300股票的所有可用财务数据','输入的财务数据需要进行零均值单位方差处理',0,'','4','',''),(2,'2019-01-30 22:43:40.000000','基于BP神经网络的选股模型_2018','BP神经网络','./dataSet/strategy/CW2018Frist_BP_train_model.m','0.79','','',0,'','2','',''),(3,'2019-03-22 15:14:47.394160','600000Number3','BP神经网络','./dataSet/model/600000Number3_train_model.m','0.73','','',0,'','','',''),(4,'2019-03-22 15:17:12.046434','600000Number3','BP神经网络','./dataSet/model/600000Number3_train_model.m','0.64','','',0,'','','','');

/*Table structure for table `snippets_strategypre` */

DROP TABLE IF EXISTS `snippets_strategypre`;

CREATE TABLE `snippets_strategypre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `code` varchar(100) NOT NULL,
  `result` varchar(100) NOT NULL,
  `result1` varchar(100) NOT NULL,
  `result2` varchar(100) NOT NULL,
  `result3` varchar(100) NOT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  `KY1` varchar(100) NOT NULL,
  `KY2` varchar(100) NOT NULL,
  `KY3` varchar(100) NOT NULL,
  `strategy_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `snippets_strategypre_strategy_id_f045cc20_fk_snippets_` (`strategy_id`),
  CONSTRAINT `snippets_strategypre_strategy_id_f045cc20_fk_snippets_` FOREIGN KEY (`strategy_id`) REFERENCES `snippets_strategy` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `snippets_strategypre` */

/*Table structure for table `snippets_technicaldata` */

DROP TABLE IF EXISTS `snippets_technicaldata`;

CREATE TABLE `snippets_technicaldata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `technicalDatas` longtext NOT NULL,
  `dimension` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `filePath` varchar(250) NOT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  `KY1` varchar(100) NOT NULL,
  `KY2` varchar(100) NOT NULL,
  `KY3` varchar(100) NOT NULL,
  `stockData_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `snippets_technicalda_stockData_id_89c3040a_fk_snippets_` (`stockData_id`),
  CONSTRAINT `snippets_technicalda_stockData_id_89c3040a_fk_snippets_` FOREIGN KEY (`stockData_id`) REFERENCES `snippets_stockdata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `snippets_technicaldata` */

insert  into `snippets_technicaldata`(`id`,`created`,`technicalDatas`,`dimension`,`number`,`filePath`,`isExpired`,`note`,`KY1`,`KY2`,`KY3`,`stockData_id`) values (1,'2019-01-09 12:11:37.267223','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,',41,609,'./dataSet/technical/600000-浦发银行1.csv',0,'','浦发银行1','','',8),(2,'2019-01-09 12:16:49.621088','1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,',41,131,'./dataSet/technical/002721-金一文化1.csv',0,'','金一文化1','','',7);

/*Table structure for table `snippets_technicallist` */

DROP TABLE IF EXISTS `snippets_technicallist`;

CREATE TABLE `snippets_technicallist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `name` varchar(100) NOT NULL,
  `nickname` varchar(100) NOT NULL,
  `tType` varchar(100) NOT NULL,
  `interface` varchar(100) NOT NULL,
  `parameter1` varchar(100) NOT NULL,
  `parameter2` varchar(100) NOT NULL,
  `parameter3` varchar(100) NOT NULL,
  `parameter4` varchar(100) NOT NULL,
  `parameter5` varchar(100) NOT NULL,
  `isExpired` tinyint(1) NOT NULL,
  `note` longtext NOT NULL,
  `KY1` varchar(100) NOT NULL,
  `KY2` varchar(100) NOT NULL,
  `KY3` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

/*Data for the table `snippets_technicallist` */

insert  into `snippets_technicallist`(`id`,`created`,`name`,`nickname`,`tType`,`interface`,`parameter1`,`parameter2`,`parameter3`,`parameter4`,`parameter5`,`isExpired`,`note`,`KY1`,`KY2`,`KY3`) values (1,'2019-01-04 06:08:18.582965','MA5-均线','MA5','均线型','MA5','收盘价序列','统计的天数','','','',0,'','','',''),(2,'2019-01-08 03:02:00.479830','EMA10-指数移动平均值','EMA10','趋势型','EMA10','收盘价序列','移动周期','','','',0,'','','',''),(3,'2019-01-09 09:24:38.801199','MA10-均线','MA10','均线型','MA10','收盘价序列','统计的天数','','','',0,'','','',''),(4,'2019-01-09 09:25:34.954411','MA20-均线','MA20','均线型','MA20','收盘价序列','统计的天数','','','',0,'','','',''),(5,'2019-01-09 09:26:40.238145','MA30-均线','MA30','均线型','MA30','收盘价序列','统计的天数','','','',0,'','','',''),(6,'2019-01-09 09:27:29.395957','MA60-均线','MA60','均线型','MA60','收盘价序列','统计的天数','','','',0,'','','',''),(7,'2019-01-09 09:30:55.817763','ARBR情绪指标','ARBR','能量型','ARBR','开盘价序列','最高价序列','最低价序列','','',0,'','','',''),(8,'2019-01-09 09:38:42.331447','BIAS0-乘离率','BIAS0','超买超卖型','BIAS0','收盘价序列','移动周期','移动平均类型','','',0,'','','',''),(9,'2019-01-09 09:39:32.587321','BIAS0-乘离率','BIAS1','超买超卖型','BIAS1','收盘价序列','移动周期','移动平均类型','','',0,'','','',''),(10,'2019-01-09 09:41:15.792224','BOLL-布林线指标','BOLL0','路径型','BOLL0','收盘价序列','移动平均类型','','','',0,'','','',''),(11,'2019-01-09 09:42:56.016956','BOLL-布林线指标','BOLL1','路径型','BOLL1','收盘价序列','移动平均类型','','','',0,'','','',''),(12,'2019-01-09 09:45:00.040050','DMA-平行线差指标','DMA','趋势型','DMA','收盘价序列','','','','',0,'','','',''),(13,'2019-01-09 09:46:04.409732','DPO-区间震荡线','DPO','趋势型','DPO','收盘价序列','','','','',0,'','','',''),(14,'2019-01-09 09:55:15.481251','EMA20-指数移动平均值','EMA20','趋势型','EMA20','收盘价序列','移动周期','','','',0,'','','',''),(15,'2019-01-09 09:56:49.987657','EMA30-指数移动平均值','EMA30','趋势型','EMA30','收盘价序列','移动周期','','','',0,'','','',''),(16,'2019-01-09 09:59:34.752081','KDJ-随机指标','KDJ','超买超卖型','KDJ','最高价序列','最低价序列','收盘价序列','','',0,'','','',''),(17,'2019-01-09 10:00:50.427409','PSY-心理线指标','PSY','能量型','PSY','收盘价序列','','','','',0,'','','',''),(18,'2019-01-09 10:03:00.080825','WVAD-威廉变异离散量','WVAD','趋势型','WVAD','开盘价序列','最高价序列','最低价序列','','',0,'','','',''),(19,'2019-01-09 10:04:11.984938','MIKE-麦克支撑压力线','MIKE','路径型','MIKE','最高价序列','最低价序列','收盘价序列','','',0,'','','','');

/*Table structure for table `snippets_zixun` */

DROP TABLE IF EXISTS `snippets_zixun`;

CREATE TABLE `snippets_zixun` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `title` varchar(100) NOT NULL,
  `category` longtext NOT NULL,
  `source` longtext NOT NULL,
  `update_time` longtext NOT NULL,
  `see_times` longtext NOT NULL,
  `publish_status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `snippets_zixun` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
