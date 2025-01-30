CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    student_name TEXT,
    house_id INTEGER,
    FOREIGN KEY (house_id) REFERENCES houses(id)
);
CREATE TABLE houses (
    id INTEGER PRIMARY KEY,
    house_name TEXT UNIQUE

);
CREATE TABLE heads (
    head_id INTEGER PRIMARY KEY,
    head_name TEXT,
    house_id INTEGER UNIQUE,
    FOREIGN KEY (house_id) REFERENCES houses(id)


);
--"SELECT s.student_name, h.head_name, hs.house_name FROM students s JOIN houses hs ON s.house_id=hs.id JOIN heads h ON h.house_id=hs.id"
