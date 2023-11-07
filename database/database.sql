CREATE TABLE IF NOT EXISTS students (
  `student_id` INT AUTO_INCREMENT PRIMARY KEY,
  `department` ENUM('SCM', 'SBE', 'SCCD'),
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `password` CHAR(60) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS users (
  `admin_id` INT AUTO_INCREMENT PRIMARY KEY,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `user_type` ENUM('delegate', 'admin', 'polling_officer','student'),
  `password` CHAR(60) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS term (
  `term_id` VARCHAR(255) UNIQUE NOT NULL,
  `date_created` DATETIME,
  `status` ENUM('ongoing', 'completed', 'pending', 'cancelled'),
  `start_time` TIMESTAMP NOT NULL,
  `end_time` TIMESTAMP NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS positions (
  `position_id` INT AUTO_INCREMENT PRIMARY KEY,
  `position` ENUM('delegate','finance','president','secretary general','social welfare','gender'),
  `rules` TEXT,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS candidates (
  `candidate_id` INT AUTO_INCREMENT PRIMARY KEY,
  `term_id` VARCHAR(255),
  `student_id` INT,
  `position_id` INT,
  `no_of_votes` INT,
  `department` ENUM('SCM', 'SBE', 'SCCD'),
  `position` ENUM('delegate','finance','president','secretary general','social welfare','gender'),
  `deleted_at` TIMESTAMP,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (term_id) REFERENCES term(term_id),
  FOREIGN KEY (position) REFERENCES positions(position),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (department) REFERENCES students(department),
  FOREIGN KEY (position_id) REFERENCES positions(position_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS voting (
  `voting_id` INT AUTO_INCREMENT PRIMARY KEY,
  `student_id` INT,
  `term_id` VARCHAR(255),
  `candidate_id` INT,
  `position_id` INT,
  `hash` VARCHAR(255),
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (term_id) REFERENCES term(term_id),
  FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
  FOREIGN KEY (position_id) REFERENCES positions(position_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
