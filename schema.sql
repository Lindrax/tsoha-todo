DROP TABLE  if EXISTS users CASCADE;
DROP TABLE  if EXISTS tasks CASCADE;
DROP TABLE  if EXISTS done CASCADE;
DROP TABLE  if EXISTS categories CASCADE;
DROP TABLE  if EXISTS calendar CASCADE;
DROP TABLE  if EXISTS deadlines CASCADE;


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
        deadline text,
        col text default '#FFFFFF');

CREATE TABLE deadlines (id serial primary key,
  task text,
    user_id int,
    deadline text);

CREATE TABLE done (id serial PRIMARY KEY,
 task_id int,
  user_id int,
   time text);

CREATE TABLE categories (id serial PRIMARY KEY,
  category text,
    user_id int,
     color text);

Create TABLE calendar (id serial primary key,
  event text,
    time text,
      user_id int);



  



