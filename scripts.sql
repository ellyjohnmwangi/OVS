CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password CHAR(60) NOT NULL
);
CREATE TABLE term (
    term_id VARCHAR(255) AUTO_INCREMENT PRIMARY KEY,
    date_created DATETIME,
    status ENUM('ongoing', 'completed', 'pending', 'cancelled'),
    start_time DATETIME,
    end_time DATETIME
);
CREATE TABLE positions (
    position_id INT AUTO_INCREMENT PRIMARY KEY,
    name_of_position VARCHAR(255) NOT NULL,
    rules TEXT
);
CREATE TABLE candidates (
    candidate_id INT AUTO_INCREMENT PRIMARY KEY,
    term_id VARCHAR(255),
    student_id INT,
    position_id INT,
    no_of_votes INT,
    deleted_at TIMESTAMP,
    FOREIGN KEY (term_id) REFERENCES term(term_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (position_id) REFERENCES positions(position_id)
);
CREATE TABLE voting (
    voting_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    term_id VARCHAR(255),
    candidate_id INT,
    position_id INT,
    hash VARCHAR(255),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (term_id) REFERENCES term(term_id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
    FOREIGN KEY (position_id) REFERENCES positions(position_id)
);
