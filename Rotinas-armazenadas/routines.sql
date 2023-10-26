use aunimal_hotel_pet;

-- -----------------------------------------------------------------------------------
-- STORED PROCEDURES
-- -----------------------------------------------------------------------------------

-- Excluir registro de reserva e os dados associados
DELIMITER $$
CREATE PROCEDURE deletar_reserva (IN _reserva_id INT)
BEGIN
    DELETE FROM cobranca_forma WHERE id_cobranca = _reserva_id;
    DELETE FROM cobranca WHERE id_reserva = _reserva_id;
	DELETE FROM pet_reserva WHERE id_reserva = _reserva_id;
	DELETE FROM reserva_servico WHERE id_reserva = _reserva_id;
	DELETE FROM reserva WHERE id_reserva = _reserva_id;
END $$
DELIMITER ;
CALL deletar_reserva(1);

-- Cadastrar novo funcionário e seus dados pessoais
DELIMITER %%
CREATE PROCEDURE formulario_admissao (
	IN p_nome VARCHAR(100),
	IN p_nascimento DATE,
    IN p_cpf CHAR(11),
    IN p_rg CHAR(11),
    IN p_sexo ENUM('M', 'F', 'NI'),
    IN p_email VARCHAR(50),
    IN p_est_civil ENUM('SOLTEIRO', 'CASADO', 'DIVORCIADO', 'SEPARADO', 'VIUVO'),
    IN p_nacionalidade VARCHAR(100),
    IN f_profissao VARCHAR(100),
    IN f_salario DECIMAL(10, 2),
    IN c_codigo_pais TINYINT,
    IN c_codigo_area TINYINT,
    IN c_numero BIGINT,
    IN e_cep CHAR(8),
    IN e_logradouro VARCHAR(50),
    IN e_numero SMALLINT UNSIGNED,
    IN e_bairro VARCHAR(50),
    IN e_cidade VARCHAR(100),
    IN e_estado VARCHAR(100))
BEGIN
    DECLARE pessoa_id INT;

    INSERT INTO pessoa
    VALUES (NULL, p_nome, p_nascimento, p_cpf, p_rg, p_sexo, p_email, p_est_civil, p_nacionalidade, NOW());

    -- Obter o último ID da pessoa cadastrada
    SET pessoa_id = LAST_INSERT_ID();

    INSERT INTO contato
    VALUES (c_codigo_pais, c_codigo_area, c_numero, pessoa_id);

    INSERT INTO endereco
    VALUES (NULL, NOW(), e_cep, e_logradouro, e_numero, e_bairro, e_cidade, e_estado, pessoa_id);

    INSERT INTO funcionario
    VALUES (NULL, NOW(), f_profissao, f_salario);
END %%
DELIMITER ;

-- Atualizar todos os dados de um pet
DELIMITER ||
CREATE PROCEDURE atualizar_pet (
	IN _id_pet INT,
	IN _classificacao VARCHAR(100),
    IN _tipo ENUM('GATO','CACHORRO'),
    IN _nome VARCHAR(100),
    IN _peso DECIMAL(5,2),
    IN _sexo ENUM('M','F'),
    IN _pelagem VARCHAR(100),
    IN _porte ENUM('PP','P','M','G','GG'),
    IN _nascimento DATE,
    IN _descricao TINYTEXT,
    IN _id_especie INT)
BEGIN
	DECLARE analisar_pet INT;
    DECLARE analisar_especie INT;
    
	SELECT COUNT(*) INTO analisar_pet FROM pet WHERE id_pet = _id_pet;
    SELECT COUNT(*) INTO analisar_especie FROM especie WHERE id_especie = _id_especie;
    
	IF analisar_pet = 1 AND analisar_especie = 1 THEN
		UPDATE pet 
			SET nome = _nome,
				peso = _peso,
				sexo = _sexo,
				pelagem = _pelagem,
				porte = _porte,
				nascimento = _nascimento,
				descricao = _descricao,
                id_especie = _id_especie
		WHERE id_pet = _id_pet;
	ELSE 
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Pet não encontrado, verifique o ID.';
    END IF;
END ||
DELIMITER ;

CALL atualizar_pet(inserir);

-- -----------------------------------------------------------------------------------
-- FUNCTIONS
-- -----------------------------------------------------------------------------------

-- Exibir o dia do nascimento
-- (Prof. usei essa função, pois fui fazendo junto com o senhor no dia da aula e também por ter gostado muito)
DELIMITER ||
CREATE FUNCTION dia_nasc (_data DATE)
RETURNS VARCHAR(200) DETERMINISTIC

BEGIN
DECLARE dia_semana VARCHAR(200);

CASE DAYOFWEEK(_data)
WHEN 1 THEN SET dia_semana := "Domingo";
WHEN 2 THEN SET dia_semana := "Segunda";
WHEN 3 THEN SET dia_semana := "Terça";
WHEN 4 THEN SET dia_semana := "Quarta";
WHEN 5 THEN SET dia_semana := "Quinta";
WHEN 6 THEN SET dia_semana := "Sexta";
ELSE SET dia_semana := "Sábado";
END CASE;
RETURN dia_semana;

END ||
DELIMITER ;

-- Faturamento total por serviço
DELIMITER ||
CREATE FUNCTION faturamento_servico(id_servico INT)
RETURNS DECIMAL(10,2) DETERMINISTIC
BEGIN
    DECLARE total INT;
    
    SELECT SUM(s.valor_total) INTO total
    FROM servico s
    JOIN reserva_servico rs ON s.id_servico = rs.id_servico
    WHERE s.id_servico = id_servico;
    
    RETURN total;
END ||
DELIMITER ;

SELECT faturamento_servico(6);
    
-- -----------------------------------------------------------------------------------
-- TRIGGERS
-- -----------------------------------------------------------------------------------
    