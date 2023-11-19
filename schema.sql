DROP TABLE  if EXISTS users CASCADE;
DROP TABLE  if EXISTS tasks CASCADE;


CREATE TABLE users (id serial primary key,
 name text,
  password text);

CREATE TABLE tasks (id serial primary key,
 task text,
  user_id int,
   done text DEFAULT 'n');


