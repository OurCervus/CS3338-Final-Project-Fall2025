-- db/init.sql
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS content_items (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  category TEXT,
  is_mandatory BOOLEAN DEFAULT FALSE,
  start_date DATE,
  end_date DATE
);
