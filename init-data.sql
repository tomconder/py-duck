drop table if exists t_employee;
drop table if exists t_department;

create table t_department
(
    id       integer primary key,
    name     text not null,
    location text not null
);

create table t_employee
(
    id            integer primary key,
    name          text    not null,
    job           text    not null,
    manager_id    integer null references t_employee (id),
    hire_date     date    not null,
    salary        integer not null,
    department_id integer not null references t_department (id)
);

insert into t_department
values (1, 'Tech', 'Memphis'),
       (2, 'Finance', 'Dallas');

insert into t_employee
values (1, 'Vince', 'engineer', null, '2017-12-29', 100, 1),
       (2, 'Mary', 'trainee', null, '2021-06-01', 50, 1),
       (3, 'Tom', 'director', null, '2017-12-29', 200, 2),
       (4, 'Penny', 'assistant', null, '2018-12-31', 100, 2);
