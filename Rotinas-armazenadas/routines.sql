use aunimal_hotel_pet;

-- -----------------------------------------------------------------------------------
-- STORED PROCEDURES
-- -----------------------------------------------------------------------------------

-- Excluir registro de reserva e os dados associados
DELIMITER $$
CREATE PROCEDURE deletar_reserva (IN _reserva_id INT)
BEGIN
    DELETE FROM cobranca WHERE id_reserva = _reserva_id;
	DELETE FROM pet_reserva WHERE id_reserva = _reserva_id;
	DELETE FROM reserva_servico WHERE id_reserva = _reserva_id;
	DELETE FROM reserva WHERE id_reserva = _reserva_id;
END $$
DELIMITER ;

CALL deletar_reserva(1);

-- Cadastrar novo funcionário
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

    -- Cadastrar na tabela pessoa
    INSERT INTO pessoa
    VALUES (NULL, p_nome, p_nascimento, p_cpf, p_rg, p_sexo, p_email, p_est_civil, p_nacionalidade, NOW());

    -- Obter o último ID da pessoa cadastrada
    SET pessoa_id = LAST_INSERT_ID();

    -- Cadastrar na tabela contato
    INSERT INTO contato
    VALUES (c_codigo_pais, c_codigo_area, c_numero, pessoa_id);

    -- Cadastrar na tabela endereço
    INSERT INTO endereco
    VALUES (NULL, NOW(), e_cep, e_logradouro, e_numero, e_bairro, e_cidade, e_estado, pessoa_id);

    -- Cadastrar funcionário
    INSERT INTO funcionario
    VALUES (NULL, NOW(), f_profissao, f_salario);
END %%
DELIMITER ;



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