


DROP TABLE IF EXISTS doctors, patients, visits, disease;
DROP DATABASE hospital_db;
CREATE DATABASE hospital_db;



-- Doctors Table
CREATE TABLE doctors(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    yrs_experience INT NOT NULL
);

-- Patients Table
CREATE TABLE patients(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INT CHECK (age > 0) DEFAULT 1,
    primary_disease_subject VARCHAR(25) NOT NULL
);

-- Visits Table
CREATE TABLE visits(
    id SERIAL PRIMARY KEY,
    doctor_id INT REFERENCES doctors(id) ON DELETE SET NULL,
    patient_id INT REFERENCES patients(id) ON DELETE SET NULL
);

-- Disease Table
CREATE TABLE disease(
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id) ON DELETE SET NULL,
    diagnosed_with_disease BOOLEAN NOT NULL,
    num_of_diseases INT NOT NULL
);



INSERT INTO doctors (first_name, last_name, specialty, yrs_experience)
VALUES
('John','Reginald','Cardiologist', 23),
('Elizabeth','Chang','Neurologist', 4),
('Marcus','Aurelius', 'Radiologist', 100);


INSERT INTO patients(first_name,last_name,age,primary_disease_subject)
VALUES
('Ron','Rodriguez', 29,'Coronary artery disease'),
('Dwayne','Johnson', 48,'Congestive heart failure'),
('Sarah','Galanis', 33,'dementia'),
('Joanna','Okoro', 73,'Bells Palsy');


INSERT INTO visits(doctor_id, patient_id)
VALUES
(1,1),
(1,2),
(2,1),
(2,4),
(2,3),
(3,2),
(3,4);

INSERT INTO disease(patient_id, diagnosed_with_disease, num_of_diseases)
VALUES
(1,true,3),
(2,true,1),
(3,true,2),
(4,true,1);