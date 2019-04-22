import pytest
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.baidu.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
            extra.append (pytest_html.extras.json({'name': 'pytest'}))
            extra.append (pytest_html.extras.image('https://www.baidu.com/img/xinshouye_c9d9de2ff40fa160f807f75f34db4ad0.gif'))
        report.extra = extra