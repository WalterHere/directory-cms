def preprocessing_filter_admin_spec(endpoints):
    """
    Filters all Wagtail Admin API endpoints from the Open API schema generated by drf-spectacular. Spec generated at
    /openui/ui/.
    """

    filtered = []
    for path, path_regex, method, callback in endpoints:
        # Remove all Wagtail admin endpoints
        if not path.startswith('/admin/'):
            filtered.append((path, path_regex, method, callback))
    return filtered
