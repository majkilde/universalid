# Nano Id -> https://github.com/puyuan/py-nanoid
# Nano Id collision calculator -> https://zelark.github.io/nano-id-cc/
# Universal ID in Lotus Notes -> https://www-01.ibm.com/support/docview.wss?uid=swg21112556

from datetime import datetime
from secrets import randbelow


# UNID format, default length = 32:
# * Position 1-20: Custom - defaults to a random (20 digits)
# * Position 21-27: Date/time (7 digits)
# * Position 28-31: microseconds (4 digits)
# * Position 32: sequence (1 digig)

class Unid:
    BASE = 36  # (a-z + 10)

    CUSTOM_LENGTH = 20
    SEQUENCE_LENGTH = 1
    DATETIME_LENGTH = 11  # total length of the datetime part, incl. the microseconds
    TOTAL_LENGTH = CUSTOM_LENGTH + DATETIME_LENGTH + SEQUENCE_LENGTH  # total length of unid to generate

    time_sequence = 0

    # Max values with base 36
    #   1 digit:    35
    #   2 digits:   1.295
    #   3 digits:   46.655
    #   4 digits:   1.679.615
    #   5 digits:   60.466.175
    #   6 digits:   2.176.782.335

    @staticmethod
    def create(time=None, prefix=None):
        time = time if time else datetime.utcnow()
        prefix = prefix if prefix else ""

        # start with the optional prefix
        unid = prefix[:Unid.CUSTOM_LENGTH]

        # add random chars
        size = Unid.CUSTOM_LENGTH - len(prefix)
        unid += Unid._get_random(size)

        # add the datetime
        unid += Unid._encode_time(time)

        # add the sequence
        unid += Unid._digit_to_char(Unid._inc_sequence())

        return unid.upper()

    @staticmethod
    def get_time(unid):
        # decode the datetime
        date_str = unid[-12:-5]

        timestamp = Unid._str_to_int(date_str)
        date = datetime.fromtimestamp(timestamp)

        # decode the microseconds
        micro_str = unid[-5:-1]
        microsecond = Unid._str_to_int(micro_str)

        # return
        date = date.replace(microsecond=microsecond)
        return date

    @staticmethod
    def _inc_sequence():
        result = Unid.time_sequence
        Unid.time_sequence += 1
        if Unid.time_sequence == Unid.BASE:
            Unid.time_sequence = 0
        return result

    @staticmethod
    def _get_random(length):
        s = ""
        while len(s) < length:
            r = randbelow(Unid.BASE)
            s += Unid._digit_to_char(r)
        return s

    @staticmethod
    def _encode_time(time):
        time_unid = Unid._int_to_str(int(time.timestamp()), 7)
        micro_unid = Unid._int_to_str(time.microsecond, 4)

        return time_unid + micro_unid

    @staticmethod
    def _int_to_str(number, width):
        # convert to string
        s = Unid._str_base(number)

        # If number is to big, then return largest possible number
        if len(s) > width:
            return Unid._digit_to_char(Unid.BASE - 1) * width

        # Return the number, padded with zeros
        return ('0' * width + s)[-width:]

    @staticmethod
    def _str_to_int(s):
        i = int(s, base=Unid.BASE)
        return i

    @staticmethod
    def _digit_to_char(digit):
        # encode a single digit to a char
        if digit < 10:
            return str(digit)
        return chr(ord('a') + digit - 10)

    @staticmethod
    def _str_base(number):
        # convert a number to an encoded string
        (d, m) = divmod(abs(number), Unid.BASE)
        if d > 0:
            return Unid._str_base(d) + Unid._digit_to_char(m)
        return Unid._digit_to_char(m)
