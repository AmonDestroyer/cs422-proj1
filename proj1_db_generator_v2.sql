-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema proj1_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proj1_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proj1_db` DEFAULT CHARACTER SET utf8mb3 ;
USE `proj1_db` ;

-- -----------------------------------------------------
-- Table `proj1_db`.`Time Unit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Time Unit` (
  `tu_id` INT NOT NULL,
  `unit_name` VARCHAR(45) NULL,
  PRIMARY KEY (`tu_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`Set Type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Set Type` (
  `set_type_id` INT NOT NULL,
  `set_type` VARCHAR(45) NULL,
  PRIMARY KEY (`set_type_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`TS_Set`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`TS_Set` (
  `set_id` INT NOT NULL,
  `set_name` VARCHAR(200) NULL,
  `description` VARCHAR(1000) NULL,
  `vector_size` INT NULL,
  `min_length` INT NULL,
  `max_length` INT NULL,
  `num_ts` INT NULL,
  `start_datetime` DATETIME NULL,
  `tu_id` INT NOT NULL,
  `set_type_id` INT NOT NULL,
  PRIMARY KEY (`set_id`),
  INDEX `fk_TS_Set_Time Unit1_idx` (`tu_id` ASC) VISIBLE,
  INDEX `fk_TS_Set_Set Type1_idx` (`set_type_id` ASC) VISIBLE,
  CONSTRAINT `fk_TS_Set_Time Unit1`
    FOREIGN KEY (`tu_id`)
    REFERENCES `proj1_db`.`Time Unit` (`tu_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TS_Set_Set Type1`
    FOREIGN KEY (`set_type_id`)
    REFERENCES `proj1_db`.`Set Type` (`set_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`Time Series`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Time Series` (
  `ts_id` INT NOT NULL,
  `ts_name` VARCHAR(100) NULL,
  `description` VARCHAR(1000) NULL,
  `y_unit` VARCHAR(45) NULL,
  `scalar/vector` TINYINT NULL,
  `vector_size` INT NULL,
  `length` INT NULL,
  `sampling_period` INT NULL,
  `set_id` INT NOT NULL,
  PRIMARY KEY (`ts_id`),
  INDEX `fk_Time Series_TS_Set1_idx` (`set_id` ASC) VISIBLE,
  CONSTRAINT `fk_Time Series_TS_Set1`
    FOREIGN KEY (`set_id`)
    REFERENCES `proj1_db`.`TS_Set` (`set_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`Keyword`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Keyword` (
  `keyword_id` INT NOT NULL,
  `keyword` VARCHAR(100) NULL,
  PRIMARY KEY (`keyword_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`Contributor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Contributor` (
  `contrib_id` INT NOT NULL,
  `contrib_fname` VARCHAR(100) NULL,
  `contrib_lname` VARCHAR(100) NULL,
  PRIMARY KEY (`contrib_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.` Domain`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.` Domain` (
  `domain_id` INT NOT NULL,
  `domain_name` VARCHAR(1000) NULL,
  PRIMARY KEY (`domain_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`Paper`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Paper` (
  `paper_id` INT NOT NULL,
  `paper_reference` VARCHAR(1000) NULL,
  `paper_link` VARCHAR(1000) NULL,
  PRIMARY KEY (`paper_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`Set-Keyword_Join`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Set-Keyword_Join` (
  `keyword_id` INT NOT NULL,
  `set_id` INT NOT NULL,
  PRIMARY KEY (`keyword_id`, `set_id`),
  INDEX `fk_Keyword_has_TS_Set_TS_Set1_idx` (`set_id` ASC) VISIBLE,
  INDEX `fk_Keyword_has_TS_Set_Keyword1_idx` (`keyword_id` ASC) VISIBLE,
  CONSTRAINT `fk_Keyword_has_TS_Set_Keyword1`
    FOREIGN KEY (`keyword_id`)
    REFERENCES `proj1_db`.`Keyword` (`keyword_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Keyword_has_TS_Set_TS_Set1`
    FOREIGN KEY (`set_id`)
    REFERENCES `proj1_db`.`TS_Set` (`set_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`Set-Contributor_Join`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Set-Contributor_Join` (
  `contrib_id` INT NOT NULL,
  `set_id` INT NOT NULL,
  PRIMARY KEY (`contrib_id`, `set_id`),
  INDEX `fk_Contributor_has_TS_Set_TS_Set1_idx` (`set_id` ASC) VISIBLE,
  INDEX `fk_Contributor_has_TS_Set_Contributor1_idx` (`contrib_id` ASC) VISIBLE,
  CONSTRAINT `fk_Contributor_has_TS_Set_Contributor1`
    FOREIGN KEY (`contrib_id`)
    REFERENCES `proj1_db`.`Contributor` (`contrib_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Contributor_has_TS_Set_TS_Set1`
    FOREIGN KEY (`set_id`)
    REFERENCES `proj1_db`.`TS_Set` (`set_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`Set-Paper_Join`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Set-Paper_Join` (
  `paper_id` INT NOT NULL,
  `set_id` INT NOT NULL,
  PRIMARY KEY (`paper_id`, `set_id`),
  INDEX `fk_Paper_has_TS_Set_TS_Set1_idx` (`set_id` ASC) VISIBLE,
  INDEX `fk_Paper_has_TS_Set_Paper1_idx` (`paper_id` ASC) VISIBLE,
  CONSTRAINT `fk_Paper_has_TS_Set_Paper1`
    FOREIGN KEY (`paper_id`)
    REFERENCES `proj1_db`.`Paper` (`paper_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Paper_has_TS_Set_TS_Set1`
    FOREIGN KEY (`set_id`)
    REFERENCES `proj1_db`.`TS_Set` (`set_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`Timeseries-Keyword_Join`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Timeseries-Keyword_Join` (
  `ts_id` INT NOT NULL,
  `keyword_id` INT NOT NULL,
  PRIMARY KEY (`ts_id`, `keyword_id`),
  INDEX `fk_Timeseries_has_Keyword_Keyword1_idx` (`keyword_id` ASC) VISIBLE,
  INDEX `fk_Timeseries_has_Keyword_Timeseries1_idx` (`ts_id` ASC) VISIBLE,
  CONSTRAINT `fk_Timeseries_has_Keyword_Timeseries1`
    FOREIGN KEY (`ts_id`)
    REFERENCES `proj1_db`.`Time Series` (`ts_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Timeseries_has_Keyword_Keyword1`
    FOREIGN KEY (`keyword_id`)
    REFERENCES `proj1_db`.`Keyword` (`keyword_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`TS_Measurement`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`TS_Measurement` (
  `tsm_id` INT NOT NULL,
  `x_val` INT NULL,
  `y_val` DOUBLE NULL,
  `ts_id` INT NOT NULL,
  PRIMARY KEY (`tsm_id`),
  INDEX `fk_TS_Measurement_Time Series1_idx` (`ts_id` ASC) VISIBLE,
  CONSTRAINT `fk_TS_Measurement_Time Series1`
    FOREIGN KEY (`ts_id`)
    REFERENCES `proj1_db`.`Time Series` (`ts_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`Timeseries-Domain_Join`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`Timeseries-Domain_Join` (
  `domain_id` INT NOT NULL,
  `ts_id` INT NOT NULL,
  PRIMARY KEY (`domain_id`, `ts_id`),
  INDEX `fk_ Domain_has_Time Series_Time Series1_idx` (`ts_id` ASC) VISIBLE,
  INDEX `fk_ Domain_has_Time Series_ Domain1_idx` (`domain_id` ASC) VISIBLE,
  CONSTRAINT `fk_ Domain_has_Time Series_ Domain1`
    FOREIGN KEY (`domain_id`)
    REFERENCES `proj1_db`.` Domain` (`domain_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ Domain_has_Time Series_Time Series1`
    FOREIGN KEY (`ts_id`)
    REFERENCES `proj1_db`.`Time Series` (`ts_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proj1_db`.`TimeseriesSet-Domain_Join`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj1_db`.`TimeseriesSet-Domain_Join` (
  `set_id` INT NOT NULL,
  `domain_id` INT NOT NULL,
  PRIMARY KEY (`set_id`, `domain_id`),
  INDEX `fk_TS_Set_has_ Domain_ Domain1_idx` (`domain_id` ASC) VISIBLE,
  INDEX `fk_TS_Set_has_ Domain_TS_Set1_idx` (`set_id` ASC) VISIBLE,
  CONSTRAINT `fk_TS_Set_has_ Domain_TS_Set1`
    FOREIGN KEY (`set_id`)
    REFERENCES `proj1_db`.`TS_Set` (`set_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TS_Set_has_ Domain_ Domain1`
    FOREIGN KEY (`domain_id`)
    REFERENCES `proj1_db`.` Domain` (`domain_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
