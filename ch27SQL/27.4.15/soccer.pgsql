-- DROP TABLE IF EXISTS teams, seasons, games, players, referees, goals;

DROP DATABASE soccer_db;

CREATE DATABASE soccer_db;

CREATE TABLE teams(
    id serial PRIMARY KEY,
    team_name text NOT NULL UNIQUE,
    ranking int
);

CREATE TABLE seasons(
    id serial PRIMARY KEY,
    start_date date NOT NULL,
    end_date date NOT NULL
);

CREATE TABLE games(
    id serial PRIMARY KEY,
    game_name text NOT NULL DEFAULT 'Soccer Match',
    first_team_id int REFERENCES teams(id) ON DELETE SET NULL,
    second_team_id int REFERENCES teams(id) ON DELETE SET NULL,
    season_id int REFERENCES seasons(id) ON DELETE SET NULL
);

CREATE TABLE players(
    id serial PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    team_id int REFERENCES teams(id) ON DELETE SET NULL
);

CREATE TABLE referees(
    id serial PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    game_id int REFERENCES games(id) ON DELETE SET NULL
);

CREATE TABLE goals(
    id serial PRIMARY KEY,
    player_id int REFERENCES players(id) ON DELETE SET NULL,
    game_id int REFERENCES games(id) ON DELETE SET NULL,
    goal_time time NOT NULL
);

-- vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INSERTS vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
INSERT INTO teams(team_name, ranking)
    VALUES ('Tigers', 1),
('Giants', 2),
('Captains', 3),
('Lions', 4),
('Housewives', 5),
('Rockets', 6),
('Tumbleweeds', 7);

INSERT INTO seasons(start_date, end_date)
    VALUES ('2020-08-01', '2021-05-23'),
('2019-07-15', '2020-05-24'),
('2018-08-01', '2019-05-26'),
('2017-07-15', '2018-05-27'),
('2016-08-01', '2017-05-28');

INSERT INTO games(game_name, first_team_id, second_team_id, season_id)
    VALUES ('The Game', 1, 2, 3),
('The Retribution', 2, 5, 2),
('Annhilation', 4, 3, 4),
('Comeback Time', 1, 7, 5), 




INSERT INTO players(first_name, last_name, team_id)
VALUES 
('Aiden', 'Nakamura', 1),
('Aaliyah', 'Smith', 1),
('Lakshmi', 'Patel', 1),
('Carlos', 'Gutierrez', 2),
('Fatima', 'Khan', 2),
('Grace', 'Owusu', 2),
('Xiu', 'Li', 3),
('Leon', 'Dubois', 3),
('Tariq', 'Hassan', 3),
('Anika', 'Krishna', 4),
('John', 'Nguyen', 4),
('Chiamaka', 'Okafor', 4),
('Sergio', 'Fernandez', 5),
('Ella', 'Cohen', 5),
('Ravi', 'Mehta', 5),
('Alejandra', 'Martinez', 6),
('Hiroshi', 'Sato', 6),
('Yasmin', 'Abdullah', 6),
('Dylan', 'Jones', 7),
('Sophie', 'Zhang', 7),
('Kwame', 'Mensah', 7),
('Olga', 'Ivanova', 8),
('Mohammed', 'Ahmed', 8),
('Emily', 'Williams', 8),
('Levi', 'Goldstein', 9),
('Julia', 'Silva', 9),
('Priya', 'Gupta', 9),
('Andre', 'Santos', 10),
('Sarah', 'Murphy', 10),
('Kenzo', 'Watanabe', 10),
('Elena', 'Vasquez', 1),
('Jamal', 'Johnson', 1),
('Lena', 'Kapoor', 1),
('Diego', 'Sanchez', 2),
('Jada', 'Baker', 2),
('Omar', 'Ali', 2),
('Sasha', 'Petrov', 3),
('Nia', 'Campbell', 3),
('Isaac', 'Kim', 3),
('Ava', 'Brown', 4),
('Samuel', 'Oluwale', 4),
('Maya', 'Chen', 4),
('Amir', 'Mossad', 5),
('Zara', 'Hussein', 5),
('Theo', 'Dimitriou', 5),
('Liam', 'OConnor', 6),
('Zoe', 'Schwartz', 6),
('Lucas', 'Rodriguez', 6);

INSERT INTO referees(first_name, last_name, game_id)
    VALUES ('Max', 'Schmidt', 1),
('Sophia', 'Müller', 2),
('Lukas', 'Schneider', 3),
('Emilia', 'Fischer', 4),
('Leon', 'Weber', 5),
('Mia', 'Meyer', 6),
('Felix', 'Wagner', 7),
('Hannah', 'Becker', 8),
('Elias', 'Hoffmann', 9),
('Anna', 'Schulz', 10);

INSERT INTO goals(player_id, game_id, goal_time)
    VALUES (1, 1, '00:12:34'),
(2, 1, '00:23:45'),
(3, 1, '00:35:12'),
(4, 2, '00:07:23'),
(5, 2, '00:19:56'),
(6, 2, '00:42:01'),
(7, 3, '00:15:27'),
(8, 3, '00:28:13'),
(9, 3, '00:39:45'),
(10, 4, '00:08:56'),
(11, 4, '00:16:34'),
(12, 4, '00:29:12'),
(13, 5, '00:05:23'),
(14, 5, '00:18:45'),
(15, 5, '00:31:56'),
(16, 6, '00:11:27'),
(17, 6, '00:22:13'),
(18, 6, '00:37:45'),
(19, 7, '00:09:56'),
(20, 7, '00:21:34'),
(21, 7, '00:33:12'),
(22, 8, '00:13:23'),
(23, 8, '00:25:45'),
(24, 8, '00:38:56'),
(25, 9, '00:06:27'),
(26, 9, '00:19:13'),
(27, 9, '00:32:45'),
(28, 10, '00:10:56'),
(29, 10, '00:23:34'),
(30, 10, '00:36:12'),
(31, 1, '00:08:23'),
(32, 1, '00:20:45'),
(33, 1, '00:33:56'),
(34, 2, '00:12:27'),
(35, 2, '00:24:13'),
(36, 2, '00:37:45'),
(37, 3, '00:09:56'),
(38, 3, '00:21:34'),
(39, 3, '00:34:12'),
(40, 4, '00:11:23'),
(41, 4, '00:22:45'),
(42, 4, '00:35:56'),
(43, 5, '00:07:27'),
(44, 5, '00:19:13'),
(45, 5, '00:32:45'),
(46, 6, '00:10:56'),
(47, 6, '00:23:34'),
(48, 6, '00:36:12'),
(49, 7, '00:08:23'),
(50, 7, '00:20:45');

