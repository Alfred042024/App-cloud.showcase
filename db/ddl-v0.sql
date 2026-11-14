    CREATE table urls (
        id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
        short_url text NOT NULL unique , 
        original_url text NOT NULL, 
        clicks bigint not NULL default 0,
        creation_date date not null default now()
    );  