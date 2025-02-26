CREATE TABLE `users` (
    `id` INT AUTO_INCREMENT,
    `first_name` VARCHAR(16) NOT NULL,
    `last_name` VARCHAR(16) NOT NULL,
    `username` VARCHAR (32) NOT NULL UNIQUE,
    `password` VARCHAR(128) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `schools` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR (32) NOT NULL,
    `type` ENUM('Primary', 'Secondary', 'Higher Education') NOT NULL ,
    `location` VARCHAR(128) NOT NULL,
    `year` INT NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `companies` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR (32) NOT NULL,
    `industry` ENUM('Technology', 'Education', 'Business') NOT NULL ,
    `location` VARCHAR(128) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `connections_users` (
    `user1` INT,
    `user2` INT,
    PRIMARY KEY(`user1`, `user2`),
    FOREIGN KEY (`user1`) REFERENCES `users`(`id`),
    FOREIGN KEY (`user2`) REFERENCES `users`(`id`)
);

CREATE TABLE `connections_school` (
    `user_id` INT,
    `school_id` INT,
    `start_date` DATETIME NOT NULL,
    `end_date` DATETIME,
    `type` TEXT NOT NULL,
    PRIMARY KEY(`user_id`, `school_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`school_id`) REFERENCES `schools`(`id`)
);
