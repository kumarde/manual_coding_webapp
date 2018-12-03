CREATE TABLE IF NOT EXISTS zzma(
    id integer PRIMARY KEY,
    tweet text NOT NULL,
    label text NOT NULL,
    isVerified integer NOT NULL,
    answer integer NOT NULL
);

CREATE TABLE IF NOT EXISTS kumarde(
    id integer PRIMARY KEY,
    tweet text NOT NULL,
    label text NOT NULL,
    isVerified integer NOT NULL,
    answer integer NOT NULL
);
