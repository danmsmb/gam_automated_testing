import contextvars
import logging
import os
import base64

import pytest
from pytest_bdd import given, then
from pytest_bdd.parsers import parse

import os, sys
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from pages.base_page import BasePage
from pages.login_page import LoginPage

"""
This module contains shared hooks, fixtures, and shared steps.
"""
import json
import allure

import pytest
from playwright.sync_api import Page, BrowserContext
from pytest_bdd import given, then
from pytest_bdd.parsers import parse

# Hooks
from datetime import datetime
import os ,  shutil
import uuid
import pytest
import allure
from pathlib import Path
from datetime import datetime
ARTIFACTS = Path("artifacts")
VIDEOS_DIR = ARTIFACTS / "videos"
ARTIFACTS.mkdir(parents=True, exist_ok=True)
VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
ALL_SHOTS = Path("artifacts/screenshots")
ALL_SHOTS.mkdir(parents=True, exist_ok=True)
from urllib.parse import urlsplit

# MERGED browser context args (session-scoped is fine)
@pytest.fixture(scope="session")
def browser_context_args():
    return {
        
        "permissions": ["geolocation"],
        "geolocation": {"latitude": 31.9539, "longitude": 35.9106},
        "timezone_id": "Asia/Amman",
        "record_video_dir": str(VIDEOS_DIR),
        "record_video_size": {"width": 1280, "height": 720},
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }




@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # save outcome so we can know pass/fail in teardown if we want
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def attach_screenshot_after_test(page, request):
    # page is a dependency, so this teardown runs BEFORE page() is torn down
    yield
    try:
        # attach bytes directly to Allure
        png_bytes = page.screenshot(full_page=True)
        name = f"{request.node.name}-final"
        allure.attach(png_bytes, name=name, attachment_type=allure.attachment_type.PNG)
    except Exception:
        pass

@pytest.fixture
def page(context, request):
    p = context.new_page()
    yield p
    # ---- teardown: finalize video, then attach to Allure ----
    try:
        p.close()   # this flushes the .webm to disk
    except Exception:
        pass
    try:
        if p.video:
            src = p.video.path()  # now exists because page is closed
            dest = VIDEOS_DIR / f"{request.node.name}.webm"
            shutil.copyfile(src, dest)  # optional: nicer name/location
            allure.attach.file(
                str(dest),
                name="video",
                attachment_type=allure.attachment_type.WEBM
            )
    except Exception:
        pass


# Hook triggered whenever a BDD step fails during test execution printing the failed step text
def pytest_bdd_step_error(step):
    print(f'Step failed: {step}')


# Fixtures
@pytest.fixture(scope='session')
def config():
    with open('config.json') as f:
        config_data = json.load(f)
    return config_data


@given('User is on the login page')
def user_on_login_page(page: Page, config):
    LoginPage(page).load(config)

@given(parse("{user_role} is logged in"))
def user_is_logged_in(page: Page, user_role, config):
    LoginPage(page).load(config)
    LoginPage(page).login(user_role, config)