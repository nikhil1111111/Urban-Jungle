-- database/trees.sql
CREATE TABLE trees (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  tree_type VARCHAR(50) NOT NULL,
  location GEOGRAPHY(POINT, 4326) NOT NULL,
  planted_at TIMESTAMP NOT NULL DEFAULT NOW(),
  verified BOOLEAN DEFAULT FALSE
);

CREATE INDEX idx_trees_location ON trees USING GIST(location);