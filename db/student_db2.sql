CREATE TABLE TABLE IF NOT EXISTS  students (
    `student_id` INT AUTO_INCREMENT PRIMARY KEY,
    `department` ENUM ('SCM','SBE','SCCD'),
    `first_name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) UNIQUE NOT NULL,
    `password` CHAR(60) NOT NULL,
    `created_at` timestamp NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NULL DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--  a delegates and admin side(Review this as per your thoughts)
CREATE TABLE TABLE IF NOT EXISTS  users (
  `admin_id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_type` ENUM('delegate','admin','polling_officer'),
  `admin` BOOLEAN NOT NULL,
  `password` CHAR(60) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE TABLE IF NOT EXISTS  term (
    `term_id` VARCHAR(255) AUTO_INCREMENT PRIMARY KEY,
    `date_created` DATETIME,
    `status` ENUM('ongoing', 'completed', 'pending', 'cancelled'),
    `start_time` DATETIME,
    `end_time` DATETIME,
    `created_at` timestamp NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NULL DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE TABLE IF NOT EXISTS  positions (
    `position_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name_of_position` VARCHAR(255) NOT NULL,
    `rules` TEXT,
    `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE TABLE IF NOT EXISTS  candidates (
    `candidate_id` INT AUTO_INCREMENT PRIMARY KEY,
    `term_id` VARCHAR(255),
    `student_id` INT,
    `position_id` INT,
    `no_of_votes` INT,
    `deleted_at` TIMESTAMP,
    `created_at` timestamp NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NULL DEFAULT NULL,
    FOREIGN KEY (term_id) REFERENCES term(term_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (position_id) REFERENCES positions(position_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE TABLE IF NOT EXISTS  voting (
    `voting_id` INT AUTO_INCREMENT PRIMARY KEY,
    `student_id` INT,
    `term_id` VARCHAR(255),
    `candidate_id` INT,
    `position_id` INT,
    `hash` VARCHAR(255),
    `created_at` timestamp NULL DEFAULT current_timestamp(),
    `updated_at` timestamp NULL DEFAULT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (term_id) REFERENCES term(term_id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
    FOREIGN KEY (position_id) REFERENCES positions(position_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
