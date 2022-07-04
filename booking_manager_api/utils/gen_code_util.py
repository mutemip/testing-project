from intel_api.utils.generate_rand_codes import generate_rand_pin


def gen_booking_code():
    initial = "BO"
    return "{}{}".format(initial, generate_rand_pin(8))