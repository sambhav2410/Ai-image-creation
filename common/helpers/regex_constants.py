from dataclasses import dataclass


@dataclass
class CommonRegex(object):
    def __init__(self):
        self.user_name_input_regex = r"^[a-zA-Z]+(?: [a-zA-Z]+)*$"
        self.user_contact_input_regex = r"(\+)?(91)?( )?[56789]\d{9}"
        self.user_country_code_input_regex = r"^\+\d+$"
        self.job_input_regex = (
            r"^[A-Za-z0-9][a-zA-Z0-9_\-/.(),:|#]+( [a-zA-Z0-9_\-/.(),:|#]+)*$"
        )
        self.job_search_regex = r"^[a-zA-Z0-9_\-/.(),:|#]+( [a-zA-Z0-9_\-/.(),:|#]+)*$"
        self.hiring_tracker_search_regex = r"^[a-zA-Z0-9@.\-]+( [a-zA-Z0-9@.\-]+)*$"
        self.interview_title_input_regex = r"^[a-zA-Z0-9 -.\'\_]+$"
        self.password_input_regex = (
            r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"
        )
        self.url_validation_regex = r"^(https?:\/\/)?([\da-z\.-]+\.[a-z\.]{2,6}|[\d\.]+)([\/:?=&#]{1}[\da-z\.-]+)*[\/\?]?$"
        self.base64_validation_regex = r"^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$"
