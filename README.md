# Resturant-Managenement-System
Modern Resturant Management System which includes Multi-Tenancy ..


## After creating a database
~~~
CREATE TABLE public.custom_user (
    id BIGSERIAL PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login TIMESTAMPTZ NULL,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(254) NOT NULL UNIQUE,
    first_name VARCHAR(200) NOT NULL,
    middle_name VARCHAR(200),
    last_name VARCHAR(200) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE,
    is_staff BOOLEAN NOT NULL DEFAULT FALSE,
    is_superuser BOOLEAN NOT NULL DEFAULT FALSE,
    role VARCHAR(20) NOT NULL DEFAULT 'CUSTOMER',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
	auth_provider VARCHAR(20) NOT NULL DEFAULT 'email'
    );

~~~
## After executing the query then only
~~~
python manage.py migrate_schemas
python manage.py migrate
~~~

## To create a tenant
~~~
python manage.py create_tenant
~~~

## To create admin specific to schema

~~~
python manage.py create_admin --schema=schema_name --username=username --email=email --password=password 
~~~
