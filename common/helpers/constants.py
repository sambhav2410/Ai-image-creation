from dataclasses import dataclass


@dataclass
class StatusCodes(object):
    def __init__(self):
        self.SUCCESS = 200
        self.CREATED = 201
        self.NO_CONTENT = 204
        self.BAD_REQUEST = 400
        self.UNAUTHORIZED = 401
        self.FORBIDDEN = 403
        self.NOT_FOUND = 404
        self.UNPROCESSABLE_ENTITY = 422
        self.ISE = 500
        self.BAD_GATEWAY = 502
        self.SERVICE_UNAVAILABLE = 503


obj_status_codes = StatusCodes()
StatusCodesDictionary = obj_status_codes.__dict__


@dataclass
class UserObStatus(object):
    def __init__(self):
        self.NOT_ONBOARDED = 0
        self.ONBOARDED = 1
        self.LOCKED = 2
        self.DEBOARDED = 3
        self.BD_ONBOARDED = 4


obj_user_ob_status = UserObStatus()
UserStatusDictionary = obj_user_ob_status.__dict__


@dataclass
class UserStatus(object):
    def __init__(self):
        self.INACTIVE = 0
        self.ACTIVE = 1


obj_user_status = UserStatus()
UserStatusDictionary = obj_user_status.__dict__


@dataclass
class OtpAction(object):
    def __init__(self):
        self.REGISTER = 1
        self.LOGIN = 2
        self.FORGOT_PASSWORD = 2
        self.CHANGE_MOBILE = 3


obj_otp_action = OtpAction()
OtpActionDictionary = obj_otp_action.__dict__


@dataclass
class RouteStatus(object):
    def __init__(self):
        self.INACTIVE = 0
        self.ACTIVE = 1
        self.REQUEST_FOR_DELETION = 2
        self.DELETION_READY = 3


obj_route_status = RouteStatus()
RouteStatusDictionary = obj_route_status.__dict__


@dataclass
class LanguagePrefrence(object):
    def __init__(self):
        self.English = 1
        self.Hindi = 2


obj_lang_status = LanguagePrefrence()
LangPrefDictionary = obj_lang_status.__dict__


class GatewaySource(object):
    def __init__(self):
        self.JUSPAY = 1
        self.EASEBUZZ = 2


obj_gatway_status = GatewaySource()
GatewayPrefDictionary = obj_gatway_status.__dict__


class TransactionType(object):
    def __init__(self):
        self.CASH = 1
        self.DIGITAL = 2


obj_transaction_type = TransactionType()
TransactionTypeDictionary = obj_transaction_type.__dict__


class BusCategory(object):
    def __init__(self):
        self.GENERAL = 1
        self.EXPRESS = 2
        self.LUXURY = 3


obj_bus_category_type = BusCategory()
BusCategoryTypeDictionary = obj_bus_category_type.__dict__


class SeatType(object):
    def __init__(self):
        self.SEATER = 1
        self.SLEEPER = 2
        self.SEATER_SLEEPER = 3


obj_seat_type = SeatType()
SeatTypeDictionary = obj_seat_type.__dict__


class GpsStatus(object):
    def __init__(self):
        self.INSTALLED = 1
        self.NOT_INSTALLED = 2
        self.FAULTY = 3
        self.IN_PROGRESS = 4


obj_gps_status = GpsStatus()
GpsStatusDictionary = obj_gps_status.__dict__


class OnlineBookingCommission(object):
    def __init__(self):
        self.FIXED = 1
        self.PERCENTAGE = 2


obj_online_booking_commission_status = OnlineBookingCommission()
OnlineBookingCommissionDictionary = obj_online_booking_commission_status.__dict__


