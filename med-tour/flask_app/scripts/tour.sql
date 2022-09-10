-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema tour
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tour
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tour` DEFAULT CHARACTER SET utf8 ;
USE `tour` ;

-- -----------------------------------------------------
-- Table `tour`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tour`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(155) NULL DEFAULT NULL,
  `last_name` VARCHAR(155) NULL DEFAULT NULL,
  `age` INT NULL DEFAULT NULL,
  `nationality` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `tour`.`places`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tour`.`places` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `place_name` VARCHAR(255) NULL DEFAULT NULL,
  `category` VARCHAR(255) NULL DEFAULT NULL,
  `price_range` VARCHAR(255) NULL DEFAULT NULL,
  `schedule` VARCHAR(255) NULL DEFAULT NULL,
  `location` VARCHAR(255) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `reference_place` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_places_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_places_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `tour`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `tour`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tour`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `place_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `comments` TEXT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_places_has_users_users2_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_places_has_users_places2_idx` (`place_id` ASC) VISIBLE,
  CONSTRAINT `fk_places_has_users_places2`
    FOREIGN KEY (`place_id`)
    REFERENCES `tour`.`places` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_places_has_users_users2`
    FOREIGN KEY (`user_id`)
    REFERENCES `tour`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `tour`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tour`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `place_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_places_has_users_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_places_has_users_places1_idx` (`place_id` ASC) VISIBLE,
  CONSTRAINT `fk_places_has_users_places1`
    FOREIGN KEY (`place_id`)
    REFERENCES `tour`.`places` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_places_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `tour`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
