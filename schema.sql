DROP TABLE  if EXISTS users CASCADE;
DROP TABLE  if EXISTS tasks CASCADE;
DROP TABLE  if EXISTS done CASCADE;
DROP TABLE  if EXISTS deadlines CASCADE;
DROP TABLE  if EXISTS calendar CASCADE;


CREATE TABLE users (id serial primary key,
 name text,
  password text);

CREATE TABLE tasks (id serial primary key,
 task text,
  user_id int,
   done BOOL DEFAULT FALSE,
    del BOOL DEFAULT False,
      time text,
        category text,
        deadline text);

CREATE TABLE done (id serial PRIMARY KEY,
 task_id int,
  user_id int,
   time text);

CREATE TABLE deadlines (id serial PRIMARY KEY,
  task_id int,
    user_id int,
      dl text);

Create TABLE calendar (id serial primary key,
  event text,
    time text,
      user_id int);

  



