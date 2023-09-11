-- MySQL Workbench Synchronization
-- Generated: 2023-09-10 23:43
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Josiel Queiroz Jr

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER TABLE `aunimal_hotel_pet`.`cliente` 
DROP FOREIGN KEY `fk_cliente_pessoa1`,
DROP FOREIGN KEY `fk_cliente_pet`;

ALTER TABLE `aunimal_hotel_pet`.`cobranca` 
DROP FOREIGN KEY `fk_cobranca_cliente`,
DROP FOREIGN KEY `fk_cobranca_funcionario`;

ALTER TABLE `aunimal_hotel_pet`.`contato` 
DROP FOREIGN KEY `fk_contato_pessoa`;

ALTER TABLE `aunimal_hotel_pet`.`funcionario` 
DROP FOREIGN KEY `fk_funcionario_pessoa1`;

ALTER TABLE `aunimal_hotel_pet`.`pagamento` 
DROP FOREIGN KEY `fk_pagamento_funcionario`;

ALTER TABLE `aunimal_hotel_pet`.`pessoa` 
DROP FOREIGN KEY `fk_pessoa_endereco`;

ALTER TABLE `aunimal_hotel_pet`.`pet` 
DROP FOREIGN KEY `fk_pet_especie`;

ALTER TABLE `aunimal_hotel_pet`.`especie` 
DROP FOREIGN KEY `fk_especie_raca`;

ALTER TABLE `aunimal_hotel_pet`.`reserva` 
DROP FOREIGN KEY `fk_cliente_reserva`,
DROP FOREIGN KEY `fk_funcionario_reserva`;

ALTER TABLE `aunimal_hotel_pet`.`cobranca_forma` 
DROP FOREIGN KEY `fk_cobranca_forma_cobranca`,
DROP FOREIGN KEY `fk_cobranca_forma_forma`;

ALTER TABLE `aunimal_hotel_pet`.`pet_servico` 
DROP FOREIGN KEY `fk_pet_servico_pet`,
DROP FOREIGN KEY `fk_pet_servico_servico`;

ALTER TABLE `aunimal_hotel_pet`.`reserva_servico` 
DROP FOREIGN KEY `fk_reserva_servico_reserva`,
DROP FOREIGN KEY `fk_reserva_servico_servico`;

ALTER TABLE `aunimal_hotel_pet`.`funcionario_servico` 
DROP FOREIGN KEY `fk_funcionario_servico_funcionario`;

ALTER TABLE `aunimal_hotel_pet`.`pet_reserva` 
DROP FOREIGN KEY `fk_pet_reserva_pet`;

ALTER TABLE `aunimal_hotel_pet`.`pessoa` 
DROP PRIMARY KEY,
ADD PRIMARY KEY (`id`);
;

ALTER TABLE `aunimal_hotel_pet`.`cobranca_forma` 
CHANGE COLUMN `parcela` `parcela` VARCHAR(45) NOT NULL ;

ALTER TABLE `aunimal_hotel_pet`.`pet_servico` 
CHANGE COLUMN `id_pet` `id_pet` INT(10) UNSIGNED NOT NULL ;

ALTER TABLE `aunimal_hotel_pet`.`reserva_servico` 
COLLATE = utf8mb4_general_ci ;

ALTER TABLE `aunimal_hotel_pet`.`funcionario_servico` 
COLLATE = utf8mb4_general_ci ;

ALTER TABLE `aunimal_hotel_pet`.`pet_reserva` 
COLLATE = utf8mb4_general_ci ;

