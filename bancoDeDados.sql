CREATE TABLE imc_registros (
    id SERIAL PRIMARY KEY,
    peso DECIMAL(5, 2) NOT NULL,
    altura DECIMAL(3, 2) NOT NULL,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    feedback TEXT
);

INSERT INTO imc_registros (peso, altura, feedback)
VALUES (75.5, 1.75, 'Peso ideal. Continue mantendo uma vida saudável.');

UPDATE imc_registros
SET peso = 80.0, feedback = 'Você está com sobrepeso. É recomendável rever sua alimentação e praticar exercícios.'
WHERE id = 1;

DELETE FROM imc_registros
WHERE id = 1;
