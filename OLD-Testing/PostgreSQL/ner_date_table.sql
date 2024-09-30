create table date1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_date VARCHAR(150) NOT NULL
);

create table time1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_time VARCHAR(150) NOT NULL
);

create table org1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_org VARCHAR(200) NOT NULL
);

create table person1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_person VARCHAR(150) NOT NULL
);

create table loc1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_loc VARCHAR(150) NOT NULL
);

create table gpe1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_gpe VARCHAR(150) NOT NULL
);

create table event1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_event VARCHAR(200) NOT NULL
);

create table money1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_money VARCHAR(150) NOT NULL
);

create table cardinal1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_cardinal VARCHAR(150) NOT NULL
);

create table quantity1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_quantity VARCHAR(150) NOT NULL
);

create table ordinal1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_ordinal VARCHAR(150) NOT NULL
);

create table work_of_art1 (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_work_of_art VARCHAR(200) NOT NULL
);

create table law1  (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_law VARCHAR(200) NOT NULL
);   

create table product1  (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_product VARCHAR(150) NOT NULL
);

create table norp1  (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_norp VARCHAR(200) NOT NULL
);

create table fac1  (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ner_fac VARCHAR(200) NOT NULL
);

insert into date1 (id, ner_date) values (1, 'September 7');
insert into date1 (id, ner_date) values (2, 'October 6 October 6');
insert into date1 (id, ner_date) values (3, 'September 7 September 7');
insert into date1 (id, ner_date) values (4, 'November 13');
insert into date1 (id, ner_date) values (5, 'the past couple of months');
insert into date1 (id, ner_date) values (6, 'September 9 September 9');
insert into date1 (id, ner_date) values (7, 'January 2');
insert into date1 (id, ner_date) values (8, 'February 7 2024');
insert into date1 (id, ner_date) values (9, 'September 25 September 25');
insert into date1 (id, ner_date) values (10, 'September 26 2024');
insert into date1 (id, ner_date) values (11, 'September 28');
insert into date1 (id, ner_date) values (12, 'Sunday');
insert into date1 (id, ner_date) values (13, 'September 24 2024');
insert into date1 (id, ner_date) values (14, 'August 29 August 29');
insert into date1 (id, ner_date) values (15, 'October 5 Select date');
insert into date1 (id, ner_date) values (16, 'September 17 2024');
insert into date1 (id, ner_date) values (17, '1980');
insert into date1 (id, ner_date) values (18, 'Saturday the 12th of October');
insert into date1 (id, ner_date) values (19, '2017');
insert into date1 (id, ner_date) values (20, '2022/23');
insert into date1 (id, ner_date) values (21, 'September 8');
insert into date1 (id, ner_date) values (22, 'September 12');
insert into date1 (id, ner_date) values (23, 'weekly');
insert into date1 (id, ner_date) values (24, 'Tuesday');
insert into date1 (id, ner_date) values (25, 'September 1 September 1');
insert into date1 (id, ner_date) values (26, 'October 15, 2024');
insert into date1 (id, ner_date) values (27, 'October 6');
insert into date1 (id, ner_date) values (28, 'November 12');
insert into date1 (id, ner_date) values (29, 'March 18');
insert into date1 (id, ner_date) values (30, 'August 28');
insert into date1 (id, ner_date) values (31, 'September 28 September 28');
insert into date1 (id, ner_date) values (32, 'August 30');
insert into date1 (id, ner_date) values (33, 'daily');
insert into date1 (id, ner_date) values (34, 'December 1');
insert into date1 (id, ner_date) values (35, 'November 7, 2024');
insert into date1 (id, ner_date) values (36, 'November 14');
insert into date1 (id, ner_date) values (37, 'month');
insert into date1 (id, ner_date) values (38, 'September 29');
insert into date1 (id, ner_date) values (39, 'June 20, 2024');
insert into date1 (id, ner_date) values (40, 'March 1');
insert into date1 (id, ner_date) values (41, 'mid week');
insert into date1 (id, ner_date) values (42, 'Remembrance Day 2018');
insert into date1 (id, ner_date) values (43, 'Week this month');
insert into date1 (id, ner_date) values (44, 'September 17');
insert into date1 (id, ner_date) values (45, 'September 10 September 10');
insert into date1 (id, ner_date) values (46, 'August 31');
insert into date1 (id, ner_date) values (47, 'July');
insert into date1 (id, ner_date) values (48, 'September 25');
insert into date1 (id, ner_date) values (49, 'July 24');
insert into date1 (id, ner_date) values (50, 'August 27 August 27');
insert into date1 (id, ner_date) values (51, 'August 28 August 28');
insert into date1 (id, ner_date) values (52, '2003 2007 2008');
insert into date1 (id, ner_date) values (53, 'Thursday');
insert into date1 (id, ner_date) values (54, 'the years');
insert into date1 (id, ner_date) values (55, 'November 12, 2024');
insert into date1 (id, ner_date) values (56, 'September 18');
insert into date1 (id, ner_date) values (57, 'October 22, 2024');
insert into date1 (id, ner_date) values (58, 'September 6 September 6');
insert into date1 (id, ner_date) values (59, 'September 27');
insert into date1 (id, ner_date) values (60, '9:30am Monday, Tuesday');
insert into date1 (id, ner_date) values (61, 'October 10');
insert into date1 (id, ner_date) values (62, 'March 2022');
insert into date1 (id, ner_date) values (63, 'October 3, 2024');
insert into date1 (id, ner_date) values (64, 'March 20');
insert into date1 (id, ner_date) values (65, 'September 11 Select date');
insert into date1 (id, ner_date) values (66, 'June 2024');
insert into date1 (id, ner_date) values (67, 'September 13');
insert into date1 (id, ner_date) values (68, '8:30am Monday');
insert into date1 (id, ner_date) values (69, '2024');
insert into date1 (id, ner_date) values (70, 'October 24, 2024');
insert into date1 (id, ner_date) values (71, 'each week');
insert into date1 (id, ner_date) values (72, 'Thursday, October 26th');
insert into date1 (id, ner_date) values (73, '13 12 30');
insert into date1 (id, ner_date) values (74, 'Friday');
insert into date1 (id, ner_date) values (75, 'August 26');
insert into date1 (id, ner_date) values (76, 'September 13 September 13');
insert into date1 (id, ner_date) values (77, 'November 7');
insert into date1 (id, ner_date) values (78, 'Monday, Tuesday', 'DATE');
insert into date1 (id, ner_date) values (79, '2002');
insert into date1 (id, ner_date) values (80, 'the 2024');
insert into date1 (id, ner_date) values (81, 'October 8, 2024');
insert into date1 (id, ner_date) values (82, 'September 14 September 14');
insert into date1 (id, ner_date) values (83, 'September 18 September 18');
insert into date1 (id, ner_date) values (84, 'September 29 September 29');
insert into date1 (id, ner_date) values (85, 'September 16');
insert into date1 (id, ner_date) values (86, 'This Christmas');
insert into date1 (id, ner_date) values (87, 'September 14');
insert into date1 (id, ner_date) values (88, 'September 19, 2024');
insert into date1 (id, ner_date) values (89, 'June 20');
insert into date1 (id, ner_date) values (90, 'the year');
insert into date1 (id, ner_date) values (91, 'September 17 September 17');
insert into date1 (id, ner_date) values (92, 'Sunday to Thursday');
insert into date1 (id, ner_date) values (93, 'March 15');
insert into date1 (id, ner_date) values (94, 'late 2024');
insert into date1 (id, ner_date) values (95, 'September 15');
insert into date1 (id, ner_date) values (96, 'November 26, 2024');
insert into date1 (id, ner_date) values (97, 'June 6th 2023');
insert into date1 (id, ner_date) values (98, 'September 6 Select date');
insert into date1 (id, ner_date) values (99, 'November 30');
insert into date1 (id, ner_date) values (100, 'October 3 October 3');
insert into date1 (id, ner_date) values (101, 'each day');
insert into date1 (id, ner_date) values (102, 'October 29');
insert into date1 (id, ner_date) values (103, 'October 4 October 4');
insert into date1 (id, ner_date) values (104, 'September 20 September 20');
insert into date1 (id, ner_date) values (105, 'November 18th');
insert into date1 (id, ner_date) values (106, 'October 15');
insert into date1 (id, ner_date) values (107, '1995');
insert into date1 (id, ner_date) values (108, 'under 18 years');
insert into date1 (id, ner_date) values (109, 'September 21');
insert into date1 (id, ner_date) values (110, 'today');
insert into date1 (id, ner_date) values (111, 'September 23');
insert into date1 (id, ner_date) values (112, 'September 4');
insert into date1 (id, ner_date) values (113, 'December 5');
insert into date1 (id, ner_date) values (114, 'the day');
insert into date1 (id, ner_date) values (115, 'November 21');
insert into date1 (id, ner_date) values (116, 'September 8 September 8');
insert into date1 (id, ner_date) values (117, '12 September 12');
insert into date1 (id, ner_date) values (118, 'September 12, 2024');
insert into date1 (id, ner_date) values (119, 'September');
insert into date1 (id, ner_date) values (120, 'October 10, 2024');
insert into date1 (id, ner_date) values (121, 'June 3');
insert into date1 (id, ner_date) values (122, 'October 5');
insert into date1 (id, ner_date) values (123, 'the mid 80’s and the third in 2000');
insert into date1 (id, ner_date) values (124, 'October 29, 2024');
insert into date1 (id, ner_date) values (125, 'September 20');
insert into date1 (id, ner_date) values (126, 'December 12th 2022');
insert into date1 (id, ner_date) values (127, 'September 5 September 5');
insert into date1 (id, ner_date) values (128, 'September 11, 2024');
insert into date1 (id, ner_date) values (129, 'October 4');
insert into date1 (id, ner_date) values (130, 'November 19, 2024');
insert into date1 (id, ner_date) values (131, 'December 5 This year');
insert into date1 (id, ner_date) values (132, 'the last Wednesday of the month');
insert into date1 (id, ner_date) values (133, 'September 2');
insert into date1 (id, ner_date) values (134, 'Aug This Month');
insert into date1 (id, ner_date) values (135, 'August 26 August 26');
insert into date1 (id, ner_date) values (136, 'September 5');
insert into date1 (id, ner_date) values (137, 'September 3 September 3');
insert into date1 (id, ner_date) values (138, '2020-21');
insert into date1 (id, ner_date) values (139, 'Tuesday 5th November');
insert into date1 (id, ner_date) values (140, 'October 2 October 2');
insert into date1 (id, ner_date) values (141, 'the age of 25');
insert into date1 (id, ner_date) values (142, 'December 15th 2023');
insert into date1 (id, ner_date) values (143, 'September 16 September 16');
insert into date1 (id, ner_date) values (144, 'September 24th 2023');
insert into date1 (id, ner_date) values (145, 'October 31');
insert into date1 (id, ner_date) values (146, 'August 29');
insert into date1 (id, ner_date) values (147, '7 Days');
insert into date1 (id, ner_date) values (148, 'November 5');
insert into date1 (id, ner_date) values (149, 'May');
insert into date1 (id, ner_date) values (150, 'September 10, 2024');
insert into date1 (id, ner_date) values (151, 'October 25');
insert into date1 (id, ner_date) values (152, 'September 18, 2024');
insert into date1 (id, ner_date) values (153, '2009');
insert into date1 (id, ner_date) values (154, 'the last twenty years');
insert into date1 (id, ner_date) values (155, 'Sunday 2');
insert into date1 (id, ner_date) values (156, '2021');
insert into date1 (id, ner_date) values (157, 'February 9th');
insert into date1 (id, ner_date) values (158, 'September 9');
insert into date1 (id, ner_date) values (159, 'October 17, 2024');
insert into date1 (id, ner_date) values (160, 'March 2024');
insert into date1 (id, ner_date) values (161, 'September 1');
insert into date1 (id, ner_date) values (162, 'early December');
insert into date1 (id, ner_date) values (163, 'September 11');
insert into date1 (id, ner_date) values (164, 'February');
insert into date1 (id, ner_date) values (165, 'April 12th');
insert into date1 (id, ner_date) values (166, 'October 30th');
insert into date1 (id, ner_date) values (167, 'THE YEAR 2008 2009');
insert into date1 (id, ner_date) values (168, 'October 5 October 5');
insert into date1 (id, ner_date) values (169, '07 5573 1491Our');
insert into date1 (id, ner_date) values (170, 'September 26');
insert into date1 (id, ner_date) values (171, 'September 2 September 2');
insert into date1 (id, ner_date) values (172, '2023');
insert into date1 (id, ner_date) values (173, 'September 6');
insert into date1 (id, ner_date) values (174, 'Tuesday, November 5th');
insert into date1 (id, ner_date) values (175, 'Friday, Saturday and');
insert into date1 (id, ner_date) values (176, 'October 2');
insert into date1 (id, ner_date) values (177, 'next week');
insert into date1 (id, ner_date) values (178, 'September 19');
insert into date1 (id, ner_date) values (179, 'November 19');
insert into date1 (id, ner_date) values (180, 'three years in a row');
insert into date1 (id, ner_date) values (181, '07 5573');
insert into date1 (id, ner_date) values (182, '2014');
insert into date1 (id, ner_date) values (183, 'October 22');
insert into date1 (id, ner_date) values (184, 'under 25');
insert into date1 (id, ner_date) values (185, 'September 2024');
insert into date1 (id, ner_date) values (186, 'September 21 September 21');
insert into date1 (id, ner_date) values (187, 'September 25, 2024');
insert into date1 (id, ner_date) values (188, 'October 24');
insert into date1 (id, ner_date) values (189, 'January 2024');
insert into date1 (id, ner_date) values (190, 'July 31');
insert into date1 (id, ner_date) values (191, 'September 19 September 19');
insert into date1 (id, ner_date) values (192, 'September 10');
insert into date1 (id, ner_date) values (193, '07 5573 1491');
insert into date1 (id, ner_date) values (194, 'under 18');
insert into date1 (id, ner_date) values (195, 'Wednesday nights');
insert into date1 (id, ner_date) values (196, 'September 30 September 30');
insert into date1 (id, ner_date) values (197, 'November 14, 2024');
insert into date1 (id, ner_date) values (198, 'year-long');
insert into date1 (id, ner_date) values (199, 'September 4 September 4');
insert into date1 (id, ner_date) values (200, 'Saturday 12th October');
insert into date1 (id, ner_date) values (201, 'the early years');
insert into date1 (id, ner_date) values (202, 'many years');
insert into date1 (id, ner_date) values (203, '2004');
insert into date1 (id, ner_date) values (204, 'Remembrance Day');
insert into date1 (id, ner_date) values (205, 'February 7');
insert into date1 (id, ner_date) values (206, '2018');
insert into date1 (id, ner_date) values (207, 'August 27');
insert into date1 (id, ner_date) values (208, 'THE YEAR 2016 2006');
insert into date1 (id, ner_date) values (209, 'Sunday October 6th Celebrate Oktoberfest');
insert into date1 (id, ner_date) values (210, 'September 11 September 11');
insert into date1 (id, ner_date) values (211, 'Monday');
insert into date1 (id, ner_date) values (212, 'October 1, 2024');
insert into date1 (id, ner_date) values (213, 'October 17');
insert into date1 (id, ner_date) values (214, 'Friday September');
insert into date1 (id, ner_date) values (215, 'November 28, 2024');
insert into date1 (id, ner_date) values (216, 'September 24');
insert into date1 (id, ner_date) values (217, '2010');
insert into date1 (id, ner_date) values (218, 'October 1 October 1');
insert into date1 (id, ner_date) values (219, 'November 28');
insert into date1 (id, ner_date) values (220, 'October');
insert into date1 (id, ner_date) values (221, 'September 15 September 15');
insert into date1 (id, ner_date) values (222, 'October 3');
insert into date1 (id, ner_date) values (223, 'MAY 2024');
insert into date1 (id, ner_date) values (224, 'September 23 September 23');
insert into date1 (id, ner_date) values (225, 'September 30');
insert into date1 (id, ner_date) values (226, 'June 6');
insert into date1 (id, ner_date) values (227, 'August 30 August 30');
insert into date1 (id, ner_date) values (228, 'April 1');
insert into date1 (id, ner_date) values (229, 'August 31 August 31');
insert into date1 (id, ner_date) values (230, 'May 12');
insert into date1 (id, ner_date) values (231, 'August');
insert into date1 (id, ner_date) values (232, '4 days');
insert into date1 (id, ner_date) values (233, 'November 5, 2024');
insert into date1 (id, ner_date) values (234, 'Wednesday');
insert into date1 (id, ner_date) values (235, 'October 1');
insert into date1 (id, ner_date) values (236, '2022');
insert into date1 (id, ner_date) values (237, 'December 2023');
insert into date1 (id, ner_date) values (238, 'annual');
insert into date1 (id, ner_date) values (239, 'December of 2023');
insert into date1 (id, ner_date) values (240, 'a week');
insert into date1 (id, ner_date) values (241, 'November 26');
insert into date1 (id, ner_date) values (242, 'Sundays');
insert into date1 (id, ner_date) values (243, 'Saturday 12th of October');
insert into date1 (id, ner_date) values (244, 'Saturday');
insert into date1 (id, ner_date) values (245, 'September 22');
insert into date1 (id, ner_date) values (246, '5 days');
insert into date1 (id, ner_date) values (247, 'October 8');
insert into date1 (id, ner_date) values (248, '1 year');
insert into date1 (id, ner_date) values (249, 'November 21, 2024');