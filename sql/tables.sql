CREATE SCHEMA IF NOT EXISTS `idhms` DEFAULT CHARACTER SET utf8 ;
USE `idhms` ;

CREATE TABLE IF NOT EXISTS `idhms`.`estados` (
  `idEstado` INT NOT NULL,
  `nome` VARCHAR(45) NULL DEFAULT NULL,
  `uf` VARCHAR(45) NULL DEFAULT NULL,
  `ibge` INT NULL DEFAULT NULL,
  `regiao` VARCHAR(45) NULL DEFAULT NULL,
  `sintaxe` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idEstado`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `idhms`.`cidades` (
  `idCidade` INT NOT NULL AUTO_INCREMENT,
  `idEstado` INT NULL DEFAULT NULL,
  `nome` VARCHAR(45) NULL DEFAULT NULL,
  `idhm` FLOAT NULL DEFAULT NULL,
  `idhmRenda` FLOAT NULL DEFAULT NULL,
  `idhmLongv` FLOAT NULL DEFAULT NULL,
  `idhmEdu` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`idCidade`),
  INDEX `idEstados_idx` (`idEstado` ASC) VISIBLE,
  CONSTRAINT `idEstado`
    FOREIGN KEY (`idEstado`)
    REFERENCES `idhms`.`estados` (`idEstado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `idhms`.`casoFullCovid` (
  `date` DATE NULL,
  `state` VARCHAR(3) NULL,
  `city` VARCHAR(60) NULL,
  `place_type` VARCHAR(10) NULL,
  `confirmed` VARCHAR(15) NULL,
  `deaths` VARCHAR(15) NULL,
  `order_for_place` VARCHAR(7) NULL,
  `is_last` VARCHAR(5) NULL,
  `estimated_population_2019` VARCHAR(15) NULL,
  `city_ibge_code` VARCHAR(10) NULL,
  `confirmed_per_100k_inhabitants` VARCHAR(15) NULL,
  `death_rate` VARCHAR(7) NULL)
ENGINE = InnoDB;