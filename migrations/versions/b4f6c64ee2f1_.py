Traceback (most recent call last):
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: no such table: footer_content

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Scripts\flask.exe\__main__.py", line 7, in <module>
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask\cli.py", line 1064, in main
    cli.main()
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\click\core.py", line 1078, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\click\core.py", line 1688, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\click\core.py", line 1688, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\click\core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\click\core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\click\decorators.py", line 33, in new_func
    return f(get_current_context(), *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask\cli.py", line 358, in decorator
    return __ctx.invoke(f, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\click\core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_migrate\cli.py", line 150, in upgrade
    _upgrade(directory, revision, sql, tag, x_arg)
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_migrate\__init__.py", line 111, in wrapped
    f(*args, **kwargs)
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\flask_migrate\__init__.py", line 200, in upgrade
    command.upgrade(config, revision, sql=sql, tag=tag)
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\command.py", line 403, in upgrade
    script.run_env()
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\script\base.py", line 583, in run_env
    util.load_python_file(self.dir, "env.py")
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\util\pyfiles.py", line 95, in load_python_file
    module = load_module_py(module_id, path)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\util\pyfiles.py", line 113, in load_module_py
    spec.loader.exec_module(module)  # type: ignore
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\Users\Ali\Desktop\visual yedek7  BUNDAN FİNAL\migrations\env.py", line 113, in <module>
    run_migrations_online()
  File "C:\Users\Ali\Desktop\visual yedek7  BUNDAN FİNAL\migrations\env.py", line 107, in run_migrations_online
    context.run_migrations()
  File "<string>", line 8, in run_migrations
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\runtime\environment.py", line 948, in run_migrations
    self.get_context().run_migrations(**kw)
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\runtime\migration.py", line 627, in run_migrations
    step.migration_fn(**kw)
  File "C:\Users\Ali\Desktop\visual yedek7  BUNDAN FİNAL\migrations\versions\b4f6c64ee2f1_.py", line 21, in upgrade
    op.drop_table('footer_content')  # FooterContent tablosunu iptal et
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 8, in drop_table
  File "<string>", line 3, in drop_table
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\operations\ops.py", line 1408, in drop_table
    operations.invoke(op)
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\operations\base.py", line 445, in invoke
    return fn(self, operation)
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\operations\toimpl.py", line 82, in drop_table
    operations.impl.drop_table(
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\ddl\impl.py", line 389, in drop_table
    self._exec(schema.DropTable(table))
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\alembic\ddl\impl.py", line 207, in _exec
    return conn.execute(construct, multiparams)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1416, in execute
    return meth(
           ^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\sql\ddl.py", line 181, in _execute_on_connection
    return connection._execute_ddl(
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1528, in _execute_ddl
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 2344, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "C:\Users\Ali\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\engine\default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: footer_content
[SQL:
DROP TABLE footer_content]
(Background on this error at: https://sqlalche.me/e/20/e3q8)