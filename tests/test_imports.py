# tests/test_imports.py
def test_import_cleanup_old_pipelines():
    from providers.gitlab.recipes import cleanup_old_pipelines

    assert hasattr(cleanup_old_pipelines, "main")
