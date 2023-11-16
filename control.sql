-- Linguagem de Controle de Dados (DML - do inglês Data Control Language)

-- Criando usuários
CREATE USER 'josiel'@'localhost' IDENTIFIED BY '1222' ;
CREATE USER 'rafaela'@'localhost' IDENTIFIED BY '4555' WITH MAX_USER_CONNECTIONS 2;
CREATE USER 'mateus'@'localhost' IDENTIFIED BY '3224' WITH MAX_USER_CONNECTIONS 5;
CREATE USER 'alcides'@'localhost' IDENTIFIED BY '8895';
CREATE USER 'silvio'@'localhost' IDENTIFIED BY '66255';
CREATE USER 'vilmar'@'localhost' IDENTIFIED BY 'prof.py';
CREATE USER 'Antonio Viniski'@'localhost' IDENTIFIED BY 'eng.dados';

-- Criando papéis
CREATE ROLE 'global_role'; 
CREATE ROLE 'db_role';
CREATE ROLE 'table_role';
CREATE ROLE IF NOT EXISTS 'ceo', 'servidor_terceirizado';

-- Concedendo privilégios
GRANT ALL PRIVILEGES ON *.* TO 'global_role'; -- Acesso global, acesso a todas as tabelas em todos os bancos de dados
GRANT ALL PRIVILEGES ON aunimal_hotel_pet.* TO 'db_role'; -- Acesso a um banco de dados específico
GRANT SELECT ON aunimal_hotel_pet.pagamento TO 'table_role'; -- Acesso a uma tabela específica
GRANT ALL PRIVILEGES ON *.* TO 'ceo'; -- ceo seria endereçado para alguém com acesso global
GRANT SELECT ON aunimal_hotel_pet. * TO 'servidor_terceirizado'; -- seria endereçado a alguém que precisaria somente ver as tabelas

-- Concedendo papéis aos usuários
GRANT 'ceo' TO 'Antonio Viniski'@'localhost';
GRANT 'servidor_terceirizado' TO 'vilmar'@'localhost';
GRANT 'global_role' TO 'josiel'@'localhost';
GRANT 'db_role' TO 'rafaela'@'localhost';
GRANT 'table_role' TO 'mateus'@'localhost';
GRANT 'global_role' TO 'alcides'@'localhost';
GRANT 'db_role' TO 'silvio'@'localhost';
GRANT 'table_role' TO 'Brother'@'localhost';