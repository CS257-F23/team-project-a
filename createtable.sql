DROP TABLE IF EXISTS exoplanet_data;
CREATE TABLE exoplanet_data (
  planet_name text,
  discovery_method text,
  discovery_year int,
  discovery_facility text,
  semi_major_axis float,
  planet_radius float,
  planet_mass float,
  galactic_latitude float, 
  galactic_longitude float,
  host_id int
);

DROP TABLE IF EXISTS star_data;
CREATE TABLE star_data (
  host_id int,
  host_name text,
  number_of_stars int,
  number_of_planets int,
  stellar_radius float,
  stellar_mass float,
  stellar_luminosity float
);