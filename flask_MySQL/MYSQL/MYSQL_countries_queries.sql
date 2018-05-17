select c.name, l.language, l.percentage 
FROM countries c 
JOIN languages l ON c.code=l.country_code 
WHERE l.language = 'Slovene'
order by l.percentage DESC;

-------------

select count(cities.id) as total_number_of_cities, c.name 
from cities
JOIN
countries c ON c.code=cities.country_code
group by c.name
Order by total_number_of_cities DESC;

--------------
select cities.name , cities.population ,c.name
from cities
JOIN
countries c ON c.code=cities.country_code
where c.name='Mexico' and cities.population>500000
order by cities.population DESC;

--------------
select  c.name, l.language,l.percentage 
FROM countries c 
JOIN languages l ON c.code=l.country_code 
where l.percentage>89
group by c.name, l.language,l.percentage 
order by l.percentage DESC;

-----------------
select name, surface_area, population from countries where surface_area < 501 and population >100000;

-----------------
select name, government_form, capital, life_expectancy from countries where 
government_form = 'Constitutional Monarchy' AND capital > 200 and life_expectancy > 75;

-----------------

select c.name, cities.name, cities.district, cities.population
from cities
JOIN
countries c ON c.code=cities.country_code
where cities.population >500000 and c.name='Argentina' and cities.district='Buenos Aires';

-------------------

select region, count(name) as count
from countries 
group by region
order by count(name) DESC;
