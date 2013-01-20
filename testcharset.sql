DROP TABLE IF EXISTS `charset_test`;

CREATE TABLE `charset_test` (
  `data` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) DEFAULT CHARSET=utf8 ;

#
# Data contents of table `wp_ctsop_plugin`
#
 
INSERT INTO `charset_test` VALUES ('“Thank you, thank you.” ') ; 
