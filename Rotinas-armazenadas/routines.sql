-- -----------------------------------------------------------------------------------
-- STORED PROCEDURES
-- -----------------------------------------------------------------------------------

-- Excluir registro de clientes e também seus dados pessoais
DELIMITER $$
CREATE PROCEDURE DeletarCliente(IN _cliente_id INT)
BEGIN
    DELETE FROM cliente WHERE id_cliente = _cliente_id;
    DELETE FROM pessoa WHERE id_pessoa = _cliente_id;
    DELETE FROM endereco WHERE id_endereco = _cliente_id;
END $$
DELIMITER ;