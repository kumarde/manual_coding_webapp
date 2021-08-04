CREATE TABLE IF NOT EXISTS responses(
    id integer PRIMARY KEY,
    comment_id text NOT NULL,
    body text NOT NULL,
    tweet_id text NOT NULL,
    mturk_id text NOT NULL,
    toxic_rating integer NOT NULL,
    see_online integer NOT NULL,
    remove_online NOT NULL
)
