
create database test;
grant all on DATABASE test to username;
grant CONNECT on DATABASE test to username ;
alter database test owner to username ;
create database test;
create role username with password 'password';
grant CONNECT on DATABASE test to username ;
grant all on DATABASE test to username;
alter database test owner to username ;
ALTER role username with LOGIN;
\c test
create extension postgis;


