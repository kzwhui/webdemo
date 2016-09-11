create database `d_web_demo`;

USE `d_web_demo`;

CREATE TABLE `t_image_url`(
  `c_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `c_url` varchar(128) NOT NULL,
  `c_description` varchar(256) NOT NULL,
  `c_modify_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `c_create_time` datetime NOT NULL,
  PRIMARY KEY (`c_id`),
  UNIQUE KEY `url` (`c_url`),
  KEY `modify_time` (`c_modify_time`),
  KEY `create_time` (`c_create_time`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
