PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
    id integer primary key,
    username text not null,
    password text not null,
    age text,
    gender text ,
    interest text 
);

INSERT INTO "users" VALUES(1,'test','123','23','Male','Computers');
INSERT INTO "users" VALUES(2,'test1','foo','23','Female','Science');
INSERT INTO "users" VALUES(3,'test2','bar','32','Male','Arts');
INSERT INTO "users" VALUES(4,'test3','baz','34','Female','Dance');
COMMIT;
