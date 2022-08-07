# Catalog products

## Models
### Diagram
![image](https://github.com/laryssonalves/catalog-products/blob/aaa2ee14b120a134c3b6faffa6334ae28051c99a/er_diagram.png)

### Database
[Django Models](https://github.com/laryssonalves/catalog-products/blob/d4a998700b251ddf7e456650fd672d1c61e84164/catalog/app/models.py)

[Django ORM Query](https://github.com/laryssonalves/catalog-products/blob/d4a998700b251ddf7e456650fd672d1c61e84164/catalog/app/models.py#L49)

[SQL Query](https://github.com/laryssonalves/catalog-products/blob/d4a998700b251ddf7e456650fd672d1c61e84164/query.sql)

## Run the project
After clonning the project you gonna need to create the virtualenv and install the dependencies:
```bash
  cd catalog-products
```
```bash
  python3 -m venv venv
```
```bash
  source venv/bin/activate
```
```bash
  pip3 install -r requirements.txt
```
And then run the project:
```bash
  python3 catalog/manage.py runserver
```

# Execution timer
It shows the CPU and Wall clock execution time

[Script](https://github.com/laryssonalves/catalog-products/blob/d4a998700b251ddf7e456650fd672d1c61e84164/execution_timer.py)

## Run the script
```bash
  python3 execution_timer.py
```
