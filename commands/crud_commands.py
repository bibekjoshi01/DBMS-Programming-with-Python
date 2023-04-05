CREATE_TABLE = (
        """
        CREATE TABLE course(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE student(
            id SERIAL PRIMARY KEY,
            roll_no INTEGER UNIQUE,
            full_name VARCHAR(100) NOT NULL,
            age INTEGER CHECK (age>=18 AND age<=30),
            dob DATE,
            course_id INTEGER,
            CONSTRAINT fk_course
                FOREIGN KEY (course_id)
                REFERENCES course(id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE teacher(
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100) NOT NULL,
            qualification VARCHAR(100) NOT NULL,
            course_id integer,
            CONSTRAINT fk_course
                FOREIGN KEY (course_id)
                REFERENCES course(id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )
