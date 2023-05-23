import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    @pytest.mark.smoke
    def test_login_none_existing_user(self):
        print("*******")
        print("TEST LOGIN NON EXISTING")
        print("*******")
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('adfjladkf')
        my_account.input_login_password('adfadfadf')
        my_account.click_login_button()

        # verify error message
        expected_err = 'Unknown username. Check again or try your email address.'
        # expected_err = 'ERROR: Invalid username. Lost your password?'
        my_account.wait_until_error_is_displayed(expected_err)