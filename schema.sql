DROP TABLE  if EXISTS users CASCADE;
DROP TABLE  if EXISTS tasks CASCADE;


CREATE TABLE users (id serial primary key,
 name text,
  password text);

CREATE TABLE tasks (id serial primary key,
 task text,
  user_id int,
   done BOOL DEFAULT FALSE,
    time text);

CREATE TABLE done (id serial PRIMARY KEY,
 task_id int,
  user_id int,
   time text);

CREATE TABLE deadlines (id serial PRIMARY KEY,
  task_id int,
    user_id int,
      dl text);
  



