SELECT create_test_data_black_lists();

SELECT find_blacklist('hoge');

SELECT find_blacklist('white');

TRUNCATE TABLE black_lists RESTART IDENTITY;
