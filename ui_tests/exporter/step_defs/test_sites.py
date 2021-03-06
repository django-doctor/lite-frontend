from django.utils import timezone
from faker import Faker
from pytest_bdd import scenarios, when, then

from tests_common import functions
from ui_tests.exporter.pages.hub_page import Hub
from ui_tests.exporter.pages.new_site_page import NewSite
from ui_tests.exporter.pages.site_list_overview_page import SitesListOverview
from ui_tests.exporter.pages.site_page import SitePage

scenarios("../features/sites.feature", strict_gherkin=False)
faker = Faker()


@when("I click new site")
def click_new_site(driver):
    sites = SitesListOverview(driver)
    sites.click_new_site_link()


@when("I specify that my site is in the United Kingdom")
def site_is_in_uk(driver):
    NewSite(driver).click_in_the_united_kingdom_radiobutton()
    functions.click_submit(driver)


@when("I click sites link")
def click_new_site(driver):
    hub = Hub(driver)
    hub.click_sites_link()


@when("I enter in the site details")
def new_sites_info(driver, context):
    context.new_site_name = faker.word() + timezone.localtime().strftime("%m%d%H%M")
    NewSite(driver).enter_new_site_details(
        context.new_site_name, faker.street_address(), faker.postcode(), faker.city(), faker.state()
    )
    functions.click_submit(driver)


@when("I select that the records for licences are held at this site")
def site_records_held_at_the_same_site(driver):
    NewSite(driver).click_same_site_as_site_where_records_located_at()
    functions.click_submit(driver)


@when("I assign all users")
def assign_all_users(driver, context):
    NewSite(driver).click_all_users()
    functions.click_submit(driver)


@then("the site is created")
@then("the site is updated")
def site_is_created_updated(driver, context):
    assert context.new_site_name in driver.title


@when("I click the change name link")
def click_edit_button(driver):
    SitePage(driver).click_change_name_link()


@when("I change the site name")
def clear_site(driver, context):
    context.new_site_name = faker.word() + timezone.localtime().strftime("%m%d%H%M")
    NewSite(driver).change_site_name(context.new_site_name)
    functions.click_submit(driver)
