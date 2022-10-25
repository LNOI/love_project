CREATE DATABASE "love";
\c love
CREATE TABLE IF NOT EXISTS users (
        username varchar(100),
        password varchar(100)
);

-- CREATE TABLE IF NOT EXISTS media (
--         uuid varchar(50) not null primary key,
--         link varchar(255),
--         created_at timestamptz not null default now(),
--         media_links text [],
--         total_img int,
--         user_id int,
--         social_type varchar(100),
--         ai_metadata json,
--         CONSTRAINT fk_id
--         FOREIGN KEY(user_id) 
--         REFERENCES users(id) 
-- );

insert into users values (
    'thanhloi',
    'thanhloi' 
);
-- insert into media (uuid,link,media_links,total_img,user_id,social_type,ai_metadata) VALUES  (
--     'BEBGKmhBXY', 
--     'https://www.instagram.com/p/Ch1b1fsL39W/?utm_source=ig_web_copy_link', 
--     '{"link1","link2","link3","link4"}',
--     4,
--     1,
--     'instagram',
--     '{}'
-- );