ALTER TABLE `aunimal_hotel_pet`.`cliente` 
ADD CONSTRAINT `fk_cliente_pessoa1`
  FOREIGN KEY (`id`)
  REFERENCES `aunimal_hotel_pet`.`pessoa` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_cliente_pet`
  FOREIGN KEY (`id_pet`)
  REFERENCES `aunimal_hotel_pet`.`pet` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`cobranca` 
DROP FOREIGN KEY `fk_cobranca_reserva`;

ALTER TABLE `aunimal_hotel_pet`.`cobranca` ADD CONSTRAINT `fk_cobranca_reserva`
  FOREIGN KEY (`id_reserva`)
  REFERENCES `aunimal_hotel_pet`.`reserva` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_cobranca_cliente`
  FOREIGN KEY (`id_cliente`)
  REFERENCES `aunimal_hotel_pet`.`cliente` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_cobranca_funcionario`
  FOREIGN KEY (`id_funcinario`)
  REFERENCES `aunimal_hotel_pet`.`funcionario` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`contato` 
ADD CONSTRAINT `fk_contato_pessoa`
  FOREIGN KEY (`id_cliente`)
  REFERENCES `aunimal_hotel_pet`.`pessoa` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`funcionario` 
ADD CONSTRAINT `fk_funcionario_pessoa1`
  FOREIGN KEY (`id`)
  REFERENCES `aunimal_hotel_pet`.`pessoa` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`pagamento` 
ADD CONSTRAINT `fk_pagamento_funcionario`
  FOREIGN KEY (`id_funcionario`)
  REFERENCES `aunimal_hotel_pet`.`funcionario` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`pessoa` 
ADD CONSTRAINT `fk_pessoa_endereco`
  FOREIGN KEY (`id_endereco`)
  REFERENCES `aunimal_hotel_pet`.`endereco` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`pet` 
ADD CONSTRAINT `fk_pet_especie`
  FOREIGN KEY (`id_especie`)
  REFERENCES `aunimal_hotel_pet`.`especie` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`especie` 
ADD CONSTRAINT `fk_especie_raca`
  FOREIGN KEY (`id_raca`)
  REFERENCES `aunimal_hotel_pet`.`raca` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`reserva` 
ADD CONSTRAINT `fk_cliente_reserva`
  FOREIGN KEY (`id_cliente`)
  REFERENCES `aunimal_hotel_pet`.`cliente` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_funcionario_reserva`
  FOREIGN KEY (`id_funcionario`)
  REFERENCES `aunimal_hotel_pet`.`funcionario` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`cobranca_forma` 
ADD CONSTRAINT `fk_cobranca_forma_cobranca`
  FOREIGN KEY (`id_cobranca`)
  REFERENCES `aunimal_hotel_pet`.`cobranca` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_cobranca_forma_forma`
  FOREIGN KEY (`id_forma`)
  REFERENCES `aunimal_hotel_pet`.`forma` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`pet_servico` 
ADD CONSTRAINT `fk_pet_servico_pet`
  FOREIGN KEY (`id_pet`)
  REFERENCES `aunimal_hotel_pet`.`pet` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_pet_servico_servico`
  FOREIGN KEY (`id_servico`)
  REFERENCES `aunimal_hotel_pet`.`servico` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`reserva_servico` 
ADD CONSTRAINT `fk_reserva_servico_reserva`
  FOREIGN KEY (`id_reserva`)
  REFERENCES `aunimal_hotel_pet`.`reserva` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_reserva_servico_servico`
  FOREIGN KEY (`id_servico`)
  REFERENCES `aunimal_hotel_pet`.`servico` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`funcionario_servico` 
DROP FOREIGN KEY `fk_funcionario_servico_servico`;

ALTER TABLE `aunimal_hotel_pet`.`funcionario_servico` ADD CONSTRAINT `fk_funcionario_servico_servico`
  FOREIGN KEY (`id_servico`)
  REFERENCES `aunimal_hotel_pet`.`servico` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_funcionario_servico_funcionario`
  FOREIGN KEY (`id_funcionario`)
  REFERENCES `aunimal_hotel_pet`.`funcionario` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;

ALTER TABLE `aunimal_hotel_pet`.`pet_reserva` 
DROP FOREIGN KEY `fk_pet_reserva_reserva`;

ALTER TABLE `aunimal_hotel_pet`.`pet_reserva` ADD CONSTRAINT `fk_pet_reserva_reserva`
  FOREIGN KEY (`id_reserva`)
  REFERENCES `aunimal_hotel_pet`.`reserva` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_pet_reserva_pet`
  FOREIGN KEY (`id_pet`)
  REFERENCES `aunimal_hotel_pet`.`pet` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
