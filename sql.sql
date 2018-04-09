CREATE TABLE AptBuilding
(
  id        INTEGER       PRIMARY KEY,
  name      VARCHAR(225) ,
  address_1 VARCHAR(128) ,
  address_2 VARCHAR(128) ,
  city      VARCHAR(225) ,
  state     VARCHAR(225) ,
  zip_code  VARCHAR(5)   ,
  owner_id  INTEGER      
);

CREATE TABLE Apt_apt
(
  id             INTEGER  PRIMARY KEY,
  number         INTEGER ,
  allow_smocking bool    ,
  room_num       INTEGER ,
  aptBuilding_id INTEGER  REFERENCES AptBuilding
);

CREATE TABLE Contract
(
  id              INTEGER       PRIMARY KEY,
  active          bool         ,
  start_date      DATE         ,
  end_date        DATE         ,
  payment_process VARCHAR(255) ,
  price           REAL         ,
  deposit         REAL         ,
  apt_id          INTEGER       REFERENCES Apt_apt,
  owner_id        INTEGER      ,
  renter_id       INTEGER      
);

CREATE TABLE Job
(
  id             INTEGER       PRIMARY KEY,
  title          VARCHAR(255) ,
  hours_week     INTEGER      ,
  price_per_hour REAL         ,
  owner_id       INTEGER      ,
  worker_id      INTEGER      
);

CREATE TABLE Job_apt
(
  id     INTEGER  PRIMARY KEY,
  job_id INTEGER  REFERENCES Job_job,
  apt_id INTEGER  REFERENCES Apt_apt
);

CREATE TABLE Owner
(
  id        INTEGER       PRIMARY KEY,
  address_1 VARCHAR(128) ,
  address_2 VARCHAR(128) ,
  city      VARCHAR(225) ,
  state     VARCHAR(225) ,
  zip_code  VARCHAR(5)   ,
  user_id   INTEGER UNIQUE
);


CREATE TABLE Renter
(
  id         INTEGER       PRIMARY KEY,
  has_animal bool         ,
  is_smoker  bool         ,
  is_single  bool         ,
  job        VARCHAR(225) ,
  user_id    INTEGER UNIQUE
);

CREATE TABLE Worker
(
  id      INTEGER       PRIMARY KEY,
  skill   VARCHAR(300) ,
  user_id INTEGER UNIQUE
);

CREATE TABLE user
(
  id           INTEGER       PRIMARY KEY,
  password     VARCHAR(128) ,
  first_name   VARCHAR(30)  ,
  last_name    VARCHAR(30)  ,
  email        VARCHAR(254) ,
  username     VARCHAR(150)  UNIQUE
);

