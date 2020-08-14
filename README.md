# urban-spoon
fastapi test project

To run the project 

setup db, using the shapefile from [Timezone boundary builder project](https://github.com/evansiroky/timezone-boundary-builder/releases/) and the postgis tool `shp2pgsl`
```sql
CREATE DATABASE tzdb;
\c tzdb
CREATE EXTENSION postgis;
```
export shapefile to db
```bash
shp2pgsql -D combined-shapefile.shp timezones | psql -U <db user> -d tzdb
```
then:

```bash
export DATABASE_URL=postgresql://user:password@localhost/tzdb
uvicorn main:app --reload
```
testing the endpoint:
```bash
curl -X GET "http://localhost:8000/timezone?latitude=12&longitude=-86" -H  "accept: application/json"

# result
{
  "name": "America/Managua"
}
```
