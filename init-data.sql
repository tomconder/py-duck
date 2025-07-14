drop table if exists t_department;
drop table if exists t_employee;

create table t_department
(
    id       integer primary key,
    name     text not null,
    location text not null
);

create sequence seq_department_id start 1;

create table t_employee
(
    id            integer primary key,
    name          text    not null,
    job           text    not null,
    manager_id    integer null,
    hire_date     integer not null,
    salary        integer not null,
    department_id integer not null
);

create sequence seq_employee_id start 1;

insert into t_department
values (nextval('seq_department_id'), 'Tech', 'Memphis');
insert into t_department
values (nextval('seq_department_id'), 'Finance', 'Dallas');

insert into t_employee
values (nextval('seq_employee_id'), 'Vince', 'engineer', null, 1514505600, 100, 1);
insert into t_employee
values (nextval('seq_employee_id'), 'Mary', 'trainee', null, 1622505600, 50, 1);

insert into t_employee
values (nextval('seq_employee_id'), 'Tom', 'director', null, 1514505600, 200, 2);
insert into t_employee
values (nextval('seq_employee_id'), 'Penny', 'assistant', null, 1546272600, 100, 2);
