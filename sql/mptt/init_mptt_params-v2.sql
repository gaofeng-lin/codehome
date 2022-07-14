SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS `mptt_param_v2`;
CREATE TABLE `mptt_param_v2`  (
  `node_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `node_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `lft` bigint(20) NOT NULL,
  `rgt` bigint(20) NOT NULL,
  `node_level` bigint(20) NOT NULL,
  PRIMARY KEY (`node_id`) USING BTREE,
  KEY `node_name` (`node_name`,`lft`,`rgt`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

insert into mptt_param (node_name, lft, rgt, node_level) values ('root', 1,2,1);