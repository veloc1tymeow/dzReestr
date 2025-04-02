CREATE DATABASE human_friends;
USE human_friends;
CREATE TABLE home_animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    type VARCHAR(50),
    commands TEXT,
    birth_date DATE
);

CREATE TABLE pack_animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    type VARCHAR(50),
    commands TEXT,
    birth_date DATE
);
INSERT INTO home_animals (name, type, commands, birth_date) VALUES
('Барсик', 'Кошка', 'Сидеть, Лапу', '2021-06-15'),
('Рекс', 'Собака', 'Фас, Голос', '2020-03-22'),
('Гоша', 'Хомяк', 'Бегать', '2022-01-10');

INSERT INTO pack_animals (name, type, commands, birth_date) VALUES
('Буцефал', 'Лошадь', 'Рысить', '2019-05-04'),
('Верблюд', 'Верблюд', 'Стоять', '2018-11-02'),
('Иа', 'Осел', 'Груз', '2020-08-17');
DELETE FROM pack_animals WHERE type = 'Верблюд';
