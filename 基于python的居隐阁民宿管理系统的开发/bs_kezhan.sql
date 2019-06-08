/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50527
Source Host           : localhost:3306
Source Database       : bs_kezhan

Target Server Type    : MYSQL
Target Server Version : 50527
File Encoding         : 65001

Date: 2019-04-18 18:50:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for gonggao
-- ----------------------------
DROP TABLE IF EXISTS `gonggao`;
CREATE TABLE `gonggao` (
  `msg` varchar(1000) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of gonggao
-- ----------------------------
INSERT INTO `gonggao` VALUES ('指利用当地闲置资源，民宿主人参与接待，为游客提供体验当地自然、文化与生产生活方式的小型住宿设施。', '关于民宿科普', '125cb6ce-5459-11e9-8a4b-085700f5cdd2');
INSERT INTO `gonggao` VALUES ('民宿 不同于传统的饭店旅馆，也许没有高级奢华的设施，但它能让人体验当地风情、感受民宿主人的热情与服务、并体验有别于以往的生活。', '关于民宿的来源', 'bc6e1a68-545e-11e9-8a4b-085700f5cdd2');

-- ----------------------------
-- Table structure for home
-- ----------------------------
DROP TABLE IF EXISTS `home`;
CREATE TABLE `home` (
  `money` varchar(30) DEFAULT NULL COMMENT '房间价钱',
  `nenber` varchar(255) DEFAULT NULL COMMENT '房间号',
  `body` varchar(255) DEFAULT NULL COMMENT '描述',
  `ya_money` varchar(30) DEFAULT NULL COMMENT '押金',
  `type` int(4) DEFAULT NULL COMMENT '1=未删除2=删除',
  `path` varchar(255) DEFAULT NULL COMMENT '地址',
  `state` varchar(5) DEFAULT NULL COMMENT '1=已预定或已出租，2等于空闲',
  `id` varchar(50) NOT NULL COMMENT '房间ID',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of home
-- ----------------------------
INSERT INTO `home` VALUES ('900', '909', '窑洞、地坑院、沙窝别墅、林间木屋、城市民居……作为旅游领域这几年涌现出来的新兴业态，民宿业的发展势头可谓强劲。民宿的发展过程中有哪些故事？各地又是如何推进民宿产业走向规范和兴盛的？让我们在全省各地走一走，带您去一探究竟吧。', '500', '1', '居隐阁大房', '2', '2f2eb3e0-5145-11e9-bbbb-085700f5cdd2');
INSERT INTO `home` VALUES ('1', '1', '1', '1', '2', '1', '2', '92a8cce6-513e-11e9-bbbb-085700f5cdd2');
INSERT INTO `home` VALUES ('800', '808', '说起民宿，很多人并不陌生。有别于传统的酒店、旅馆，这是一种为游客提供体验当地风土人情、自然文化生活的住宿方式。人们远离都市，来到青山绿水之间，住进各具风情和地方特色的民宿中，观景之后，还可以在民宿中尽情地感受当地人的日常生活。', '500', '1', '居隐阁豪华房', '2', 'aa630938-513d-11e9-bbbb-085700f5cdd2');
INSERT INTO `home` VALUES ('500', '908', '旅游民宿是利用当地闲置资源，民宿主人参与接待，为游客提供体验当地自然、文化与生产生活方式的小型住宿设施。旅游民宿分为二个等级，金宿级、银宿级。金宿级为高等级，银宿级为普通等级。等级越高表示接待设施与服务品质越高。', '200', '1', '居隐阁小房', '2', 'ef926a16-545e-11e9-8a4b-085700f5cdd2');

-- ----------------------------
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `user_id` varchar(50) DEFAULT NULL COMMENT '用户id',
  `home_id` varchar(50) DEFAULT NULL COMMENT '房间ID',
  `id` varchar(50) NOT NULL COMMENT '订单ID',
  `ya_money` varchar(255) DEFAULT NULL COMMENT '押金金额',
  `money` varchar(255) DEFAULT NULL COMMENT '房费金额',
  `type` varchar(5) DEFAULT NULL COMMENT '1=未入住，2=已入住',
  `plun` varchar(255) DEFAULT NULL COMMENT '评论',
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of order
-- ----------------------------
INSERT INTO `order` VALUES ('0dad1906-545f-11e9-8a4b-085700f5cdd2', 'ef926a16-545e-11e9-8a4b-085700f5cdd2', '1eefa242-545f-11e9-8a4b-085700f5cdd2', '200', '500', '3', '房子整洁舒服，风景好', '2019-04-01 09:18:32');
INSERT INTO `order` VALUES ('0dad1906-545f-11e9-8a4b-085700f5cdd2', 'aa630938-513d-11e9-bbbb-085700f5cdd2', 'b3ec07aa-545f-11e9-8a4b-085700f5cdd2', '500', '800', '1', null, '2019-04-01 09:22:42');
INSERT INTO `order` VALUES ('be61302a-5130-11e9-bbbb-085700f5cdd2', '2f2eb3e0-5145-11e9-bbbb-085700f5cdd2', 'c9f089a4-545a-11e9-8a4b-085700f5cdd2', '500', '900', '2', '', '2019-04-01 08:47:32');
INSERT INTO `order` VALUES ('be61302a-5130-11e9-bbbb-085700f5cdd2', 'aa630938-513d-11e9-bbbb-085700f5cdd2', 'f5465efc-5451-11e9-8a4b-085700f5cdd2', '500', '800', '3', '房间整洁好', '2019-04-01 07:44:19');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `name` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `id` varchar(50) DEFAULT NULL,
  `type` int(4) DEFAULT NULL COMMENT '1=正常，2=注销',
  `z_name` varchar(255) DEFAULT NULL COMMENT '真实姓名',
  `telephone` varchar(255) DEFAULT NULL COMMENT '电话'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('css', '123456', '0dad1906-545f-11e9-8a4b-085700f5cdd2', '1', '陈笑笑', '123456789');
INSERT INTO `user` VALUES ('wjj', '123', 'be61302a-5130-11e9-bbbb-085700f5cdd2', '1', '吴镓俊', '13249994131');
INSERT INTO `user` VALUES ('wss', '123456', '6a5c74cc-545e-11e9-8a4b-085700f5cdd2', '1', '吴思思', '123456789');
