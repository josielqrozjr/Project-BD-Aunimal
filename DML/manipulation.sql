/* Linguagem de Manipulação de Dados (DML - do inglês Data Manipulation Language):*/

USE aunimal_hotel_pet;

-- -----------------------------------------------------------------------------------
-- Inserir ao menos 6 registros em cada uma das tabelas do banco de dados.
-- -----------------------------------------------------------------------------------

INSERT INTO pessoa (nome, nascimento, cpf, rg, sexo, email, est_civil, nacionalidade, data_criacao)
VALUES 
('Ana Souza Luz Wosche', '1992-07-12', '78901234567', '78901234501', 'F', 'ana.souza@gmail.com', 'SEPARADO', 'Brasil', NOW()),
('Lucas Gabriel Oliveira', '1998-04-25', '89012345678', '89012345602', 'M', 'lucas.oliveira@gmail.com', 'DIVORCIADO', 'Brasil', NOW()),
('Camila Silva Sobrinho', '1997-09-03', '90123456789', '90123456703', 'F', 'camila.sobrinho@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('Fernando Rodrigo Pereira', '1984-11-30', '12345678909', '12345878904', 'M', 'fernando.rodrigo@gmail.com', 'CASADO', 'Brasil', NOW()),
('Larissa Santos Flow', '1990-03-15', '23456789098', '23456789005', 'F', 'larissa.flow@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('Ricardo Lima de Sousa', '1986-01-08', '34567890187', '34567890106', 'M', 'ricardo.lima@gmail.com', 'CASADO', 'Brasil', NOW()),
('Josiel Queiroz Júnior', '1994-05-15', '12345678910', '12345978907', 'M', 'josiel.queiroz@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('Rafaela Vecchi Pelentier', '1996-08-20', '23456789012', '23456789008', 'F', 'rafaela.vecchi@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('João Vitor de Lima Antunes', '1998-03-10', '34567890123', '34567890109', 'M', 'joao.antunes@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('Ana Pereira Dias', '1995-11-18', '45678901234', '45678901210', 'F', 'ana.dias@gmail.com', 'SOLTEIRO', 'Brasil', NOW()),
('Roberto Loures Raposo', '1988-09-05', '56789012345', '56789012311', 'M', 'roberto.raposo@gmail.com', 'CASADO', 'Brasil', NOW()),
('Juliana Mascarenhas Soares', '1989-12-30', '67890123456', '67890123412', 'F', 'juliana.mascarenhas@gmail.com', 'VIUVO', 'Brasil', NOW());

INSERT INTO cliente (id_cliente, data_criacao)
VALUES (1, NOW()), (2, NOW()), (3, NOW()), (4, NOW()), (5, NOW()), (6, NOW());

INSERT INTO funcionario (id_funcionario, data_criacao, profissao, salario)
VALUES
(6, NOW(), 'Treinador', 2500.00),
(7, NOW(), 'CEO', 8500.00),
(8, NOW(), 'CEO', 8500.00),
(9, NOW(), 'CEO', 8500.00),
(10, NOW(), 'Analista Administrativo', 2200.00),
(11, NOW(), 'Cuidador', 2860.00),
(12, NOW(), 'Médico veterinário', 3200.00);
       
       
INSERT INTO reserva (check_in, checkout, descricao, valor_total, id_cliente, id_funcionario)
VALUES 
('2023-10-20 12:00:00', '2023-10-25 10:00:00', 'Reserva para férias', 500.00, 1, 10),
('2023-11-05 14:00:00', '2023-11-10 11:00:00', 'Reserva para viagem de negócios', 600.00, 2, 10),
('2023-11-15 10:00:00', '2023-11-20 09:00:00', 'Reserva para evento especial', 700.00, 3, 10),
('2023-12-01 15:00:00', '2023-12-06 13:00:00', 'Reserva para feriado', 550.00, 4, 10),
('2023-12-10 11:00:00', '2023-12-15 08:00:00', 'Reserva para fim de semana', 450.00, 5, 10),
('2023-12-20 16:00:00', '2023-12-28 12:00:00', 'Reserva para Natal', 880.00, 6, 10);

INSERT INTO cobranca (data_cobranca, valor_total, id_reserva, id_funcionario)
VALUES 
('2023-10-26 14:00:00', 500.00, 1, 10),
('2023-11-11 12:00:00', 600.00, 2, 7),
('2023-11-21 09:00:00', 700.00, 3, 10),
('2023-12-07 16:00:00', 550.00, 4, 8),
('2023-12-16 10:00:00', 450.00, 5, 9),
('2024-01-02 18:00:00', 880.00, 6, 10);

INSERT INTO forma (descricao) 
VALUES 
('Cartão de Crédito'), 
('Cartão de Débito'), 
('Dinheiro'), 
('Transferência Bancária'), 
('PIX'), 
('Boleto');

INSERT INTO raca (classificacao) 
VALUES ('Persa'), ('Siamês'), ('Poodle'), ('Bulldog'), ('Golden Retriever'), ('Maine Coon');

INSERT INTO especie (tipo, id_raca) 
VALUES ('GATO', 1), ('GATO', 2), ('CACHORRO', 3), ('CACHORRO', 4), ('CACHORRO', 5), ('GATO', 6);





-- -----------------------------------------------------------------------------------      
-- Criar 5 instruções de atualização de registros em diferentes tabelas.
-- -----------------------------------------------------------------------------------


-- -----------------------------------------------------------------------------------
-- Criar 5 instruções de exclusão de registros em diferentes tabelas.
-- -----------------------------------------------------------------------------------
